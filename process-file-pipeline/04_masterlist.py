# Master List Generation
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

# Open "mri_y_qc_incl.csv" and inspect metadata 
df = pd.read_csv(mri_y_qc_incl)

# Display the first few rows of the dataframe to understand content
print("First few rows of dataframe: ")
print(df.head())

# Display information about the dataframe
print("\nMetadata of dataframe: ")
print(df.info())
print(df.columns)

# Extract rows where imgincl_nback_include column reports value of "1"
passed_subjects = df[df['imgincl_nback_include'] == 1]
master_list = passed_subjects[['src_subject_id']]

# Save the master list to a new CSV file
output_file = '/Users/aliamahama-rodriguez/local/master_list.csv'
master_list.to_csv(output_file, index=False)

print(f"Master list generated with {len(master_list)} subjects. The result has been saved to {output_file}")

# aliamahama-rodriguez@Alias-MBP local % python3 04_masterlist.py
# First few rows of dataframe: 
#     src_subject_id                 eventname  imgincl_t1w_include  imgincl_t2w_include  ...  imgincl_rsfmri_include  imgincl_mid_include  imgincl_nback_include  imgincl_sst_include
#0  NDAR_INV003RTV85     baseline_year_1_arm_1                    1                    1  ...                       1                    1                      1                    1
#1  NDAR_INV005V6D2C     baseline_year_1_arm_1                    1                    1  ...                       0                    1                      0                    0
#2  NDAR_INV007W6H7B     baseline_year_1_arm_1                    1                    1  ...                       1                    1                      1                    1
#3  NDAR_INV00BD7VDC     baseline_year_1_arm_1                    1                    1  ...                       1                    1                      1                    1
#4  NDAR_INV00CY2MDM  2_year_follow_up_y_arm_1                    1                    1  ...                       1                    1                      1                    1

#[5 rows x 9 columns]

#Metadata of dataframe: 
#<class 'pandas.core.frame.DataFrame'>
#RangeIndex: 19649 entries, 0 to 19648
#Data columns (total 9 columns):
# #   Column                  Non-Null Count  Dtype 
#---  ------                  --------------  ----- 
# 0   src_subject_id          19649 non-null  object
# 1   eventname               19649 non-null  object
# 2   imgincl_t1w_include     19649 non-null  int64 
# 3   imgincl_t2w_include     19649 non-null  int64 
# 4   imgincl_dmri_include    19649 non-null  int64 
# 5   imgincl_rsfmri_include  19649 non-null  int64 
# 6   imgincl_mid_include     19649 non-null  int64 
# 7   imgincl_nback_include   19649 non-null  int64 
# 8   imgincl_sst_include     19649 non-null  int64 
# dtypes: int64(7), object(2)
# memory usage: 1.3+ MB
# None
# Index(['src_subject_id', 'eventname', 'imgincl_t1w_include',
#       'imgincl_t2w_include', 'imgincl_dmri_include', 'imgincl_rsfmri_include',
#       'imgincl_mid_include', 'imgincl_nback_include', 'imgincl_sst_include'],
#      dtype='object')
#Master list generated with 14110 subjects. The result has been saved to /Users/aliamahama-rodriguez/local/master_list.csv

