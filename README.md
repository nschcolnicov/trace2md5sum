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

