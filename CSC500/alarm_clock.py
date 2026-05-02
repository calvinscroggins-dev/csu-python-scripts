# This program calculates alarm time down to minutes using a 24-hour clock

def calculate_alarm_time_with_minutes():

    try:
        # Get current hour and minute
        current_hour = int(input("Enter current hour (0-23): "))
        current_minute = int(input("Enter current minute (0-59): "))

        # Get wait time in hours and minutes
        wait_hours = int(input("Enter hours to wait: "))
        wait_minutes = int(input("Enter minutes to wait: "))

        # Validate inputs
        if current_hour < 0 or current_hour > 23:
            print("Error: Hour must be between 0 and 23.")
            return

        if current_minute < 0 or current_minute > 59:
            print("Error: Minute must be between 0 and 59.")
            return

        if wait_hours < 0 or wait_minutes < 0:
            print("Error: Wait time cannot be negative.")
            return

        # Convert current time to total minutes
        current_total_minutes = (current_hour * 60) + current_minute

        # Convert wait time to total minutes
        wait_total_minutes = (wait_hours * 60) + wait_minutes

        # Add and wrap around 24 hours (1440 minutes)
        final_total_minutes = (current_total_minutes + wait_total_minutes) % 1440

        # Convert back to hours and minutes
        final_hour = final_total_minutes // 60
        final_minute = final_total_minutes % 60

        # Output result
        print(f"\nAlarm will go off at: {final_hour:02d}:{final_minute:02d}")

    except ValueError:
        print("Error: Please enter valid whole numbers.")


# Run program
calculate_alarm_time_with_minutes()