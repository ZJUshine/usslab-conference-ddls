import os
import yaml

def find_yaml_files(directory):
    """Recursively find all .yml files in the directory."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.yml'):
                yield os.path.join(root, file)

def concatenate_yaml_files(directory):
    """Concatenate the contents of all .yml files into a single string."""
    all_content = []
    for yaml_file in find_yaml_files(directory):
        with open(yaml_file, 'r', encoding='utf-8') as file:  # Specify UTF-8 encoding here
            content = file.read()
            all_content.append(content)
    return '\n'.join(all_content)

def main():
    directory = './'  # Replace with your directory path
    all_yaml_content = concatenate_yaml_files(directory)

    with open('allconf.yml', 'w') as outfile:
        outfile.write(all_yaml_content)

if __name__ == '__main__':
    main()