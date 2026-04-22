import os, hashlib, json
from pathlib import Path
import sys
import argparse

RAW = Path('data/raw')
RAW.mkdir(parents = True, exist_ok = True)

def hash_files(path):
    h = hashlib.sha256()
    with open(path, 'rb') as file:
        for chunk in iter(lambda: file.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()

def save_manifest(manifest, path = 'data/raw/manifest.json'):
    with open(path, 'w') as file:
        json.dump(manifest, file, indent = 2)

def ingest_md(local_path: str, dest_name: str = None):
    src = Path(local_path)
    if not src.exists():
        raise FileNotFoundError(local_path)
    
    dest = RAW / (dest_name or src.name)
    
    with open(src, 'r', encoding='utf-8') as f:
        content = f.read()
    
    with open(dest, 'w', encoding='utf-8') as f:
        f.write(content)
        
    h = hash_files(dest)
    
    manifest = {
        'file': str(dest),
        'lines': len(content.splitlines()),
        'characters': len(content),
        'sha256': h
    }
    
    save_manifest(manifest)
    print('Ingested', manifest)
    return manifest
    
def parse_args(argv):
    p = argparse.ArgumentParser(description = "ingest markdown dataset")
    p.add_argument("--source_data", type = str, default = 'data/source/politicas.md', help = "Path to read the source data")
    return p.parse_args(argv)
    
def main(argv=None):
    args = parse_args(argv or sys.argv[1:])
    manifest = ingest_md(args.source_data)
    print('Done')
    
if __name__ == '__main__':
    main()
