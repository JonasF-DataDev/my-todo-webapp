FILEPATH = "todos.txt"



def get_todos(filepath = FILEPATH):
    """Read a text file and return the list of
    to-do items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def push_todos(todos_arg, filepath=FILEPATH):
    """ Write todos items list into textfile."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

# __name__ = de naam van je document.
# als je het document uitvoert vanuit zichzelf is __name__ altijd main, maar als ik functions.py uitvoer van in
# cli.py dan is de name uit dit document gelijk "aan functions"
if __name__ == "__main__":
    print("Hello from functions")