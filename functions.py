import glob

FILENAME = "todos.txt"


def get_todos(filename=FILENAME):
    """ Read and returns the content of the file
        specified as parameter as list
    """
    with open(filename, "r") as file:
        todo_list = file.readlines()
    return todo_list


def write_todos(todos_arg, filename=FILENAME):
    """ Write the content of the list passed into a file"""
    with open(filename, "w") as file:
        file.writelines(todos_arg)


def get_local_files(filter_files):
    return glob.glob(filter_files)


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


if __name__ == "__main__":
    print(get_local_files("*.txt"))
