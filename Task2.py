import re

# Function to check the strength of a password
def check_password_strength(password):
    strength = 0
    feedback = []

    # Check the length of the password
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")
    
    # Check for digits
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")
    
    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character (e.g., !@#$%^&*).")
    
    # Assess password strength level
    if strength >= 6:
        feedback.append("Password strength: Very Strong")
    elif strength >= 4:
        feedback.append("Password strength: Strong")
    elif strength >= 3:
        feedback.append("Password strength: Moderate")
    else:
        feedback.append("Password strength: Weak")

    return feedback

# Main function
def main():
    password = input("Enter your password: ")
    feedback = check_password_strength(password)

    # Display feedback
    print("\nFeedback:")
    for item in feedback:
        print(f"- {item}")

# Run the program
if __name__ == "__main__":
    main()
