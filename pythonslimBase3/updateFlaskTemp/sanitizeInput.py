import re

def sanitize(input):
    patterns = [(r'&',r'\\&'),(r'>',r'\\>'),(r'<',r'\\<'),(r'!',r'\\!'),(r';',r'\\;'),(r'#',r'\\#'),(r'-',r'\\-'),(r'\n',' '),(r'\b',''),(r'"',r'\"'),(r"'",r"\'"),(r"\$",r"\\$")]
    einput = input
    for match,sub in patterns:
        einput = re.sub(match,sub,einput)
    return einput

def unsanitize(input):
    patterns = [(r'&',r'\\&'),(r'>',r'\\>'),(r'<',r'\\<'),(r'!',r'\\!'),(r';',r'\\;'),(r'#',r'\\#'),(r'-',r'\\-'),(r'\n',' '),(r'\b',''),(r'"',r'\"'),(r"'",r"\'"),(r"\$",r"\\$")]
    einput = input
    for sub,match in patterns:
        einput = re.sub(match,sub,einput)
    return einput



