# (1) Load provided data into dataframe
# Match SRC_Subject_ID and concatenate to original "fmriresults01.csv" file. 

# Load required libraries
import pandas as pd 
import os

# Define file paths
mri_y_qc_auto_post = '/Users/aliamahama-rodriguez/local/mri_y_qc_auto_post.csv'
mri_y_qc_incl = '/Users/aliamahama-rodriguez/local/mri_y_qc_incl.csv'
mri_y_qc_man_post_fmr = '/Users/aliamahama-rodriguez/local/mri_y_qc_man_post_fmr.csv'
mri_y_qc_man_post_t2w = '/Users/aliamahama-rodriguez/local/mri_y_qc_man_post_t2w.csv'
mri_y_qc_motion = '/Users/aliamahama-rodriguez/local/mri_y_qc_motion'
mri_y_qc_raw_tfmr_nback = '/Users/aliamahama-rodriguez/local/mri_y_qc_raw_tfmr_nback'
mri_y_tfmr_nback_beh = '/Users/aliamahama-rodriguez/local/mri_y_tfmr_nback_beh.csv'
mri_y_adm_info = '/Users/aliamahama-rodriguez/local/mri_y_adm_info.csv'
fmriresults01 = '/Users/aliamahama-rodriguez/local/fmriresults01.csv'

output_file_path = '/Users/aliamahama-rodriguez/local/metadata.csv'

def count_rows_in_csv(csv_file):
    # Read the CSV file into a pandas datafrmae
    try:
        df = pd.read_csv(csv_file)
        # Count the number of rows in the DataFrame
        num_rows = len(df)
        # Print the number of rows
        print(f"Number of rows in {csv_file}: {num_rows}")
    except FileNotFoundError:
        print(f"Error: File {csv_file} not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: File {csv_file} is empty.")

# List of CSV files to process
csv_files = [
    '/Users/aliamahama-rodriguez/local/mri_y_qc_auto_post.csv',
    '/Users/aliamahama-rodriguez/local/mri_y_qc_incl.csv',
    '/Users/aliamahama-rodriguez/local/mri_y_qc_man_post_fmr.csv',
    '/Users/aliamahama-rodriguez/local/mri_y_qc_man_post_t2w.csv',
    '/Users/aliamahama-rodriguez/local/mri_y_qc_motion.csv',
    '/Users/aliamahama-rodriguez/local/mri_y_qc_raw_tfmr_nback.csv',
    '/Users/aliamahama-rodriguez/local/mri_y_tfmr_nback_beh.csv',
    '/Users/aliamahama-rodriguez/local/mri_y_adm_info.csv',
    '/Users/aliamahama-rodriguez/local/fmriresults01.csv'
]

# Process each CSV file
for file in csv_files:
    count_rows_in_csv(file)

# Merge the datasets on the 'src_subject_id' column
merged_df = pd.merge(df1, df2, on='src_subject_id', how='inner')

# Save the merged data frame to a new .csv file
merged_df.to_csv(output_file_path, index=False)

print(f"Merged data is saved to {output_file_path}")

