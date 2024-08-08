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

def validate_user(name, email, password):
    try:
        validate_name(name)
        validate_email(email)
        validate_password(password)
        return True
    except ValueError as e:
        print(f"Validation Error: {e}")
        return False
    
def register_user(name, email, password):
    try: 
        if validate_user(name, email, password):
            new_user = {"name": name, "email": email, "password": password}
            return new_user
    except ValueError as e:
        print(f"Registration Error: {e}")
        return False
    
name = "Luong Tuan Vy"
email = "luongtuanvy123@gmail.com"
password = "Hellohello1"

new_user = register_user(name, email, password)
if new_user:
    print("User registered successfully:", new_user)
else:
    print("User registration failed")