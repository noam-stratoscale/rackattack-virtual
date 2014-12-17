import re


def replaceRegexInFile(filename, original, modified):
    with open(filename, 'r') as f:
        contents = f.read()
    contents = re.sub(original, modified, contents)
    with open(filename, 'w') as f:
        f.write(contents)
