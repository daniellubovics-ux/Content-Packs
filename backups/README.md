# Encrypted Telemetry backups

These archives contain sensitive live data. They are encrypted with GnuPG
AES-256 and a randomly generated 256-bit passphrase. The passphrase is kept
separately by the owner and is never committed here. Losing it makes the backup
unrecoverable. Keep an independent secure copy of it.

The backup includes the complete SQLite database (accounts, password hashes,
enrollments, progress and every other stored table), all mirrored data files,
historical database snapshots, and the deployed course content and packs.
The active database is captured through SQLite's online backup API. Source
file hashes are checked against the archive manifest and source files. Transient
SQLite WAL/SHM housekeeping files are excluded. No running service is paused
and no live records are modified. The internal encrypted MANIFEST.json contains
per-file SHA-256 hashes and source table counts for restoration checks.

This is a backup of the existing SQLite service, not a PostgreSQL conversion.
Application code is stored in the application repository. Hosting configuration,
environment secrets and external provider accounts must be restored separately;
they are not exported into this repository.

## Restore into an isolated directory

1. Install Git LFS, Python 3 and GnuPG. Clone this repository and run `git lfs pull`.
2. Choose a backup directory listed here and an empty recovery location outside
   all Git repositories. Reassemble the encrypted archive; this verifies every
   chunk and the complete ciphertext checksum:

   ```sh
   python backups/reassemble.py backups/2026-10-29 /secure/recovery/telemetry.tar.gz.gpg
   ```

3. Decrypt using the separately stored recovery passphrase. GnuPG prompts for it;
   do not put the passphrase directly on the command line:

   ```sh
   gpg --output /secure/recovery/telemetry.tar.gz --decrypt /secure/recovery/telemetry.tar.gz.gpg
   ```

4. Extract into an empty isolated directory. Verify all file hashes against
   MANIFEST.json, run SQLite `PRAGMA integrity_check` on `data/db/telemetry.db`,
   and compare table counts with the manifest before using the restored data.
   `data/files/` contains the matching uploaded data, `data/backups/` retains
   historical snapshots, and `deployed/` holds the deployed course files.
5. Test recovery with outbound email and AI-provider calls disabled. Production
   restoration requires a separately authorized maintenance window; never copy
   a backup over a running database or invoke an import that overwrites live data.

`backup.json` records capture time, encryption settings, chunk checksums and the
local verification result. Account details and source file names stay encrypted.
No GitHub Actions or Render deployment workflow is added by these backups.
