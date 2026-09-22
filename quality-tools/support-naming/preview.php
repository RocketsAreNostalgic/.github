<?php
/** Produce disposable rename previews from pinned Git objects; never edit a checkout. */
declare(strict_types=1);

function preview_path(string $path): void {
    if ('' === $path || '/' === $path[0] || false !== strpos($path, '\\')
        || preg_match('/[\x00-\x1f]/', $path)
        || array_intersect(array('.', '..', ''), explode('/', $path))) {
        throw new RuntimeException('Unsafe relative path: ' . $path);
    }
}

function preview_source(string $root, array $manifest, array $file): string {
    $repo = $file['repository'];
    preview_path($repo);
    preview_path($file['path']);
    if (false !== strpos($repo, '/') || !isset($manifest['repositories'][$repo])) {
        throw new RuntimeException('Unknown repository.');
    }
    $revision = $manifest['repositories'][$repo];
    if (!preg_match('/\A[0-9a-f]{40}\z/', $revision)) {
        throw new RuntimeException('An exact commit is required.');
    }
    $process = proc_open(
        array('git', '-C', $root . '/' . $repo, 'show', $revision . ':' . $file['path']),
        array(0 => array('pipe', 'r'), 1 => array('pipe', 'w'), 2 => array('pipe', 'w')),
        $pipes
    );
    if (!is_resource($process)) {
        throw new RuntimeException('Could not read pinned Git source.');
    }
    fclose($pipes[0]);
    $source = stream_get_contents($pipes[1]);
    $error = stream_get_contents($pipes[2]);
    fclose($pipes[1]);
    fclose($pipes[2]);
    if (0 !== proc_close($process) || !is_string($source)) {
        throw new RuntimeException('Pinned source unavailable: ' . $error);
    }
    if (!hash_equals($file['sha256'], hash('sha256', $source))) {
        throw new RuntimeException('Source hash mismatch: ' . $repo . '/' . $file['path']);
    }
    return $source;
}

function preview_rename(string $source, array $file): array {
    $rules = $file['tokens'] ?? array();
    $counts = array_fill(0, count($rules), 0);
    $seen = array();
    $destinations = array();
    foreach ($rules as $rule) {
        if (!in_array($rule['kind'], array('T_STRING', 'T_VARIABLE'), true)
            || !preg_match('/\A\$?[a-z_][a-z0-9_]*\z/', $rule['to'])
            || $rule['from'] === $rule['to'] || $rule['count'] < 1) {
            throw new RuntimeException('Invalid identifier rule.');
        }
        $key = $rule['kind'] . ':' . $rule['from'];
        if (isset($seen[$key])) {
            throw new RuntimeException('Duplicate identifier rule.');
        }
        $seen[$key] = true;
        $destination = $rule['kind'] . ':' . strtolower($rule['to']);
        if (isset($destinations[$destination])) {
            throw new RuntimeException('Colliding destination identifiers.');
        }
        $destinations[$destination] = true;
    }
    $result = '';
    // Exact source hashes make these reviewed per-file token mappings bounded.
    // This is not a general PHP symbol resolver or a global string substitution.
    foreach (empty($rules) ? array($source) : token_get_all($source, TOKEN_PARSE) as $token) {
        $text = is_array($token) ? $token[1] : $token;
        if (is_array($token)) {
            foreach ($rules as $index => $rule) {
                if (token_name($token[0]) !== $rule['kind']) {
                    continue;
                }
                if (0 === strcasecmp($text, $rule['to'])) {
                    throw new RuntimeException('Destination identifier already exists: ' . $rule['to']);
                }
                if ($text === $rule['from']) {
                    $text = $rule['to'];
                    ++$counts[$index];
                    break;
                }
            }
        }
        $result .= $text;
    }
    foreach ($rules as $index => $rule) {
        if ($counts[$index] !== $rule['count']) {
            throw new RuntimeException('Identifier count mismatch: ' . $rule['from']);
        }
    }
    $literal_count = 0;
    foreach ($file['literals'] ?? array() as $rule) {
        if (empty($rule['reason']) || '' === $rule['from']
            || substr_count($result, $rule['from']) !== $rule['count']) {
            throw new RuntimeException('Unreviewed literal or literal count mismatch.');
        }
        $result = str_replace($rule['from'], $rule['to'], $result);
        $literal_count += $rule['count'];
    }
    return array($result, array_sum($counts), $literal_count);
}

try {
    if (4 !== $argc) {
        throw new RuntimeException('Usage: php preview.php manifest.json REPOSITORY_PARENT NEW_OUTPUT_DIRECTORY');
    }
    $manifest = json_decode((string) file_get_contents($argv[1]), true, 512, JSON_THROW_ON_ERROR);
    if (1 !== $manifest['version']) {
        throw new RuntimeException('Unsupported manifest version.');
    }
    $root = realpath($argv[2]);
    $parent = realpath(dirname($argv[3]));
    $name = basename($argv[3]);
    if (false === $root || false === $parent || !preg_match('/\A[a-zA-Z0-9_-][a-zA-Z0-9._-]*\z/', $name)) {
        throw new RuntimeException('Existing input/output parents and a new directory name are required.');
    }
    $output = $parent . '/' . $name;
    if (file_exists($output) || is_link($output)) {
        throw new RuntimeException('Output already exists; refusing to overwrite it.');
    }
    foreach ($manifest['repositories'] as $repo => $revision) {
        preview_path($repo);
        $repo_root = realpath($root . '/' . $repo);
        if (false === $repo_root || $output === $repo_root || 0 === strpos($output, $repo_root . '/')) {
            throw new RuntimeException('Output must be outside the input repositories.');
        }
    }
    // Validate every source and generated-copy prerequisite before writing anything.
    foreach ($manifest['guards'] as $guard) {
        preview_source($root, $manifest, $guard);
    }
    $prepared = array();
    $report = array('revisions' => $manifest['repositories'], 'files' => array(),
        'pending_steps' => $manifest['derived_steps'] ?? array(),
        'generated_copy' => 'pending supported sync script; not hand-edited');
    foreach ($manifest['files'] as $file) {
        $path = $file['repository'] . '/' . $file['path'];
        if (isset($prepared[$path])) {
            throw new RuntimeException('Duplicate target path.');
        }
        list($contents, $tokens, $literals) = preview_rename(preview_source($root, $manifest, $file), $file);
        $prepared[$path] = $contents;
        $report['files'][$path] = array('token_edits' => $tokens, 'literal_edits' => $literals, 'sha256' => hash('sha256', $contents));
    }
    if (!mkdir($output, 0700)) {
        throw new RuntimeException('Could not create output directory.');
    }
    foreach ($prepared as $path => $contents) {
        $target = $output . '/' . $path;
        if (!is_dir(dirname($target)) && !mkdir(dirname($target), 0700, true)) {
            throw new RuntimeException('Could not create preview directory.');
        }
        if (strlen($contents) !== file_put_contents($target, $contents)) {
            throw new RuntimeException('Could not write preview file.');
        }
    }
    $json = json_encode($report, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES | JSON_THROW_ON_ERROR) . "\n";
    if (strlen($json) !== file_put_contents($output . '/preview.json', $json)) {
        throw new RuntimeException('Could not write preview report.');
    }
    echo $json;
} catch (Throwable $error) {
    fwrite(STDERR, $error->getMessage() . "\n");
    exit(1);
}
