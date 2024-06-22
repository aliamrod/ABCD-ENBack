# Match SRC_Subject_ID and concatenate to original "fmriresults01.csv" file. 

# Load required libraries
import pandas as pd 

# Define file paths
data1_path = '/Users/aliamahama-rodriguez/local/fmriresults01.csv'
data2_path = '/Users/aliamahama-rodriguez/local/mri_y_tfmr_nback_beh.csv'
output_file_path = '/Users/aliamahama-rodriguez/local/concatenated_files.csv'

# (1) Load provided data into dataframe
df1 = pd.read_csv(data1_path)
df2 = pd.read_csv(data2_path)

print(df1.head(10))
print(df2.head(10))

# Merge the datasets on the 'src_subject_id' column
merged_df = pd.merge(df1, df2, on='src_subject_id', how='inner')

# Save the merged data frame to a new .csv file
merged_df.to_csv(output_file_path, index=False)

print(f"Merged data is saved to {output_file_path}")

