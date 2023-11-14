import random
import string

def password_generator(lenght=6):
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    
    
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits)
        ]
    
    remaining_characters = lenght - len(password)
    all_characters = uppercase_letters + lowercase_letters + digits
    password.extend(random.choice(all_characters) for _ in range(remaining_characters))
    
    random.shuffle(password)
    
    str_password = ''.join(password)
    
    return str_password


password = password_generator()
print('Password: ', password)

    
    