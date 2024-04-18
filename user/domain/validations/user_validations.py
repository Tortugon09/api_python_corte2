import re

def validate_email(email):
    email_regex = r'^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[\w]+$'
    if not re.match(email_regex, email):
        return False
    return True

def validate_name(name):
    return name.replace(" ", "").isalpha() and name.strip() != ""