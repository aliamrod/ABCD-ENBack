# Script handles reading a text file, splitting lines by delimiter, creating a data frame, processing 
# ... data and saving it to a CSV file.

# Read in text file.
import pandas as pd

def convert_txt_to_csv(txt_file_path, csv_file_path):
    try:
        # Open and read the text file
        with open(txt_file_path, 'r') as file:
            lines = file.readlines()
        
        # Check if file is empty
        if not lines:
            print("The file is empty.")
            return
        
        # Extract headers and data
        headers = lines[0].strip().split('\t')
        data = [line.strip().split('\t') for line in lines[2:]]  # Skip the second row with descriptions
        
        # Remove quotes from headers
        headers = [header.strip('"') for header in headers]
        
        # Remove quotes from data
        data = [[value.strip('"') for value in row] for row in data]
        
        # Check if headers and data are present
        if not headers or not data:
            print("No columns to parse from file.")
            return

        # Create DataFrame
        df = pd.DataFrame(data, columns=headers)
        
        # Display the first few rows of the DataFrame
        print("First few rows of the DataFrame:")
        print(df.head())
        
        # Convert date columns to datetime objects
        df['interview_date'] = pd.to_datetime(df['interview_date'], errors='coerce')
        
        # Fill missing values or perform other cleaning steps
        df.fillna('', inplace=True)
        
        # Write the DataFrame to a CSV file
        df.to_csv(csv_file_path, index=False)
        
        print(f'Data has been successfully written to {csv_file_path}')
    except Exception as e:
        print(f'An error occurred: {e}')

# Define file paths
txt_file_path = "/Users/aliamahama-rodriguez/local/fmriresults01.txt"
csv_file_path = "/Users/aliamahama-rodriguez/local/fmri_results.csv"

# Convert the text file to CSV
convert_txt_to_csv(txt_file_path, csv_file_path)
