import string

def check_password_complexity(password):
    # Define criteria for password complexity
    min_length = 8
    min_lowercase = 1
    min_uppercase = 1
    min_digits = 1
    min_special_chars = 1

    # Check password length
    if len(password) < min_length:
        return "Password should be at least {} characters long.".format(min_length)

    # Check character diversity
    lowercase_count = sum(1 for char in password if char in string.ascii_lowercase)
    uppercase_count = sum(1 for char in password if char in string.ascii_uppercase)
    digits_count = sum(1 for char in password if char in string.digits)
    special_chars_count = sum(1 for char in password if char in string.punctuation)

    # Check if criteria met
    if lowercase_count < min_lowercase:
        return "Password should contain at least {} lowercase character(s).".format(min_lowercase)
    elif uppercase_count < min_uppercase:
        return "Password should contain at least {} uppercase character(s).".format(min_uppercase)
    elif digits_count < min_digits:
        return "Password should contain at least {} digit(s).".format(min_digits)
    elif special_chars_count < min_special_chars:
        return "Password should contain at least {} special character(s).".format(min_special_chars)
    else:
        return "Password meets complexity requirements."

def main():
    # Input password from user
    password = input("Enter your password: ")

    # Check password complexity
    result = check_password_complexity(password)

    # Print result
    print(result)

if __name__ == "__main__":
    main()
