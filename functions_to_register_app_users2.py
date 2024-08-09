# Start coding here
import re

def validate_name(name):
    if not name or len(name) < 3:
        raise ValueError("Name must at least 3 characters.")
    return True

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        raise ValueError("Invalid email address.")
    return True

def validate_password(password):
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters.")
    if not re.search(r'[A-Z]', password):
        raise ValueError("Passsword must contain at least 1 uppercase letter.")
    if not re.search(r'[0-9]', password):
        raise ValueError("Password must contain at least 1 digit")
    return True

# 1. Function to validate user input from sign-up form
def validate_user(name, email, password):
    """Validate the user name, email and password.

    Args:
        name (string): Name that we're attempting to validate.
        email (string): Email address that we're attempting to validate.
        password (string): Password that we're attempting to validate.

    Returns:
        Boolean: Will return True if all validation checks pass

    Raises ValueError if validation fails.
    """

    # Check if name is not valid, if not raise value error.
    if validate_name(name) == False:
        raise ValueError("Please make sure your name is greater than 2 characters!")

    # Check if email is not valid, if not raise value error.
    if validate_email(email) == False:
        raise ValueError("Your email address is in the incorrect format, please enter a valid email.")

    # Check if password is not valid, if not raise value error.
    if validate_password(password) == False:
        raise ValueError("Your password is too weak, ensure that your password is greater than 8 characters, contains a capital letter and a number.")

    # If none of the if not statements are triggered, return True
    return True

# 2. Function to register validated user if all checks have passed
def register_user(name, email, password):
    """Attempt to register the user if they pass validation.

    Args:
        name (string): Name of the user
        email (string): Email address of the user
        password (string): Password of the user

    Returns:
        Dict: Return a dictionary with the user details

    Raises ValueError on missing arguments.
    """

    # Check if user input is valid by calling the validate user function
    if validate_user(name, email, password):
        # Create user object with details
        user = {
            "name": name,
            "email": email,
            "password": password
        }

        # Return user object
        return user

    # If validation fails, return False
    return False
# Use as many cells as you need