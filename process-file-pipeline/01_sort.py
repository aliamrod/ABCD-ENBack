import os
import shutil
import tarfile

# Directory containing .tgz files
directory = './abcd-mproc-release5'
output_directory = './sorted_abcd-mproc'

# Ensure the output directory exists, create if not
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Function to extract .tgz file and organize by participant ID
def extract_and_organize(filename, output_dir):
    try:
        # Extract participant ID from filename
        participant_id = filename.split('_')[0]

        # Create directory for participant if not exists
        participant_dir = os.path.join(output_dir, participant_id)
        if not os.path.exists(participant_dir):
            os.makedirs(participant_dir)
        
        # Extract .tgz file to participant directory 
        with tarfile.open(filename, 'r:gz') as tar: #argument specifies that we are opening file `filename` in read mode ('r') and that it is a gzip-compressed file ('gz')
            tar.extractall(path=participant_dir)
    except tarfile.ReadError:
        with tarfile.open(filename, 'r') as tar:
            tar.extractall(path=participant_dir)
    
        print(f"Extracted {filename} to {participant_dir}")
    except Exception as e:
        print(f"Failed to process {filename}: {str(e)}")
        return False

# List to keep track of processed files
processed_files = []

# Iterate over each file in the directory
for file in os.listdir(directory):
    if file.endswith('.tgz'):
        file_path = os.path.join(directory, file)
        extract_and_organize(file_path, output_directory)

print("Extraction and organization has been completed.")

# Check if all original files have been processed
original_files = [f for f in os.listdir(directory) if f.endswith('.tgz')]

if len(processed_files) != len(original_files):
    # Find unprocessed files
    unprocessed_files = set(original_files) - set(processed_files)
    
    # Write unprocessed files to a text file
    with open('unsorted_files.txt', 'w') as f:
        f.write("Files that have not been sorted:\n")
        for file in unprocessed_files:
            f.write(f"{file}\n")

    print(f"There are {len(unprocessed_files)} files that have not been sorted. "
          f"Check 'remaining_unsorted_files.txt' for details.")
else:
    print("All original files have been successfully sorted and processed.")
