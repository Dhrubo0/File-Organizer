import os   
from shutil import move

while True:
    try:
        # Takes the location of your Directory
        path = input(r"Enter the directory you want to organize: ")
        path = os.path.normpath(path)

        # Gives a list of all the files in the given Directory
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        break
    except FileNotFoundError:
        print(">> Error: The specified directory does not exist. Please check the path and try again. <<\n")
    except PermissionError:
        print(">> Error: Permission denied. Please check your permissions and try again. <<\n")
    except Exception as e:
        print(f">> Error: {e} <<\n")

# Makes the Directories according to the file type; Makes a 'No_Extension' Directory if a file with no extension exists
def make_dirs(dire):
    for file in dire:
        file_type = file.split('.')[-1] if '.' in file else 'No_Extension'
        full_path = os.path.join(path, file_type)
        if not os.path.exists(full_path):
            os.mkdir(full_path)

# Moves the files to their respective Directories
def move_files(files, path):
    for file in files:
        source_file = os.path.join(path, file)
        if '.' in file:     # Checks if the file has an extension type
            file_type = file.split('.')[-1]
            destination_dir = os.path.join(path, file_type)
            move(source_file, destination_dir)
            print(f'"{file}" moved to "{destination_dir}"')
        else:
            destination_dir = os.path.join(path, "No_Extension")
            move(source_file, destination_dir)
            print(f'"{file}" moved to "{destination_dir}"')

# Calls "make_dirs" & "move_files"
if __name__ == "__main__":
    make_dirs(files)
    move_files(files, path)