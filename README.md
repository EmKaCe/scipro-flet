# scipro-flet
**Scientific Programming with Python: Assignment Peer Feedback/Grading Template**

**Authors: Karl Kirschner, Ph.D. and Emre Çetin based on the [original work](https://github.com/karlkirschner/scipro_assignments_grading) by Minh Truong, Erik Autenrieth, Abanoub Abdelmalak and Karl N. Kirschner, Ph.D.**

A simple application for peer reviewing the assignments of the students in the course "Scientific Programming with Python" at the University of Applied Sciences Bonn-Rhein-Sieg. The app is designed to be used by students to review each other's assignments and provide feedback. The app is built using the [Flet framework](https://flet.dev), which allows for easy creation of web applications in Python.

## Requirements
- Python 3.12+
- Poetry 2.0+

## Setting up the environment
Install the required dependencies using Poetry. If you don't have Poetry installed, you can install it by following the instructions on the [Poetry website](https://python-poetry.org/docs/#installation).

### install dependencies
```bash
poetry install
```

## Run the app

To run the app, you can use the `task` command provided by taskify.
```
poetry run task dev
```

Flet supports hot reloading, so you can make changes to your code and see the updates in real-time without restarting the app. This is especially useful during development.
I have however noticed that the hot reloading does not always work as expected. If you encounter issues with hot reloading, you can try stopping the app and running it again using the command above.

## Build the app

To build the app, you can use the `task` command provided by taskify.
```
poetry run task build
```

This will create a standalone executable for your app. The executable will be created in the `dist` folder. You can then distribute this executable to others without requiring them to install Python or any dependencies.
This is mainly used for the CI/CD pipeline, but you can also use it to build the app locally. The build process may take some time, depending on the size of your app and the number of dependencies.

## Setting up Visual Studio Code
This project is configured to work with Visual Studio Code and provides a `.vscode` folder with the necessary settings. To set up Visual Studio Code for this project, follow these steps:
1. Open the project folder in Visual Studio Code.
2. Install the recommended extensions when prompted. Some of the recommended extensions are optional, but they can enhance your development experience. The following extensions are **required**:
    - Python
    - Pylance
    - Black Formatter

3. If you have the Python extension installed, you may need to select the correct Python interpreter for the project. You can do this by opening the command palette (Ctrl+Shift+P or Cmd+Shift+P) and typing `Python: Select Interpreter`. Choose the interpreter that corresponds to your Poetry environment. You can verify the correct interpreter by checking the name of the environment in the bottom left right corner of the VS Code window. It should match the name of the environment created by Poetry.