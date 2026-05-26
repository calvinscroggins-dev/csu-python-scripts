# Program that displays course information using dictionaries

# Dictionary containing course room numbers
room_numbers = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

# Dictionary containing course instructors
instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

# Dictionary containing course meeting times
meeting_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

# Ask the user to enter a course number
course = input("Enter a course number: ").upper()

# Check if the course exists in the dictionaries
if course in room_numbers:

    # Display the course information
    print("\n===== Course Information =====")
    print("Course Number :", course)
    print("Room Number   :", room_numbers[course])
    print("Instructor    :", instructors[course])
    print("Meeting Time  :", meeting_times[course])

else:
    
    # Display an error message if the course is not found
    print("\nCourse not found. Please enter a valid course number.")