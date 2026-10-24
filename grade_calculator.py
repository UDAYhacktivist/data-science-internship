# Week 2: Student Grade Calculator

def calculate_grade(marks):
    """Determines grade and encouraging message based on marks."""
    if marks >= 90:
        return "A", "Outstanding achievement! Keep up the brilliant work! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good effort! With a little more focus, you can reach the top! 💪"
    elif marks >= 60:
        return "D", "Passed. Consider reviewing challenging topics to improve! 📚"
    else:
        return "F", "Needs Improvement. Don't be discouraged, practice will make you better! 🎯"

def get_valid_marks():
    """Uses a while loop to ensure valid input between 0 and 100."""
    while True:
        user_input = input("Enter marks (0-100): ").strip()
        try:
            marks = float(user_input)
            if 0 <= marks <= 100:
                return marks
            else:
                print("❌ Invalid input! Marks must be strictly between 0 and 100. Try again.\n")
        except ValueError:
            print("❌ Invalid input! Please enter a numerical value. Try again.\n")

def main():
    print("========================================")
    print("       STUDENT GRADE CALCULATOR         ")
    print("========================================\n")
    
    # 1. Get student name
    name = input("Enter student name: ").strip()
    
    # 2. Get validated marks
    marks = get_valid_marks()
    
    # 3. Compute grade and message
    grade, message = calculate_grade(marks)
    
    # 4. Display result card
    print("\n" + "="*40)
    print(f"📊 RESULT FOR {name.upper()}:")
    print(f"Marks:   {marks:.1f}/100")
    print(f"Grade:   {grade}")
    print(f"Message: {message}")
    print("="*40)

if __name__ == "__main__":
    main()