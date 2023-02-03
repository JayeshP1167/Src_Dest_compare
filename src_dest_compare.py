import os

def path_exist(dir_path):
    """
    Check if path exists
    """
    return os.path.exists(dir_path)

def count_files(dir_path):
    """
    Return the no of files inside a dir_path
    """
    return len([f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))])


def file_path_size_extractor(dir_path):
    """
    Generate a map with file_name inside a dir along with it's size.
    """
    src_file_size = {}
    for path, dirs, files in os.walk(dir_path):
        for f in files:
            fp = os.path.join(path, f)
            src_file_size[f] = os.path.getsize(fp)

    return src_file_size

def src_dest_equal_validation(src_path: str, dest_path: str):
    # Both Source & Destination Path Exists
    if path_exist(src_path) and path_exist(dest_path):
        print(f'Validation - Both Locations {src_path} and {dest_path} exists.')
        # Validation - 1, No of Files in the src & dest path
        if count_files(src_path) == count_files(dest_path):
            print(f'Validation - Directory Size in both {src_path} and {dest_path} looks similar.')
            dest_file_size_dict = file_path_size_extractor(dest_path)
            src_file_size_dict = file_path_size_extractor(src_path)
            if  src_file_size_dict.keys() == dest_file_size_dict.keys():
                print(f'Validation - Same Files Present in Both the Locations')
                unmatched_files_by_size = []
                for file in src_file_size_dict.keys():
                    if src_file_size_dict.get(file) != src_file_size_dict.get(file):
                        unmatched_files_by_size.append(file)
                if unmatched_files_by_size:
                    print(f"Validation Error - File Size Mismatching for the files: {unmatched_files_by_size}")
                else:
                    print(f"Validation - Same Files with Equal Size Present in both the Locations")
                    return True
            else:
                print(f'Validation Error - Files Missing in the Destination: {src_file_size_dict.keys()-dest_file_size_dict.keys()}')
        else:
            print(f"Validation Error - Directory Size in both {src_path} and {dest_path} doesn't looks similar.")
    else:
        if not path_exist(src_path):
            print(f"Validation Error - {src_path}' doesn't exist")
        else:
            print(f"Validation Error - {dest_path} doesn't exist.")
    return False

# call the method with src_path & dir_path src_dest_equal_validation(src_path: str, dest_path: str)
# For Testing purpose I have passed the same path.
print(os.getcwd())
print(src_dest_equal_validation(os.getcwd(), os.getcwd()))