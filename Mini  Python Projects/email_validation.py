def is_valid_email(email):
    """Function to validate an email without using the re module."""
    try:
        email = email.strip()  # Remove leading/trailing spaces

        # Basic length check
        if len(email) < 6:
            raise ValueError("Too short (Must be at least 6 characters)")

        # First character must be a letter
        if not email[0].isalpha():
            raise ValueError("First character must be a letter")

        # '@' must be present and only once
        if "@" not in email or email.count("@") != 1:
            raise ValueError("Must contain exactly one '@'")

        # Splitting local part and domain
        local_part, domain_part = email.split("@")

        # Domain must contain a dot (.)
        if "." not in domain_part:
            raise ValueError("Domain must contain a '.'")

        # Extract domain extension
        domain_extension = domain_part.split(".")[-1]

        # Valid domain extensions
        valid_extensions = {"com", "net", "org", "edu"}
        if domain_extension not in valid_extensions:
            raise ValueError("Domain must end with .com, .net, .org, or .edu")

        # Checking for invalid characters
        allowed_chars = set("abcdefghijklmnopqrstuvwxyz0123456789_.@")
        for char in email:
            if char.isspace():
                raise ValueError("Cannot contain spaces")
            elif char.isalpha() and char.isupper():
                raise ValueError("Cannot contain uppercase letters")
            elif char not in allowed_chars:
                raise ValueError(f"Contains invalid character '{char}'")

        return "✅ Valid Email"
    
    except ValueError as e:
        return f"❌ Invalid Email: {e}"


# Taking user input and validating with exception handling
try:
    email = input("Enter your email: ").strip()  # Stripping extra spaces
    result = is_valid_email(email)
    print(result)

except KeyboardInterrupt:
    print("\n⚠ Program interrupted by user.")
except Exception as e:
    print(f"⚠ Unexpected Error: {e}")





