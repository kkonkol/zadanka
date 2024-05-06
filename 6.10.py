import hashlib
import os

class AuthenticationServer:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password_hash, salt):
        self.users[username] = (password_hash, salt)

    def get_salt(self, username):
        if username in self.users:
            return self.users[username][1]
        else:
            return None

    def authenticate(self, username, password_hash):
        if username in self.users:
            stored_password_hash, _ = self.users[username]
            return stored_password_hash == password_hash
        return False

class Client:
    def __init__(self, server):
        self.server = server

    def register_manually(self):
        username = input("Podaj nazwę użytkownika: ")
        password = input("Podaj hasło: ")
        print("Podane hasło przed zahaszowaniem:", password)
        self.register(username, password)

    def register(self, username, password):
        salt = os.urandom(16)
        print("Wygenerowana sól:", salt)
        password_hash = hashlib.sha256(password.encode() + salt).hexdigest()
        print("Zahaszowane hasło:", password_hash)
        self.server.add_user(username, password_hash, salt)
        print("Użytkownik zarejestrowany pomyślnie.")

    def login_manually(self):
        username = input("Podaj nazwę użytkownika: ")
        password = input("Podaj hasło: ")
        print("Podane hasło przed zahaszowaniem:", password)
        if self.login(username, password):
            print("Logowanie udane.")
        else:
            print("Niepoprawna nazwa użytkownika lub hasło.")

    def login(self, username, password):
        salt = self.server.get_salt(username)
        print("Przypisana sól do użytkownika:", salt)
        if salt:
            password_hash = hashlib.sha256(password.encode() + salt).hexdigest()
            print("Zahaszowane hasło:", password_hash)
            return self.server.authenticate(username, password_hash)
        else:
            return False

# Przykładowe użycie
server = AuthenticationServer()
client = Client(server)

# Rejestracja nowego użytkownika
client.register_manually()

# Logowanie
client.login_manually()
