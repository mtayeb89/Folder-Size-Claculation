import os
import tkinter as tk
from tkinter import filedialog, messagebox


# Function to calculate folder size
def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # Check if it's a file and add its size to the total
            if os.path.isfile(fp):
                total_size += os.path.getsize(fp)
    return total_size


# Function to convert size to human-readable format
def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB")
    i = int((len(str(size_bytes)) - 1) / 3)
    p = pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"


# Function to select folder and calculate size
def calculate_folder_size():
    folder_path = filedialog.askdirectory(title="Select Folder to Calculate Size")
    if not folder_path:
        messagebox.showerror("Error", "No folder selected")
        return

    # Calculate folder size
    folder_size = get_folder_size(folder_path)

    # Convert to human-readable format and display
    readable_size = convert_size(folder_size)
    lbl_size.config(text=f"Folder Size: {readable_size}")


# Create the main Tkinter window
root = tk.Tk()
root.title("Folder Size Calculator")

# Button to select folder and calculate size
btn_select = tk.Button(root, text="Select Folder and Calculate Size", command=calculate_folder_size)
btn_select.pack(pady=10)

# Label to display the folder size
lbl_size = tk.Label(root, text="Folder Size: N/A")
lbl_size.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
