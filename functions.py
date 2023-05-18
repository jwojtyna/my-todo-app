FILEPATH = "todos.txt"


def get_todos():
    with open(FILEPATH, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


# default parameter below might be filepath="todos.txt" instead of filepath
def write_todos(todos_arg):
    with open(FILEPATH, 'w') as file_local:
        file_local.writelines(todos_arg)
        return True


if __name__ == "__main__":
    print(get_todos())
