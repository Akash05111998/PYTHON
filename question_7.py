import os
import shutil


SMALL_SIZE_LIMIT = 1 * 1024 * 1024  # 1 MB
MIDDLE_SIZE_LIMIT = 100 * 1024 * 1024  # 100 MB


source_folder = "/path/to/your/source/folder"

small_size_folder = "/path/to/your/destination/small_size"
middle_size_folder = "/path/to/your/destination/middle_size"
large_size_folder = "/path/to/your/destination/large_size"


os.makedirs(small_size_folder, exist_ok=True)
os.makedirs(middle_size_folder, exist_ok=True)
os.makedirs(large_size_folder, exist_ok=True)


def segregate_files_by_size(source_folder):
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        
        
        if os.path.isdir(file_path):
            continue
        
        
        file_size = os.path.getsize(file_path)
        
        
        if file_size < SMALL_SIZE_LIMIT:
            destination_folder = small_size_folder
        elif file_size < MIDDLE_SIZE_LIMIT:
            destination_folder = middle_size_folder
        else:
            destination_folder = large_size_folder
        
        
        destination_file_path = os.path.join(destination_folder, filename)
        
        
        shutil.move(file_path, destination_file_path)
        print(f"Moved {filename} to {destination_folder}")


segregate_files_by_size(source_folder)
