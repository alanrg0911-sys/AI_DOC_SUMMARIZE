from upload_file import upload_pdf
from upload_file import extract_text
from summarize import summarize
from history import save_history, view_history
from pathlib import Path
import threading
from tkinter import ttk
import tkinter as tk

root = tk.Tk()
root.withdraw()

loading_window = None
progress = None


def show_loading():

    global loading_window, progress

    loading_window = tk.Toplevel(root)
    loading_window.title("Generating Summary")
    loading_window.geometry("350x100")

    progress = ttk.Progressbar(
        loading_window,
        mode="indeterminate",
        length=250
    )

    progress.pack(pady=20)

    progress.start(10)

    loading_window.update()

def start_summary():

    filepath = upload_pdf()

    if filepath:

        show_loading()

        text = extract_text(filepath)

        thread = threading.Thread(
            target=summarize_document,
            args=(text, filepath),
            daemon=True
        )

        thread.start()

def summarize_document(text, filepath):

    summary = summarize(text)

    filename = Path(filepath).name
    save_history(filename)

    root.after(0, finish_summary, summary)

def finish_summary(summary):

    progress.stop()
    loading_window.destroy()

    print("\n==== SUMMARY ====\n")
    print(summary)

option = int(input("=== Welcome to PDF summarize! ===\n\n" "Please select one of the following options.\n\n " "[ 1 ] Summarize PDF.\n\n [ 2 ] View history.\n"))

if option == 1:
    
    start_summary()


elif option == 2:
    print("\n\n===This is your history so far===\n\n")
    view_history()

while True:

    root.mainloop()
    
    
