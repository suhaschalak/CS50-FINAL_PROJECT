# CS50-FINAL_PROJECT
# Fitness Tracker

#### Video Demo: [YouTube URL](https://youtu.be/LE1U6QoO9pk)
#### Description:
The Fitness Tracker project is designed to help users monitor their physical activity, set fitness goals, and track their progress over time. It leverages various technologies and principles to provide a comprehensive fitness tracking solution.

## Project Structure

- `tracker.py`: The main script that runs the fitness tracker application.
- `test_tracker.py`: Contains unit tests for the functions in `tracker.py`.
- `requirements.txt`: Lists all pip-installable libraries required for the project.
- `README.md`: Documentation for the project, including theoretical concepts and usage instructions.

## Libraries

- **pandas**: A powerful data manipulation and analysis library.
- **matplotlib**: A plotting library for creating static, animated, and interactive visualizations.
- **seaborn**: A data visualization library based on matplotlib that provides a high-level interface for drawing attractive and informative statistical graphics.


## Functionality

The Fitness Tracker project includes several key features and functions, organized as follows:

### Main Functions

1. **get_user_input()**:
    - Prompts the user for fitness data, such as exercise type, duration, and calories burned.
    - Ensures that the input is valid through error handling and input validation.

2. **calculate_progress()**:
    - Analyzes the user's fitness data to calculate progress towards set goals.
    - Uses statistical methods to provide insights into the user's fitness trends over time.

3. **generate_report()**:
    - Creates visual reports of the user's fitness data using `matplotlib` and `seaborn`.
    - Provides a comprehensive overview of the user's fitness activities, including charts and graphs.

### Data Handling

- **pandas**: Utilized for data manipulation, cleaning, and storage. It helps in organizing the fitness data into a structured format for easy analysis.
- **matplotlib** and **seaborn**: Used for creating visualizations. These libraries help in generating informative plots that provide insights into the user's fitness progress.

### Additional Functions

1. **validate_input()**:
    - Ensures that the user's input is within acceptable ranges and formats.
    - Provides feedback to the user if the input is invalid and prompts for re-entry.

2. **store_data()**:
    - Saves the user's fitness data to a file or database for persistent storage.
    - Ensures that data is saved in a structured format that can be easily retrieved and analyzed.

3. **load_data()**:
    - Retrieves the user's previously saved fitness data.
    - Allows the user to continue tracking progress without losing any data between sessions.

4. **set_goals()**:
    - Allows the user to set fitness goals, such as target weight, target exercise duration, or calories to burn.
    - Stores these goals and uses them to calculate progress and provide feedback.

5. **display_summary()**:
    - Provides a summary of the user's fitness activities, including total exercise duration, calories burned, and progress towards goals.
    - Uses statistical summaries to give the user a clear picture of their overall fitness journey.

### Exception Handling

- **try-except blocks**: Used throughout the project to handle potential errors, such as invalid input or issues with data retrieval and storage.
- **Custom error messages**: Provide clear feedback to the user, helping them correct mistakes and continue using the application smoothly.

### User Interface

- **Command-line interface (CLI)**: The project uses a simple CLI to interact with the user, providing prompts and displaying information in an easy-to-understand format.
- **Interactive prompts**: Guide the user through entering data, setting goals, and viewing reports, ensuring a smooth and intuitive user experience.

  ## Installing Libraries
  All the necessary libraries are listed in the `requirements.txt` file. To install them, run:
  ```bash
  pip install -r requirements.txt

By integrating these functionalities, the Fitness Tracker project provides a comprehensive tool for users to monitor their physical activities, set and achieve fitness goals, and visualize their progress over time.
