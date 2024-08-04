import pandas as pd
import matplotlib.pyplot as plt

def main():
    while True:
        print("Fitness Tracker")
        print("1. Log Workout")
        print("2. Track Progress")
        print("3. Generate Report")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            exercise_type = input("Exercise Type: ")
            duration = float(input("Duration (minutes): "))
            intensity = input("Intensity (low/medium/high): ")
            calories_burned = float(input("Calories Burned: "))
            notes = input("Notes: ")
            log_workout(exercise_type, duration, intensity, calories_burned, notes)
        
        elif choice == "2":
            metric = input("Metric (weight/measurement): ")
            value = float(input("Value: "))
            track_progress(metric, value)
        
        elif choice == "3":
            generate_report()
        
        elif choice == "4":
            break
        
        else:
            print("Invalid choice. Please try again.")

def log_workout(exercise_type, duration, intensity, calories_burned, notes):
    workout_data = {
        "exercise_type": [exercise_type],
        "duration": [duration],
        "intensity": [intensity],
        "calories_burned": [calories_burned],
        "notes": [notes]
    }
    df = pd.DataFrame(workout_data)
    df.to_csv("workouts.csv", mode='a', header=False, index=False)
    print("Workout logged successfully!")

def track_progress(metric, value):
    progress_data = {
        "metric": [metric],
        "value": [value]
    }
    df = pd.DataFrame(progress_data)
    df.to_csv("progress.csv", mode='a', header=False, index=False)
    print("Progress tracked successfully!")

def generate_report():
    try:
        workouts_df = pd.read_csv("workouts.csv", names=["exercise_type", "duration", "intensity", "calories_burned", "notes"], header=None)
        progress_df = pd.read_csv("progress.csv", names=["metric", "value"], header=None)
        
        # Display workout summary
        print("\nWorkout Summary:")
        print(workouts_df.describe(include='all'))
        
        # Plot progress
        plt.figure(figsize=(10, 6))
        progress_df.groupby('metric').sum()['value'].plot(kind='bar')
        plt.title('Progress Report')
        plt.xlabel('Metric')
        plt.ylabel('Value')
        plt.savefig('progress_report.png')
        plt.show()
        print("Progress report generated and saved as 'progress_report.png'.")

    except FileNotFoundError:
        print("No data found to generate a report.")

if __name__ == "__main__":
    main()
