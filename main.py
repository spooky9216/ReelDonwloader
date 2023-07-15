import tkinter as tk
from tkinter import ttk
import instaloader
import re
import os
import threading

def extract_username_and_media_code_from_url(url):
    pattern = r"(?:https?:\/\/)?(?:www\.)?instagram\.com\/reel\/([a-zA-Z0-9_-]+)\/"
    match = re.match(pattern, url)
    if match:
        media_code = match.group(1)
        username = "instagram"  # Since the URL does not contain the username, use "instagram" as a default
        return username, media_code
    else:
        raise ValueError("Invalid Instagram Reel URL")


def download_reel():
    url = url_entry.get()
    username, media_code = extract_username_and_media_code_from_url(url)

    def download_thread():
        loader = instaloader.Instaloader()

        try:
            post = instaloader.Post.from_shortcode(loader.context, media_code)
            loader.download_post(post, target=f"{username}_reels")
            status_label.configure(text="Download complete!")
            delete_files(f"{username}_reels")
        except instaloader.exceptions.InstaloaderException:
            status_label.configure(text="Unable to download reel.")

    # Create a separate thread for downloading the reel
    thread = threading.Thread(target=download_thread)
    thread.start()


def delete_files(folder_path):
    extensions_to_delete = ['.txt', '.zip', '.jpg', '.jpeg', '.png', '.xz']  # Add more file extensions if needed

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension in extensions_to_delete:
                os.remove(file_path)
                print(f"Deleted: {file_path}")


# Create the main application window
root = tk.Tk()
root.title("Instagram Reel Downloader")
root.geometry("400x200")
root.configure(bg="#333333")  # Set background color

# Create a frame for the form
form_frame = ttk.Frame(root, padding=20)
form_frame.configure(style="Dark.TFrame")  # Apply custom style
form_frame.pack()

# Create form labels
url_label = ttk.Label(form_frame, text="Instagram Reel URL:")
url_label.grid(row=0, column=0, sticky=tk.W)

# Create form fields
url_entry = ttk.Entry(form_frame)
url_entry.grid(row=0, column=1)

# Create submit button
submit_button = ttk.Button(form_frame, text="Download Reel", command=download_reel)
submit_button.grid(row=1, column=1, pady=10)

# Create status label
status_label = ttk.Label(root, text="")
status_label.pack()

# Apply custom styles
style = ttk.Style()

# Configure frame style
style.configure("Dark.TFrame", background="#333333")

# Configure label style
style.configure("Dark.TLabel", background="#333333", foreground="#FFFFFF")

# Configure entry style
style.configure("Dark.TEntry", background="#555555", foreground="#FFFFFF")

# Configure button style
style.configure("Dark.TButton", background="#555555", foreground="#FFFFFF")

# Run the application
root.mainloop()
