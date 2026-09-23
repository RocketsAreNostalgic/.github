<?php
/** Audit-aid declaration/caller inventory; output is a new local measurement, not historical provenance. */
declare(strict_types=1);

if ($argc !== 4) {
    fwrite(STDERR, "Usage: php inventory-php-names.php SNAPSHOT_ROOT PARSER_VENDOR_AUTOLOAD OUTPUT_JSON\n");
    exit(1);
}
require $argv[2];
$root = realpath($argv[1]);
$composerInstalled = dirname($argv[2]) . '/composer/installed.json';
if (!is_file($composerInstalled)) {
    throw new RuntimeException('Parser Composer installed metadata is required.');
}
$installed = json_decode((string) file_get_contents($composerInstalled), true, 512, JSON_THROW_ON_ERROR);
$packages = $installed['packages'] ?? $installed;
$parserPackage = null;
foreach ($packages as $package) {
    if (($package['name'] ?? null) === 'nikic/php-parser') {
        $parserPackage = $package;
        break;
    }
}
if (!is_array($parserPackage)) {
    throw new RuntimeException('nikic/php-parser package identity is missing.');
}
$parserIdentity = [
    'name' => 'nikic/php-parser',
    'version' => $parserPackage['version'] ?? null,
    'reference' => $parserPackage['source']['reference'] ?? null,
];
$parser = (new PhpParser\ParserFactory())->createForNewestSupportedVersion();
$out = ['toolchain' => ['parser' => $parserIdentity], 'classes' => [], 'methods' => [], 'properties' => [], 'parameters' => [], 'variables' => [], 'calls' => [], 'strings' => [], 'named_arguments' => [], 'files' => [], 'errors' => []];
$visibility = static fn(int $flags): string => ($flags & 4) ? 'private' : (($flags & 2) ? 'protected' : 'public');
$typeName = static function ($type): ?string {
    if ($type instanceof PhpParser\Node\Name) {
        return $type->toString();
    }
    if ($type instanceof PhpParser\Node\NullableType && $type->type instanceof PhpParser\Node\Name) {
        return $type->type->toString();
    }
    return null;
};
$walk = function ($node, array $ctx) use (&$walk, &$out, $visibility, $typeName): void {
    if (!$node instanceof PhpParser\Node) {
        return;
    }
    $at = ['repo' => $ctx['repo'], 'file' => $ctx['file'], 'line' => $node->getStartLine()];
    if ($node instanceof PhpParser\Node\Stmt\ClassLike) {
        $ctx['class'] = isset($node->namespacedName) ? $node->namespacedName->toString() : '@anonymous:' . $ctx['file'] . ':' . $node->getStartLine();
        $ctx['scope'] = $ctx['class'];
        $ctx['field_types'] = [];
        $parents = [];
        foreach (['extends', 'implements'] as $field) {
            foreach ((array) (isset($node->$field) ? (is_array($node->$field) ? $node->$field : [$node->$field]) : []) as $parent) {
                $parents[] = $parent->toString();
            }
        }
        foreach ($node->getProperties() as $property) {
            foreach ($property->props as $item) {
                $ctx['field_types'][$item->name->toString()] = $typeName($property->type);
            }
        }
        foreach ($node->getMethods() as $method) {
            foreach ($method->params as $param) {
                if ($param->flags && is_string($param->var->name)) {
                    $ctx['field_types'][$param->var->name] = $typeName($param->type);
                }
            }
        }
        $ctx['parents'] = $parents;
        $out['classes'][] = $at + ['class' => $ctx['class'], 'kind' => $node->getType(), 'parents' => $parents];
    }
    if ($node instanceof PhpParser\Node\FunctionLike) {
        $name = $node instanceof PhpParser\Node\Stmt\ClassMethod || $node instanceof PhpParser\Node\Stmt\Function_ ? $node->name->toString() : '@closure:' . $node->getStartFilePos();
        $ctx['scope'] = $ctx['class'] . '::' . $name . ':' . $node->getStartLine();
        $ctx['types'] = [];
        $ctx['params'] = [];
        $methodVisibility = $node instanceof PhpParser\Node\Stmt\ClassMethod ? $visibility($node->flags) : null;
        if ($node instanceof PhpParser\Node\Stmt\ClassMethod) {
            $methodAt = $at;
            $methodAt['line'] = $node->name->getStartLine();
            $out['methods'][] = $methodAt + ['class' => $ctx['class'], 'name' => $name, 'visibility' => $methodVisibility, 'abstract' => $node->isAbstract(), 'static' => $node->isStatic()];
        }
        foreach ($node->getParams() as $param) {
            $paramName = $param->var->name;
            if (!is_string($paramName)) {
                continue;
            }
            $ctx['types'][$paramName] = $typeName($param->type);
            $ctx['params'][$paramName] = true;
            $row = ['repo' => $ctx['repo'], 'file' => $ctx['file'], 'line' => $param->var->getStartLine(), 'class' => $ctx['class'], 'scope' => $ctx['scope'], 'name' => $paramName, 'visibility' => $methodVisibility];
            $out['parameters'][] = $row;
            if ($param->flags) {
                $row['visibility'] = $visibility($param->flags);
                $row['promoted'] = true;
                $out['properties'][] = $row;
            }
        }
    }
    if ($node instanceof PhpParser\Node\Stmt\Property) {
        foreach ($node->props as $item) {
            $propertyAt = $at;
            $propertyAt['line'] = $item->name->getStartLine();
            $out['properties'][] = $propertyAt + ['class' => $ctx['class'], 'name' => $item->name->toString(), 'visibility' => $visibility($node->flags), 'promoted' => false];
        }
    }
    if ($node instanceof PhpParser\Node\Expr\Variable && is_string($node->name)) {
        $key = implode('|', [$ctx['repo'], $ctx['file'], $ctx['scope'], $node->name]);
        if (!isset($out['variables'][$key])) {
            $out['variables'][$key] = $at + ['scope' => $ctx['scope'], 'name' => $node->name, 'parameter' => isset($ctx['params'][$node->name]), 'occurrences' => 0, 'lines' => []];
        }
        ++$out['variables'][$key]['occurrences'];
        $out['variables'][$key]['lines'][] = $node->getStartLine();
    }
    if ($node instanceof PhpParser\Node\Expr\MethodCall || $node instanceof PhpParser\Node\Expr\NullsafeMethodCall || $node instanceof PhpParser\Node\Expr\StaticCall) {
        $target = null;
        if ($node instanceof PhpParser\Node\Expr\StaticCall && $node->class instanceof PhpParser\Node\Name) {
            $target = $node->class->toString();
            if (in_array(strtolower($target), ['self', 'static'], true)) {
                $target = $ctx['class'];
            } elseif ('parent' === strtolower($target)) {
                $target = $ctx['parents'][0] ?? null;
            }
        } elseif (isset($node->var)) {
            $receiver = $node->var;
            if ($receiver instanceof PhpParser\Node\Expr\Variable && is_string($receiver->name)) {
                $target = 'this' === $receiver->name ? $ctx['class'] : ($ctx['types'][$receiver->name] ?? null);
            } elseif ($receiver instanceof PhpParser\Node\Expr\PropertyFetch && $receiver->var instanceof PhpParser\Node\Expr\Variable && 'this' === $receiver->var->name && $receiver->name instanceof PhpParser\Node\Identifier) {
                $target = $ctx['field_types'][$receiver->name->toString()] ?? null;
            } elseif ($receiver instanceof PhpParser\Node\Expr\New_ && $receiver->class instanceof PhpParser\Node\Name) {
                $target = $receiver->class->toString();
            }
        }
        $out['calls'][] = $at + ['method' => $node->name instanceof PhpParser\Node\Identifier ? $node->name->toString() : null, 'target' => $target, 'kind' => $node->getType()];
    }
    if ($node instanceof PhpParser\Node\Scalar\String_ && strlen($node->value) <= 160) {
        $out['strings'][] = $at + ['value' => $node->value];
    }
    if ($node instanceof PhpParser\Node\Arg && null !== $node->name) {
        $out['named_arguments'][] = $at + ['name' => $node->name->toString()];
    }
    foreach ($node->getSubNodeNames() as $field) {
        $value = $node->$field;
        foreach (is_array($value) ? $value : [$value] as $child) {
            $walk($child, $ctx);
        }
    }
};
foreach (glob($root . '/ran-*', GLOB_ONLYDIR) as $directory) {
    $repo = basename($directory);
    $chunks = [];
    exec('git -C ' . escapeshellarg($directory) . ' ls-files -z -- ' . escapeshellarg('*.php'), $chunks, $status);
    if (0 !== $status) {
        throw new RuntimeException("Unable to enumerate tracked PHP files for {$repo}.");
    }
    $paths = array_values(array_filter(explode("\0", implode("\n", $chunks)), static fn(string $path): bool => '' !== $path));
    foreach ($paths as $relative) {
        $pathname = $directory . '/' . $relative;
        $file = new SplFileInfo($pathname);
        if (!$file->isFile()) {
            throw new RuntimeException("Tracked PHP file is missing: {$repo}/{$relative}");
        }
        $out['files'][] = ['repo' => $repo, 'file' => $relative, 'sha256' => hash_file('sha256', $pathname)];
        try {
            $ast = $parser->parse(file_get_contents($pathname));
            $traverser = new PhpParser\NodeTraverser(new PhpParser\NodeVisitor\NameResolver());
            $ast = $traverser->traverse($ast);
            foreach ($ast as $node) {
                $walk($node, ['repo' => $repo, 'file' => $relative, 'class' => '', 'scope' => '@file', 'types' => [], 'params' => [], 'field_types' => [], 'parents' => []]);
            }
        } catch (Throwable $error) {
            $out['errors'][] = ['repo' => $repo, 'file' => $relative, 'error' => $error->getMessage()];
        }
    }
}
$out['variables'] = array_values($out['variables']);
$json = json_encode($out, JSON_UNESCAPED_SLASHES | JSON_PRETTY_PRINT | JSON_INVALID_UTF8_SUBSTITUTE | JSON_THROW_ON_ERROR) . "\n";
$written = file_put_contents($argv[3], $json);
if (false === $written || strlen($json) !== $written) {
    throw new RuntimeException('Failed to write the complete AST inventory output.');
}
printf("Parsed %d files; %d methods; %d properties; %d errors.\n", count($out['files']), count($out['methods']), count($out['properties']), count($out['errors']));
exit($out['errors'] ? 1 : 0);
