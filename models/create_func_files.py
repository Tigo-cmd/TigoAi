"""this module handles creation of python files especially for up and coming alx students>>>
    creates files append function if needed

####################################################################################################################
Copyright (c) 2024 Emmanuel Tigo, All Rights Reserved
Originally By Nwali Ugonna Emmanuel (Emmanuel Tigo)
###################################################################################################################
    """
import os
import subprocess


# import sys


def is_exists(filename="", content=[]):
    if content is None:
        content = []
    if os.path.exists(filename):
        """checks if file exists in the current directory and overwrites when prompted"""
        overwrite = input(f"{filename} already exists Overwrite?(Y/N): ").lower()
        if 'y' in overwrite:
            prototype = input(f"prototype for {filename}: ")
            content.append(f"{prototype}\n")
            with open(filename, 'w', encoding='utf-8') as f:
                # creates file and writes contents to each line of the file
                f.writelines(content)
            os.chmod(filename, 0o764)
        elif 'n' in overwrite:
            pass
        else:
            print("invalid input")
    else:
        prototype = input(f"prototype for {filename}: ")
        content.append(f"{prototype}\n")
        with open(filename, 'w', encoding='utf-8') as f:
            # creates file and writes contents to each line of the file
            f.writelines(content)
        os.chmod(filename, 0o764)


def source_code_create(filename="", prototype=""):
    """handles creating python functions files
     and setting necessary permissions
        Args:
            filename: name of file to be created, must be a c or python file extension else it creates an empty file
            prototype: this is the alx provided function eg: def create_file(filename=""):
            """
    if filename[-2:] == ".c":
        create_cfile(filename)
    elif filename[-3:] == ".py":
        create_pyfile(filename)
    else:
        if '.' not in filename:  # checks if the file is a sourcecode file else creates an empty file
            with open(filename, 'w', encoding='utf-8') as file:
                pass
            print("created an empty file")


def create_header_files(filename=""):
    """function for creating c header files and appending c prototypes to the file"""
    header = ""
    if os.path.exists(filename):
        pass
    else:
        header = filename
        content = [f"ifndef {header}\ndefine {header}\n", "#include <stdio.h>", "\n"]
        with open(header, 'w', encoding='utf-8') as file:
            file.writelines(content)
    return header


def create_c_main_files(filename=""):
    """creates C main files
    Args:
        filename: file to be created must be a c extension
    """
    content = [f"#include \"{header}\"\n", f"/**\n*{filename}-\n"
                                             f"* @param\n* @param\n* Description:"
                                             f" \n* Return: Always(0) success\n*/\n",
               "int main()\n{\n\tprintf(\"Welcome\")\n\n}"]
    if os.path.exists(filename):
        """checks if the fil exists in the current dir"""
        overwrite = input(f"{filename} already exists Overwrite?(Y/N): ").lower()
        if 'y' in overwrite:
            with open(filename, 'w', encoding='utf-8') as file:
                file.writelines(content)
        elif 'n' in overwrite:
            pass
        else:
            print("invalid input")
            pass
    else:
        with open(filename, 'w', encoding='utf-8') as file:
            file.writelines(content)


def create_py_main_files(filename=""):
    """handles the creation of python main files"""

    content = ["#!/usr/bin/python3\n", '"""module documentation"""\n\n', "if __name__ == '__main__':"
                                                                         "    "]
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(content)
    os.chmod(filename, 0o764)


def create_cfile(filename="", prototype=""):
    """function for creating c function files"""
    header = "main.h"
    if os.path.exists(header):
        pass
    else:
        header = ""
    content = [f"#include \"{header}\"\n", f"/**\n*{filename}-\n"
                                             f"* @param\n* @param\n* Description:"
                                             f" \n* Return: Always(0) success\n*/\n", f"{prototype}\n",
               #  contents to write to the file
               "{\n}" if prototype != "" else ""]
    is_exists(filename, content) # class the function and creates
    update_header_file(prototype)


def create_pyfile(filename=""):
    """function for creating python function files"""

    content = ["#!/usr/bin/python3\n", '"""module documentation"""\n\n']
    is_exists(filename, content)  # class the function and creates


def update_header_file(prototype, filename):
    # Read the contents of main.h except for the last line
    header = "main.h"
    if os.path.exists(header):
        pass
    else:
        header = filename
    with open(header, 'r') as file:
        lines = file.readlines()[:-1]

    # Append the new function prototype and #endif
    lines.append(prototype + '\n')
    lines.append("#endif\n")

    # Write the updated contents back to main.h
    with open(header, 'w') as file:
        file.writelines(lines)


def file_create(filename=""):
    """creates normal python file users adds codes to taste
        Args:
            filename: file to be creates by function
            if file extension is invalid the program will yell out
            """
    if filename[-3:] == '.py':
        create_py_main_files(filename)
    elif filename[-2:] == ".c":
        create_c_main_files(filename)
    elif filename[-2:] == ".h":
        create_header_files(filename)
    else:
        with open(filename, 'w', encoding='utf-8') as file:
            pass
        print("created an empty file")


def test_prototype(filename=""):
    """this creates a test file prototype with common startup lines"""
    content = ["#!/usr/bin/python3\n", '"""module documentation"""',
               "import unittest\n\n", f"class Test_{filename}(unittest.Testcase):"
                                      f"    def setup():\n", "if __name__ == '__main__':"
                                                             "    unittest.main()"]
    if "test" in filename:
        if os.path.exists(filename):
            overwrite = input(f"{filename} already exists Overwrite?(Y/N): ").lower()
            if 'y' in overwrite:
                with open(filename, 'w', encoding='utf-8') as file:
                    file.writelines(content)
                os.chmod(filename, 0o764)
            elif 'n' in overwrite:
                pass
            else:
                print("invalid input")
                pass
        with open(filename, 'w', encoding='utf-8') as file:
            file.writelines(content)
        os.chmod(filename, 0o764)


def delete_files(filename=""):
    """handles the deletion of files """
    if os.path.exists(filename):
        subprocess.run(["rm", "-rfi", f"{filename}"])