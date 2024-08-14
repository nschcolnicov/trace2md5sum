import os
import glob
import hashlib
import csv
import argparse

def md5sum(file_path):
    """Compute the MD5 checksum of a file."""
    hash_md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def get_files_from_directory(directory, depth):
    """Recursively get files from a directory up to a specified depth."""
    if depth < 0:
        raise ValueError("Depth must be a non-negative integer.")
    
    files = []
    for root, _, filenames in os.walk(directory):
        # Calculate current depth
        current_depth = root[len(directory):].count(os.sep)
        if current_depth > depth:
            continue
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files

def process_tsv(file_path, base_path, depth=0):
    """Process the TSV file and compute MD5 sums."""
    # Replace $USER with the actual username
    user = os.getenv('USER')
    if user:
        base_path = base_path.replace("$USER", user)
    else:
        raise EnvironmentError("The $USER environment variable is not set.")

    matches = []
    hash_count = {}  # Dictionary to track occurrences of each hash

    # Read the TSV file
    with open(file_path, 'r') as tsv_file:
        reader = csv.DictReader(tsv_file, delimiter='\t')
        for row in reader:
            hash_value = row['hash']
            search_path = os.path.join(base_path, hash_value)
            print(f"Searching for folders matching: {search_path}")

            # Find matching directories
            for folder in glob.glob(search_path + '*'):
                if os.path.isdir(folder):
                    print(f"Found matching folder: {folder}")
                    matches.append((folder, hash_value))
    
    # Process each matching folder
    for match_path, hash_value in matches:
        # Increment count for this hash
        hash_count[hash_value] = hash_count.get(hash_value, 0) + 1
        index = hash_count[hash_value]

        print(f"Processing folder: {match_path}")

        # Collect all files in the directory up to the specified depth
        files = get_files_from_directory(match_path, depth)
        
        # Use original hash value for naming, replace slashes with underscores
        hash_value_for_filename = hash_value.replace('/', '_')
        md5_file_path = f"{hash_value_for_filename}_{index}.md5sum"
        with open(md5_file_path, 'w') as md5_file:
            for file in files:
                file_md5 = md5sum(file)
                md5_file.write(f"{file_md5}  {file}\n")
        
        print(f"MD5 sums for files in {match_path} written to {md5_file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a TSV file and compute MD5 sums of files in matching folders.")
    parser.add_argument("tsv_file", help="Path to the TSV file")
    parser.add_argument("base_path", help="Base path for searching directories (no default)")
    parser.add_argument("--depth", type=int, default=0, help="Depth for directory traversal. Default is 0 (no recursion).")
    args = parser.parse_args()

    process_tsv(args.tsv_file, args.base_path, args.depth)
