

def read_str_prompt(filepath: str):

    with open(filepath, 'r') as file:
            template = file.read()

    return(template) 