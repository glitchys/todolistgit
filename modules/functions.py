FILEPATH = "todos.txt"

def get_todos(filepath = FILEPATH):
    """Returns a list of to-dos"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath = FILEPATH ):
    """Writes to-dos to a file"""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print('hello from functions')
