import os
import shutil

from config import FILE_TYPES


def organize(folder_path):
    
    for item in os.listdir(folder_path):

        # Create the full path to the item
        source_path = os.path.join(folder_path, item)

        # Skip folders
        if not os.path.isfile(source_path):
            continue

        # Get the file extension
        _, extension = os.path.splitext(item)
        extension = extension.lower()

        # Default folder if no match is found
        destination_folder = "Others"

        # Find the correct category
        for folder, extensions in FILE_TYPES.items():
            if extension in extensions:
                destination_folder = folder
                break

        # Create the destination folder path
        destination_path = os.path.join(folder_path, destination_folder)

        # Create the folder if it doesn't exist
        os.makedirs(destination_path, exist_ok=True)

        # Move the file
        shutil.move(
            source_path,
            os.path.join(destination_path, item)
        )

        print(f"Moved '{item}' → '{destination_folder}'")