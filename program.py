def check_password_strength(password):
    # Function to check the strength of the password
    length = len(password)  # Calculate the length of the password
    if length < 8:
        return "Weak: Password should be at least 8 characters long."
        # Return a message indicating the password is weak if its length is less than 8
    elif length >= 8 and length < 12:
        if any(char.isdigit() for char in password):
            return "Moderate: Password should be at least 12 characters long."
            # Return a message indicating the password is moderate if its length is between 8 and 11 (inclusive)
            # and it contains at least one digit
        else:
            return "Weak: Password should include at least one digit."
            # Return a message indicating the password is weak if its length is between 8 and 11 (inclusive)
            # and it does not contain any digit
    elif length >= 12:
        if any(char.isdigit() for char in password):
            return "Strong: Password meets the minimum requirements."
            # Return a message indicating the password is strong if its length is 12 or greater and it contains at least one digit
        else:
            return "Moderate: Password should include at least one digit."
            # Return a message indicating the password is moderate if its length is 12 or greater and it does not contain any digit


# Test the password strength checker
password = input("Enter your password: ")  # Prompt the user to enter a password
result = check_password_strength(password)  # Call the function to check the strength of the password
print(result)  # Print the result indicating the strength of the password