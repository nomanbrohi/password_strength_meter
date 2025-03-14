import random
def password_generator(length):

    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    special_chars = "!@#$%^&*"

    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(special_chars)
    ]
    allchar = letters + digits + special_chars


    for i in range(length - 3):
        password.append(random.choice(allchar))
    random.shuffle(password)
    return "".join(password)



