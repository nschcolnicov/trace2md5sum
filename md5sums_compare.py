import os
import pandas as pd
import argparse

def process_folder(folder_name):
    # Initialize an empty list to store dataframes
    dataframes = []
    
    # Iterate over each file in the folder
    for filename in os.listdir(folder_name):
        if filename.endswith(".md5sum"):
            file_path = os.path.join(folder_name, filename)
            # Load the file into a dataframe
            df = pd.read_csv(file_path, sep='\s+', header=None, names=['hash', 'filepath', 'process'])
            # Extract the filename from the filepath
            df['filename'] = df['filepath'].apply(lambda x: os.path.basename(x))
            # Add the folder name as a new column
            df['source'] = folder_name
            # Append the dataframe to the list
            dataframes.append(df)
    
    # Concatenate all dataframes from this folder into one
    return pd.concat(dataframes, ignore_index=True)

def main(folder1_path, folder2_path):
    # Process both folders
    folder1_df = process_folder(folder1_path)
    folder2_df = process_folder(folder2_path)

    # Merge the dataframes on 'filename' and 'process', suffixes to differentiate columns with the same name
    merged_df = pd.merge(folder1_df, folder2_df, on=['filename', 'process'], suffixes=('_folder1', '_folder2'), how='outer')

    # Compare the hash columns to check if they are identical
    merged_df['check'] = merged_df.apply(lambda row: 'Identical' if row['hash_folder1'] == row['hash_folder2'] else 'Non-identical', axis=1)

    # Save the final dataframe to a CSV file if needed
    merged_df.to_csv('merged_results.csv', index=False)

    # Save the final dataframe to a CSV file
    merged_df.to_csv('results.csv', index=False)

    # Display the merged dataframe
    print(merged_df)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Compare MD5 checksum files between two folders.')
    parser.add_argument('folder1_path', type=str, help='Path to the folder1 folder containing .md5sum files')
    parser.add_argument('folder2_path', type=str, help='Path to the folder2 folder containing .md5sum files')

    args = parser.parse_args()
    
    main(args.folder1_path, args.folder2_path)
