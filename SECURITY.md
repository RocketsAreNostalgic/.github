# Security

Report security vulnerabilities privately whenever the repository provides a private vulnerability-reporting capability. On GitHub, use the repository's Security area and its **Report a vulnerability** option when available.

If private vulnerability reporting is unavailable, use the repository's `Security reporting help` issue form or equivalent public fallback only to request a confidential contact route. Do not include vulnerability details, exploit steps, reproduction traces, credentials, tokens, webhook secrets, WordPress salts, database contents, customer data, signed URLs, private source, private repository or site identities, release assets, full production logs, or other sensitive material in that public request.

In a private report, include the affected version, relevant environment details, impact, and the smallest reproduction information needed for maintainers to investigate. Redact private repository and site identities unless the private identity itself is directly necessary to understand the vulnerability.

Supported versions and security-fix policy are repository-specific. A repository that needs an explicit supported-version statement or a concrete private reporting URL should provide a local `SECURITY.md` while preserving this disclosure boundary.
