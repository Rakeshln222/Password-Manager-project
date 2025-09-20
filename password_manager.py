import sqlite3
from cryptography.fernet import Fernet
import getpass

# Set your master password here
MASTER_PASSWORD = "mypassword123"

# Generate encryption key (run once)
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Load the encryption key from the file
def load_key():
    return open("key.key", "rb").read()

# Create database if it doesn't exist
def create_db():
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service TEXT NOT NULL,
            username TEXT NOT NULL,
            password BLOB NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Authenticate using master password
def authenticate():
    attempt = getpass.getpass("Enter master password: ")
    if attempt == MASTER_PASSWORD:
        return True
    else:
        print("Incorrect password!")
        return False

# Add a new password entry
def add_password(cipher):
    service = input("Enter service name: ")
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    encrypted_password = cipher.encrypt(password.encode())
    
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute("INSERT INTO passwords (service, username, password) VALUES (?, ?, ?)",
              (service, username, encrypted_password))
    conn.commit()
    conn.close()
    print("Password added successfully!")

# View all stored passwords
def view_passwords(cipher):
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute("SELECT service, username, password FROM passwords")
    rows = c.fetchall()
    conn.close()

    for service, username, encrypted_password in rows:
        decrypted_password = cipher.decrypt(encrypted_password).decode()
        print(f"Service: {service}")
        print(f"Username: {username}")
        print(f"Password: {decrypted_password}")
        print("-" * 20)

# Delete a password entry
def delete_password():
    service = input("Enter service name to delete: ")
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute("DELETE FROM passwords WHERE service = ?", (service,))
    conn.commit()
    conn.close()
    print(f"Deleted entries for {service}")

# Main program loop
def main():
    create_db()
    key = load_key()
    cipher = Fernet(key)

    if not authenticate():
        return

    while True:
        print("\n1. Add Password")
        print("2. View Passwords")
        print("3. Delete Password")
        print("4. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_password(cipher)
        
        elif choice == "2":
            view_passwords(cipher)
        
        elif choice == "3":
            delete_password()
        
        elif choice == "4":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
