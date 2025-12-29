import re

def check_password_strength(password):
    # Minimum length
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    
    # Check for uppercase letter
    if not re.search(r"[A-Z]", password):
        return "Weak: Password must contain at least one uppercase letter."
    
    # Check for lowercase letter
    if not re.search(r"[a-z]", password):
        return "Weak: Password must contain at least one lowercase letter."
    
    # Check for digit
    if not re.search(r"\d", password):
        return "Weak: Password must contain at least one digit."
    
    # Check for special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak: Password must contain at least one special character."
    
    # Check for spaces
    if re.search(r"\s", password):
        return "Weak: Password must not contain spaces."
    
    return "Strong password!"

# Example usage:
password = input("Enter a password to check: ")
result = check_password_strength(password)
print(result)
