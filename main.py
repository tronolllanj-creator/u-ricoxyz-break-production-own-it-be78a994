# A simple script that writes a specific melancholic quote to entry.txt in the output directory.

import os

TEXT = 'I broke your trust like cheap glass, and now you’re bleeding trying to pick up the pieces.'

def main():
    output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, 'entry.txt')
    
# Gate allows 1-200 characters; file must contain only the entry plus a trailing newline.
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(TEXT + '\n')

if __name__ == '__main__':
    main()
