# Import Packages

import tkinter
from tkinter import filedialog

# Function for the file explorer dialog box to appear

def open_file_dialog_box(default_extension):
    
    # path of the file that is going to be stored
    folder = filedialog.asksaveasfilename(

        # default flie extension will be passed on from the main function based on the call
        defaultextension = default_extension,

        # filetypes to filter
        filetypes=[
            ("All files", "*.*"),
            ("Text files", "*.txt"),
            ("Word files", "*.docx"),
            ("CSV files", "*.csv")
        ]
    )

    # Checking whether a folder was selected by the user
    if folder:
        print(f"Selected folder: {folder}")
    return folder