# Content Packs

Latest EM (Engineering Mechanics I) and Maths content pack bundles.

| Subject | Version | Bundle |
| --- | --- | --- |
| EM | 1-9-12-distinct-transfer-problems | [telemetry-mechanics-i-1-9-12-distinct-transfer-problems.lfpack](EM/telemetry-mechanics-i-1-9-12-distinct-transfer-problems.lfpack) |
| Maths | 1-9-3 | [mathematik-bayern-nt1-privat-v1-9-3.lfpack](Maths/mathematik-bayern-nt1-privat-v1-9-3.lfpack) |

## Download

The `.lfpack` bundles are stored using Git LFS. Install Git LFS, then clone:

```sh
git lfs install
git clone https://github.com/daniellubovics-ux/Content-Packs.git
cd Content-Packs
git lfs pull
```

Import the downloaded `.lfpack` bundle using the application's content pack importer.

`catalog.json` records pack IDs, versions, file sizes, and SHA-256 checksums.
`SHA256SUMS` provides the checksums in standard checksum-file format.

Both bundles were copied byte-for-byte from the latest local releases. ZIP integrity, embedded pack metadata, and declared asset presence were checked before upload.

## Database recovery

[Encrypted Telemetry backups](backups/README.md) preserve database accounts,
progress, uploaded files and historical snapshots. Recovery requires the
owner's separately stored passphrase. These backups do not deploy the application.
