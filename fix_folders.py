import os

def replace_spaces_with_underscores(start_path):
    """
    Recursively walks through directories and replaces spaces with underscores in folder names
    """
    for root, dirs, files in os.walk(start_path, topdown=False):
        for dir_name in dirs:
            if ' ' in dir_name:
                old_path = os.path.join(root, dir_name)
                new_name = dir_name.replace(' ', '_')
                new_path = os.path.join(root, new_name)
                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed: {old_path} -> {new_path}")
                except OSError as e:
                    print(f"Error renaming {old_path}: {e}")

if __name__ == "__main__":
    # Set the starting directory - you can modify this path
    start_directory = "c:/Users/NateG/source/repo/Udemy/100-days-of-python-challenge"  # Current directory
    
    print(f"Starting folder rename process from: {os.path.abspath(start_directory)}")
    replace_spaces_with_underscores(start_directory)
    print("Folder rename process completed")
