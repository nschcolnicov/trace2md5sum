# trace2md5sum

This repository contains a Python script for processing nextflow trace TSV files to compute MD5 checksums of files located in directories matching specified hash values. It supports recursive file searching up to a specified depth and generates output files with MD5 checksums for all files found.

## Usage

### Script Overview

The script performs the following tasks:
1. Reads a nextflow trace TSV file containing task information. 
2. Constructs search paths based on hash values from the TSV file.
3. Searches for directories matching these paths.
4. Computes MD5 checksums for all files within these directories up to a specified depth.
5. Outputs MD5 checksums to files named according to the hash values.

**Note: Nextflow trace files end with "_trace.txt" even though they are TSV files

### Running the Script

```bash
python md5sum_calculator.py <path_to_your_trace_file.txt> <base_path> --depth 0
```

#### Arguments

## Arguments

1. **`tsv_file`** (str, required):
   - Path to the nextflow trace.txt TSV file containing the hash values to search for.
   - This is a mandatory positional argument.

2. **`base_path`** (str, required):
   - Base path where the script will search for directories matching the hash values.
   - This is a mandatory positional argument with no default value.

3. **`--depth`** (int, optional, default=0):
   - Specifies the depth for directory traversal.
   - Default is 0, meaning the script will not recurse into subdirectories beyond the matched folder.


#### Example

If you have a nextflow trace TSV file `test_trace.txt` and want to search directories up to a depth of 2, you can run:

```bash
python md5sum_calculator.py test_trace.tx /home/test/nextflow_workdirs/ --depth 2
```
This will search for directories matching the hash values in test_trace.tx, compute MD5 checksums for all files within these directories, and write the results to files named with the hash values.


# MD5 Checksum Comparison Script: md5sums_compare.py

This Python script compares MD5 checksum files between two folders to determine if the files with the same names and processes have identical checksums. The results are merged into a single CSV file, with columns indicating whether the checksums are identical or not.

## Usage

To use this script, you need to provide the paths to the two folders containing the `.md5sum` files you want to compare. The script will process these folders, merge the data, and output the results to a CSV file.

### Arguments

The script requires two positional arguments:

1. **folder1_path**: The path to the first folder containing `.md5sum` files.
2. **folder2_path**: The path to the second folder containing `.md5sum` files.

### Example Command

```bash
python compare_md5.py /path/to/folder1 /path/to/folder2
```

### Expected Output

The script generates a CSV file named `results.csv` in the same directory where the script is executed. This CSV file contains the following columns:

- `hash_folder1`: The MD5 checksum from files in the first folder.
- `filepath_folder1`: The file paths from the first folder.
- `process_folder1`: The process information from the first folder.
- `filename_folder1`: The extracted filenames from the first folder.
- `source_folder1`: The source folder name (folder1).

- `hash_folder2`: The MD5 checksum from files in the second folder.
- `filepath_folder2`: The file paths from the second folder.
- `process_folder2`: The process information from the second folder.
- `filename_folder2`: The extracted filenames from the second folder.
- `source_folder2`: The source folder name (folder2).

- `check`: A column indicating whether the checksums are 'Identical' or 'Non-identical'.
