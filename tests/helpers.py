import uuid


def generate_name():
    return uuid.uuid4().hex


def generate_pass():
    return uuid.uuid4().hex


def generate_email():
    return f'{uuid.uuid4().hex}@gmail.com'
