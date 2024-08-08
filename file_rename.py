import os

# Specify the folder path
folder_path = 'images\\Opportunities\\GTa'

# List all files in the folder
files = os.listdir(folder_path)

# Sort the files (optional, if you want them in a specific order)
files.sort()

# Rename each file
for index, file_name in enumerate(files, start=1):
    # Get the file extension
    file_extension = os.path.splitext(file_name)[1]

    # Create the new file name
    new_name = f"{index}{file_extension}"

    # Construct full file paths
    old_file_path = os.path.join(folder_path, file_name)
    new_file_path = os.path.join(folder_path, new_name)

    # Rename the file
    os.rename(old_file_path, new_file_path)

print("Files have been renamed.")
