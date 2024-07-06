FILEPATH= "to-do list\todos.txt"


def get_todos(filepath= FILEPATH):
    """Read a text file and return the list of to-do items"""
    with open(r'to-do list\todos.txt','r') as file_local:
        todos_local=file_local.readlines()
    return todos_local    
    
def write_todos(todos_arg,filepath=FILEPATH):
    """Write the to-do items list in the text file"""
    with open(r'to-do list\todos.txt','w') as file:
        file.writelines(todos_arg)
