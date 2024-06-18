import pandas as pd

# Load the CSV file
data = pd.read_csv("/Users/aliamahama-rodriguez/local/fmriresults01.csv", sep=',')
data.columns = data.columns.str.strip()  # Strip whitespace from column names

# Print the column names
print("Columns in the dataframe:", data.columns)

# Ensure 'subjectkey' column exists
if 'subjectkey' in data.columns:
    # Inspect some values in the 'subjectkey' column
    print("Sample 'subjectkey' values:\n", data['subjectkey'].head(20))
    
    # Check for duplicates in the 'subjectkey' column
    duplicates = data['subjectkey'].duplicated().sum()
    print(f"Number of duplicate 'subjectkey' values: {duplicates}")
    
    # Show duplicate 'subjectkey' values if any
    if duplicates > 0:
        duplicate_keys = data['subjectkey'][data['subjectkey'].duplicated(keep=False)]
        print(f"Duplicate 'subjectkey' values:\n{duplicate_keys}")
    
    # Check for presence of underscores in the 'subjectkey'
    contains_underscore = data['subjectkey'].str.contains('_', na=False).sum()
    print(f"Number of 'subjectkey' values containing underscores: {contains_underscore}")
    
    # Check for 'subjectkey' length
    subjectkey_lengths = data['subjectkey'].str.len().value_counts()
    print(f"Distribution of 'subjectkey' lengths:\n{subjectkey_lengths}")
    
    # 01. Filter the rows where 'subjectkey' do not contain underscores
    filtered_data_no_underscore = data[~data['subjectkey'].str.contains('_', na=False)]
    print("Data without underscores in 'subjectkey':\n", filtered_data_no_underscore)
    
    # 02. Filter rows where 'subjectkey' has less than 16 characters
    filtered_data_less_than_16_chars = data[data['subjectkey'].str.len() < 16]
    print("Data with 'subjectkey' less than 16 characters:\n", filtered_data_less_than_16_chars)

    # 03. Combine both filters to derive the final data frame
    filtered_data = pd.concat([filtered_data_no_underscore, filtered_data_less_than_16_chars]).drop_duplicates()
    print("Combined filtered data:\n", filtered_data)

    # Extract the 'subjectkey' values from the filtered data
    subjectkeys_to_inspect = filtered_data['subjectkey']

    # Write the 'subjectkey' values to a new .txt file
    with open('subjectkeys_to_inspect.txt', 'w') as f:
        for subjectkey in subjectkeys_to_inspect:
            f.write(f"{subjectkey}\n")
else:
    print("The 'subjectkey' column is not found in the data.")

# Returns empty Data Frame for all conditions, so all subjectkeys pass required conditions. 

# Sort all subjectkeys into respect files. 
