# To-Do List Application Readme

This readme provides an overview of the **To-Do List Application**, a Python application built using the PyQt5 library
for managing tasks and to-do items. The application allows users to add, organize, and track their tasks in a simple and user-friendly interface.

![Screenshot 2023-09-19 172735](https://github.com/Mohadeseh76/To-Do_List/assets/141071219/be39e626-26e5-44d1-8aa8-080adaf47f8f)

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Project Structure](#project-structure)
5. [Contributing](#contributing)
6. [License](#license)

## Features <a name="features"></a>
- **Task Management**: Users can add tasks to a list by entering task names and optional due dates.
- **Task Status**: Tasks can be marked as completed or pending.
- **Date Selection**: Users can set due dates for tasks using a date picker.
- **Visual Customization**: The application features a colorful and user-friendly interface.
- **Data Persistence**: Task data is saved to a file (`todo_data.pkl`) for persistence between application launches.
- **Reset**: Users can clear all tasks from the list.
- **Save**: Users can save the current task list to the data file.

## Installation <a name="installation"></a>
To run the To-Do List Application, follow these steps:

1. Ensure you have Python 3.x installed on your system.

2. Install the PyQt5 library using pip:
   ```bash
   pip install PyQt5
   ```

3. Clone or download the project from the GitHub repository:
   ```bash
   git clone https://github.com/yourusername/todo-list-app.git
   ```

4. Navigate to the project directory:
   ```bash
   cd todo-list-app
   ```

5. Run the application:
   ```bash
   python main.py
   ```

## Usage <a name="usage"></a>
- **Adding Tasks**: Enter a task description in the text input box and select an optional due date using the date picker.
-  Click the "Add Task" button to add the task to the list.

- **Marking Tasks as Complete**: Click the checkbox next to a task to mark it as completed. Click the checkbox again to mark it as pending.

- **Clearing Completed Tasks**: Click the "Clear Completed" button to remove all completed tasks from the list.

- **Saving Data**: Click the "Save" button to save the current task list to the data file (`todo_data.pkl`).

- **Resetting Data**: Click the "Reset" button to clear all tasks from the list.

## Project Structure <a name="project-structure"></a>
- `main.py`: The main application script that defines the PyQt5-based GUI and the to-do list logic.
- `todo_data.pkl`: A binary data file used to persist task data.
- `README.md`: This readme file.

## Contributing <a name="contributing"></a>
Contributions to this project are welcome. You can contribute by:
- Reporting issues or suggesting enhancements through GitHub issues.
- Forking the repository and creating pull requests to fix issues or add new features.
- Providing feedback and suggestions for improvements.

## License <a name="license"></a>
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

