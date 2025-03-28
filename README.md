# Ransomware-Detector

# Overview
This project consists of a ransomware simulator that encrypts files and a detection system that identifies potential ransomware activity. The graphical user interface (GUI) makes it easy to run scans and analyze system security.

# Features
* Simulated Ransomware Attack – Encrypts files in a directory to mimic real ransomware behavior.
* Ransomware Detection – Scans for encrypted files and alerts users.
* Graphical Interface – Easy-to-use GUI with modern design.
* Safe for Testing – Files can be decrypted back safely.
* Customizable – Modify encryption algorithms or detection methods.

  # How it works?

  # Encryption
  - Uses AES encryption (Fernet) from the cryptography library.

  - Encrypts files inside test_files/ and adds a .locked extension.

  - Generates a unique encryption key (key.key).

  # Detection System
  - Scans all files and checks if they are unreadable (encrypted).

  - Flags files based on their encryption patterns (e.g., gAAAAA for Fernet).

  - Displays warnings in the GUI if suspicious files are found.

  # GUI Interface
  - Built using Tkinter with a modern theme.

  - Provides real-time ransomware detection.

  - Shows alerts for encrypted files and allows scanning on demand.
