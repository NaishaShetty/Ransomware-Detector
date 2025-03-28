import tkinter as tk
from tkinter import messagebox, ttk
from ransomware_detector import detect_encrypted_files

# Scan function
def run_scan():
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, "🔍 Scanning for ransomware...\n")

    infected_files = detect_encrypted_files("test_files")

    if infected_files:
        text_area.insert(tk.END, "\n⚠️ WARNING: Ransomware detected!\n", "warning")
        for file in infected_files:
            text_area.insert(tk.END, f"  - {file}\n", "warning")
        status_label.config(text="⚠️ Threat Detected!", fg="red")
        messagebox.showwarning("Ransomware Alert", "Suspicious encrypted files found!")
    else:
        text_area.insert(tk.END, "\n✅ No ransomware found. Your system is safe!\n", "safe")
        status_label.config(text="✅ No threats detected!", fg="lime")

# UI Setup
root = tk.Tk()
root.title("Ransomware Detector")
root.geometry("600x450")
root.configure(bg="#121212")

# Title Label
title_label = tk.Label(root, text="🛡️ Ransomware Detector", font=("Arial", 18, "bold"), fg="lime", bg="#121212")
title_label.pack(pady=10)

# Text Area for Results
text_area = tk.Text(root, height=14, width=70, bg="#1e1e1e", fg="white", font=("Arial", 10))
text_area.pack(pady=10)
text_area.tag_config("warning", foreground="red", font=("Arial", 10, "bold"))
text_area.tag_config("safe", foreground="lime", font=("Arial", 10, "bold"))

# Status Label
status_label = tk.Label(root, text="", bg="#121212", font=("Arial", 12))
status_label.pack(pady=5)

# Scan Button
scan_button = ttk.Button(root, text="🔍 Scan Now", command=run_scan)
scan_button.pack(pady=10)

# Run the GUI
root.mainloop()
