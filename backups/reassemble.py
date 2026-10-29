"""Verify and reassemble encrypted backup chunks; never decrypt inside Git."""
import argparse
import hashlib
import json
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('backup', type=Path, help='Directory containing backup.json')
parser.add_argument('output', type=Path, help='New encrypted .gpg file outside this repository')
args = parser.parse_args()
repository = Path(__file__).resolve().parent.parent
output = args.output.resolve()
if output.is_relative_to(repository):
    parser.error('Choose an output outside this repository to keep recovery files separate.')
metadata = json.loads((args.backup / 'backup.json').read_text(encoding='utf-8'))
whole = hashlib.sha256()
total = 0
with output.open('xb') as dst:
    for part in metadata['parts']:
        name = part['name']
        if Path(name).name != name:
            raise ValueError('Invalid chunk name')
        h = hashlib.sha256()
        size = 0
        with (args.backup / name).open('rb') as src:
            for block in iter(lambda: src.read(1024 * 1024), b''):
                h.update(block)
                whole.update(block)
                dst.write(block)
                size += len(block)
        if size != part['bytes'] or h.hexdigest() != part['sha256']:
            raise ValueError('Chunk verification failed: ' + name + '. Do not decrypt the incomplete output.')
        total += size
if total != metadata['encrypted_bytes'] or whole.hexdigest() != metadata['encrypted_sha256']:
    raise ValueError('Complete archive verification failed. Do not decrypt the output.')
print('Verified encrypted archive:', output)
