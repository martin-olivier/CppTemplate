#!/usr/bin/env python3

import os

class Color:
    RED   = '\033[91m'
    GREEN = '\033[92m'
    END   = '\033[0m'

def replace_content(file_path: str, search: str, replace: str):
    with open(file_path, 'r') as file :
        filedata = file.read()
    filedata = filedata.replace(search, replace)
    with open(file_path, 'w') as file:
        file.write(filedata)

if __name__ == "__main__":
    try:
        name = input("Enter the name of your binary:\n")
        if len(name) == 0:
            raise Exception("the name of your binary cannot be empty")
        name_upper = name.capitalize()
        replace_content("README.md", "binary", name)
        replace_content("README.md", "# CppTemplate", "# " + name_upper)
        replace_content("README.md", "\n- [Python3](https://www.python.org/download/releases/3.0/)", "")
        replace_content(".gitignore", "binary", name)
        replace_content("Makefile", "binary", name)
        replace_content("CMakeLists.txt", "binary", name)
        replace_content("CMakeLists.txt", "Template", name_upper)
        print(Color.GREEN + "Setup Done" + Color.END)
        os.remove("setup.py")
        exit(0)
    except Exception as e:
        print(Color.RED + "Exception raised : " + Color.END + str(e))
        exit(84)
