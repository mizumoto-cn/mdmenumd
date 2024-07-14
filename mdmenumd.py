import os
import argparse

def generate_file_list(root_dir, file_extension):
    file_tree = {}
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(file_extension):
                relative_path = os.path.relpath(os.path.join(root, file), root_dir)
                path_parts = relative_path.split(os.sep)
                current_level = file_tree
                for part in path_parts[:-1]:
                    current_level = current_level.setdefault(part, {})
                current_level[path_parts[-1]] = relative_path
    return file_tree

def write_md(file_tree, md_file, indent=0):
    for key, value in file_tree.items():
        if isinstance(value, dict):
            md_file.write('  ' * indent + f'- {key}\n')
            write_md(value, md_file, indent + 1)
        else:
            md_file.write('  ' * indent + f'- [{key}]({value})\n')

def create_md_file(root_dir, file_extension, md_filename='directory.md'):
    file_tree = generate_file_list(root_dir, file_extension)
    with open(os.path.join(root_dir, md_filename), 'w', encoding='utf-8') as md_file:
        md_file.write("# List of Files\n\n")
        write_md(file_tree, md_file)

def main():
    parser = argparse.ArgumentParser(description='Generate a markdown file listing all files with a specified extension in a directory and its subdirectories.')
    parser.add_argument('root_directory', help='The root directory to search for files')
    parser.add_argument('file_extension', help='The file extension to search for')
    parser.add_argument('--md_filename', default='directory.md', help='The name of the markdown file to generate (default: directory.md)')

    args = parser.parse_args()

    create_md_file(args.root_directory, args.file_extension, args.md_filename)

if __name__ == "__main__":
    main()
