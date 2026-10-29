# Final cutover recovery point

This encrypted archive supplements `../2026-10-29`, which retains historical
backups and deployed course content. It captures the final authoritative source
after application requests and workers were stopped for PostgreSQL migration.
It includes every account, password hash, session, progress record and other
SQLite table, plus all mirrored uploads and exam files. It is a SQLite recovery
point, not a PostgreSQL dump. The original services and disks are retained.

Use `../reassemble.py` with this directory to create an encrypted `.tar.gpg`
outside Git, then decrypt using the owner's existing recovery passphrase.
Extract into a new isolated directory. The archive contains `snapshot.sqlite3`,
`files/`, and `files-manifest.json` (relative paths mapped to byte size and SHA256).
Verify SQLite integrity and foreign keys, and all file checksums before use.
The separately verified PostgreSQL migration bundle also includes application-only
content and frontend assets on the retained application disk. Environment secrets
and the recovery passphrase are never committed here.

After PostgreSQL accepts new writes, this pre-cutover snapshot alone is not a
lossless rollback. Preserve and reconcile later PostgreSQL changes first.
