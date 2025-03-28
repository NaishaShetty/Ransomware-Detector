import os
from cryptography.fernet import Fernet

# Function to check if a file is encrypted
def is_encrypted(file_path):
    try:
        with open(file_path, "rb") as file:
            data = file.read(100)  # Read first 100 bytes

        # If the first bytes start with Fernet's pattern, it's encrypted
        if data.startswith(b'gAAAAA'):
            return True
        return False
    except Exception as e:
        return False  # If an error occurs, assume it's not encrypted

# Function to detect encrypted files
def detect_encrypted_files(target_folder):
    suspicious_files = []

    for file_name in os.listdir(target_folder):
        file_path = os.path.join(target_folder, file_name)

        if os.path.isfile(file_path):
            if is_encrypted(file_path):  # Check if the file is unreadable
                suspicious_files.append(file_name)

    return suspicious_files

if __name__ == "__main__":
    target_folder = "test_files"
    print("🔍 Scanning for ransomware activity...")
    infected_files = detect_encrypted_files(target_folder)

    if infected_files:
        print("⚠️ WARNING: Possible ransomware detected!")
        for file in infected_files:
            print(f"🚨 Suspicious file: {file}")
    else:
        print("✅ No ransomware detected. System safe!")
