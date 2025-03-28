#  Backend

This directory contains the backend logic for simulating ransomware behavior and detecting encrypted files.

##  How It Works

###  **Encryption (Ransomware Simulator)**
- Uses AES encryption (Fernet) from the `cryptography` library.
- Encrypts files inside the `test_files/` directory.
- Appends a `.locked` extension to encrypted files.
- Generates a unique encryption key (`key.key`).

###  **Detection (Ransomware Detector)**
- Scans all files for unreadable (encrypted) content.
- Flags files based on encryption signatures (e.g., `gAAAAA` for Fernet).
- Displays alerts in the console and GUI.

###  **Decryption (Safe Recovery)**
- Uses the stored encryption key (`key.key`) to restore original files.
- Only works if the encryption key is available.



