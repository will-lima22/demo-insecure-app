import pickle

# Desserialização insegura
def load_data(data):
    return pickle.loads(data)  # RCE vulnerability


# Hardcoded password
def authenticate(password):
    if password == "admin123":
        return True
    return False
