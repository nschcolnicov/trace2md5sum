import pandas as pd
import argparse

def main(file1, file2):
    # Read TSV files into pandas DataFrames
    df1 = pd.read_csv(file1, sep="\t")
    df2 = pd.read_csv(file2, sep="\t")

    # Get unique values from the "name" column
    names1 = set(df1['name'].unique())
    names2 = set(df2['name'].unique())

    # Find differences
    only_in_file1 = names1 - names2
    only_in_file2 = names2 - names1

    # Print results
    print("Values in file1 but not in file2:")
    for value in only_in_file1:
        print(value)

    print("\nValues in file2 but not in file1:")
    for value in only_in_file2:
        print(value)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compare unique values in the 'name' column between two TSV files.")
    parser.add_argument("file1", help="Path to the first TSV file")
    parser.add_argument("file2", help="Path to the second TSV file")
    args = parser.parse_args()

    main(args.file1, args.file2)
