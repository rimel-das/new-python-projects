# import re is used to bring in Python’s Regular Expressions (regex) module. This module provides functions to search, match, and manipulate text using patterns.

# Regex helps in validating, searching, and modifying text patterns efficiently.
# For example, checking if an email follows a proper format, like ensuring it starts with a letter, contains "@", and has a valid domain.

# Where is re Used?
#  Email & username validation
#  Password strength checks
#  Extracting phone numbers or URLs from text
#  Formatting & cleaning text






import re

def is_valid_email(email):
    """Function to validate an email with exception handling and regex."""
    try:
        email = email.strip()  # Remove leading/trailing spaces

        # Regular expression for a basic email validation
        email_pattern = r'^[a-z][a-z0-9_.]+@[a-z]+\.[a-z]{2,3}$'

        if not re.match(email_pattern, email):
            raise ValueError("Invalid email format")

        if len(email) < 6:
            raise ValueError("Too short (Must be at least 6 characters)")

        if not email[0].isalpha():
            raise ValueError("First character must be a letter")

        if "@" not in email or email.count("@") != 1:
            raise ValueError("Must contain exactly one '@'")

        if not email.endswith(('.com', '.net', '.org', '.edu')):
            raise ValueError("Domain must end with .com, .net, .org, or .edu")

        # Checking for invalid characters
        for char in email:
            if char.isspace():
                raise ValueError("Cannot contain spaces")
            elif char.isalpha() and char.isupper():
                raise ValueError("Cannot contain uppercase letters")
            elif char.isdigit():
                continue
            elif char in {"_", ".", "@"}:  # Allowed special characters
                continue
            else:
                raise ValueError(f"Contains invalid character '{char}'")

        return " Valid Email"
    
    except ValueError as e:
        return f" Invalid Email: {e}"


# Taking user input and validating with exception handling
try:
    email = input("Enter your email: ").strip()  # Stripping extra spaces
    result = is_valid_email(email)
    print(result)

except KeyboardInterrupt:
    print("\n⚠ Program interrupted by user.")
except Exception as e:
    print(f"⚠ Unexpected Error: {e}")
