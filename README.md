# TigoAi - CLI AI Assistant and Source Control

**Author**: Nwali Ugonna Emmanuel
**Country**: Nigeria  

### Chat with Tigo_bot on Telegram 
<a href="https://t.me/TigoGPTBot">@Tigo_bot</a>
<h4>Features</h4>

<ol>
<li>
Speech to Text Response
</li>
<li>
Real Time Chat and Response from Groq API
</li
</ol>

## Overview

TigoAi is a user-friendly command-line source control tool designed to simplify the management of your project's source code directly from your terminal. It streamlines version control workflows and allows for efficient code management with minimal commands.

By integrating AI into this tool, TigoAi significantly enhances functionality, making the command-line experience more intelligent, intuitive, and effective. AI's capabilities, such as analysis, prediction, and adaptation, empower developers to manage complex codebases and collaborate efficiently.

TigoAi handles a wide range of tasks, including committing, pushing, and staging changes. It also simplifies the creation of files, functions, classes, packages, and more. Additionally, developers can interact with AI to ask questions, debug files, and perform tasks seamlessly from the command line.

### Example of Usage:
```bash
tigo@Tigo:~$ TigoAi create a python file that will print out the Fibonacci series
Done!

tigo@Tigo:~$ ls
fib.py

tigo@Tigo:~$ cat fib.py
#!/usr/bin/python
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

if __name__ == "__main__":
    n = int(input("Enter the number of Fibonacci numbers to generate: "))
    fib_sequence = fibonacci(n)
    print("Fibonacci series:")
    for num in fib_sequence:
        print(num, end=" ")
    print()

tigo@Tigo:~$ sc -a fib.py -c -p
TigoAi: fib.py added to git
Press enter to suggest a commit
Commit: 
Msg: Added Fibonacci series generator script.
Successfully pushed.
``` 
### What the Project Will Not Solve

Graphical User Interface (GUI) Integration: This tool is focused only on command-line operations. It will not provide a graphical interface for users who prefer a visual approach to source control management.

Advanced Git Features: While the tool handles basic Git operations like committing, pushing, and staging changes, it may not cover more advanced Git features such as rebasing, cherry-picking, or complex merge conflict resolution etc.

Complex Workflow Automation: The tool is designed to handle basic tasks efficiently, but it may not be suitable for automating complex workflows or integrating with other tools and services outside of its primary scope. 

This tool is basically an CLI Developer assistant which would be designed to help and improve workflow.

Who the Project Will Help / Who the Users Will Be

The project targets developers, small development teams, open-source contributors Command-Line Enthusiasts, especially those who regularly use Python and favor or need command-line interfaces for source control.

### Is this Project Relevant or Dependent on a Specific Locale?

This project is not dependent on any specific locale. It will be designed to be globally relevant and can be used by developers anywhere in the world, provided they work in environments where command-line tools are common.

Technical Risks/impacts

The project might rely on third-party libraries or frameworks that may not be compatible with future versions of Python or may have conflicting dependencies and might need to be installed before use, failure to do so might result in program failure.

Users who find it usefully might need to install subsequent updates for possible changes to be made in the future for bug fixes and feedbacks.

Safeguards/Alternatives:

Ensure all required libraries are installed on the local machine from the requirements file that'll be provided.

Regularly update and test dependencies in a controlled environment by visiting the github repo to be notified on any changes made.

### Existing Solutions

Visual studio source control feature for advanced git workflow

Pycharm IDE source control feature and gitCopilot Ai

Reimplementation Of Proven Solution

TigoAi would integrate Ai for more functionalities and easy access to solution from command line. With one lined argument the user can get access to Ai from anywhere in the terminal

Imagine you just open the terminal and ask an Ai for any question, to perform some tasks just like SIRI on the IOS..
 





                                                                                                                                                                                                                                                                                                                                    