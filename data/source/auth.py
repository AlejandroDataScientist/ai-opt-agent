import hashlib

USER_DB = {
    "admin": hashlib.sha256("12345".encode()).hexdigest()
}

def authenticate(username, password):
    pw_hash = hashlib.sha256(password.encode()).hexdigest()
    if username in USER_DB and USER_DB[username] == pw_hash:
        return True
    return False

def login_required(func):
    def wrapper(is_authenticated, *args, **kwargs):
        if not is_authenticated:
            return "Error: Acceso denegado. Requiere autenticación."
        return func(*args, **kwargs)
    return wrapper

