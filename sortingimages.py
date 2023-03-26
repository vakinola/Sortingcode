import os
import shutil

location_path = os.getcwd()
files_in_folder = []
folders_to_create = []


def check_path(path: str) -> bool:
    # This function checks if the inputed value is valid or not

    return os.path.exists(path)


def pic_format_check(file_name: str) -> bool:
    # This checks if the files being sorted are not JPEG or JPG

    _, file_extension = os.path.splitext(file_name)
    if file_extension == ".jpeg":
        return True
    else:
        return False


def get_name(file: str) -> str:
    # This function gets the year from each file name
    title = file[:4]
    return title


def check_if_folder_exists(title: str) -> bool:
    # This function checks if the folders based on the file name already exist

    if title not in folders_to_create:
        folders_to_create.append(title)
        return True
    else:
        return False


def create_folder(title: str):
    # This function creates folders from file name if they do not exist

    title_year_of_file = get_name(title)
    print(title_year_of_file)

    if check_if_folder_exists(title_year_of_file):
        os.makedirs(title_year_of_file)
    else:
        pass


def move_file_to_folder(file_name, path):
    # This folder moves files into their respective folders based on the year in their name

    title_year_of_file = get_name(file_name
                                  )

    sourcePath = path+'/'+file_name

    destination = title_year_of_file
    destinationPath = path+'/'+destination
    print("This is the destination", destinationPath)

    # Move the content
    # source to destination
    shutil.move(sourcePath, destinationPath)

    print(file_name, 'has been moved!')


def get_files(path=location_path):
    # This function gets the path from the user input or uses the default path if none is given
    # and returns the files in the folder

    print(type(path))

    location_path = os.getcwd()

    individual_files_in_folder = os.listdir(location_path)

    for file in individual_files_in_folder:
        result_pic_format_check = pic_format_check(file)
        if result_pic_format_check:
            files_in_folder.append(file)
            create_folder(file)
            move_file_to_folder(file, path)
        else:
            pass


if __name__ == "__main__":
    path = input(
        "enter filepath to sort files or press enter to use default path: ")

    if path == "":
        get_files()

    elif len(path) >= 1:
        # uses the length of the inputed path to ensure it is not an empty string and verifies if it is a valid path

        # calls the verification function to check if the path is valid
        path_validation = check_path(path)

        if path_validation:
            print("Path checked and successfully validated")

            try:
                get_files(path)

            finally:

                print("Files successfully loaded from inputed path")

        else:

            print("The path entered is invalid, Please Enter a valid Path")
