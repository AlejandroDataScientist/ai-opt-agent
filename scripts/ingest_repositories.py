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

def save_manifest(manifest, path = 'data/raw/manifest_scripts.json'):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(manifest, file, indent = 2)

def ingest_scripts(source_folder: str):
    src_dir = Path(source_folder)
    if not src_dir.exists() or not src_dir.is_dir():
        raise FileNotFoundError(f"No se encontró la carpeta: {source_folder}")
    scripts = list(src_dir.glob('*.py'))
    
    if not scripts:
        print("No se encontraron archivos .py")
        return None

    full_manifest = []

    for script_path in scripts:
    
        dest = RAW / script_path.name

        with open(script_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        with open(dest, 'w', encoding='utf-8') as f:
            f.write(content)
            
        h = hash_files(dest)
        
        file_info = {
            'file_name': script_path.name,
            'path': str(dest),
            'lines': len(content.splitlines()),
            'sha256': h
        }
        full_manifest.append(file_info)
        print(f'Ingested: {script_path.name} | Hash: {h[:10]}...')

    save_manifest(full_manifest)
    return full_manifest
    
def parse_args(argv):
    p = argparse.ArgumentParser(description = "Ingesta de scripts de Python")
    
    p.add_argument("--source_folder", type = str, default = 'data/source/', help = "Carpeta con los archivos .py")
    return p.parse_args(argv)
    
def main(argv=None):
    args = parse_args(argv or sys.argv[1:])
    manifest = ingest_scripts(args.source_folder)
    print('Done')
    
if __name__ == '__main__':
    main()
