import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from datetime import datetime

# Function to save user data to Excel
def save_to_excel():
    # Get user input
    name = entry_name.get()
    city = entry_city.get()
    state = entry_state.get()
    country = entry_country.get()
    contact = entry_contact.get()
    email = entry_email.get()
    father_name = entry_father.get()
    mother_name = entry_mother.get()
    occupation = entry_occupation.get()
    document = document_var.get()

    # Validate input
    if not all([name, city, state, country, contact, email, father_name, mother_name, occupation, document]):
        messagebox.showwarning("Input Error", "Please fill all fields")
        return

    # Create a dictionary for the data
    data = {
        "Name": [name],
        "City": [city],
        "State": [state],
        "Country": [country],
        "Contact Number": [contact],
        "Email": [email],
        "Father's Name": [father_name],
        "Mother's Name": [mother_name],
        "Occupation": [occupation],
        "Document": [document],
        "Timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    }

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Save to Excel
    try:
        # Check if the file already exists
        try:
            existing_df = pd.read_excel("user_data.xlsx")
            df = pd.concat([existing_df, df], ignore_index=True)
        except FileNotFoundError:
            pass

        # Save the updated DataFrame to Excel
        df.to_excel("user_data.xlsx", index=False)
        messagebox.showinfo("Success", "Data saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("User Data Entry Form")
root.geometry("600x600")
root.configure(bg="#f0f0f0")

# Add a title label with animation
title_label = tk.Label(
    root,
    text="User Data Entry Form",
    font=("Helvetica", 20, "bold"),
    bg="#f0f0f0",
    fg="#4CAF50"
)
title_label.pack(pady=10)

# Create a frame for the form
form_frame = tk.Frame(root, bg="#f0f0f0")
form_frame.pack(pady=10)

# Function to animate button on hover
def on_enter(e):
    save_button.config(bg="#45a049", fg="white")

def on_leave(e):
    save_button.config(bg="#4CAF50", fg="white")

# Create form fields
entry_name = tk.Entry(form_frame, font=("Helvetica", 12))
entry_city = tk.Entry(form_frame, font=("Helvetica", 12))
entry_state = tk.Entry(form_frame, font=("Helvetica", 12))
entry_country = tk.Entry(form_frame, font=("Helvetica", 12))
entry_contact = tk.Entry(form_frame, font=("Helvetica", 12))
entry_email = tk.Entry(form_frame, font=("Helvetica", 12))
entry_father = tk.Entry(form_frame, font=("Helvetica", 12))
entry_mother = tk.Entry(form_frame, font=("Helvetica", 12))
entry_occupation = tk.Entry(form_frame, font=("Helvetica", 12))

# Add fields to the form
fields = [
    ("Enter Your Name", entry_name),
    ("Enter Your City", entry_city),
    ("Enter Your State", entry_state),
    ("Enter Your Country", entry_country),
    ("Contact Number", entry_contact),
    ("Email", entry_email),
    ("Father's Name", entry_father),
    ("Mother's Name", entry_mother),
    ("Occupation", entry_occupation)
]

for i, (label_text, entry) in enumerate(fields):
    label = tk.Label(form_frame, text=label_text, font=("Helvetica", 12), bg="#f0f0f0")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
    entry.grid(row=i, column=1, padx=10, pady=5)

# Add document dropdown
document_label = tk.Label(form_frame, text="Document", font=("Helvetica", 12), bg="#f0f0f0")
document_label.grid(row=len(fields), column=0, padx=10, pady=5, sticky="w")
document_var = tk.StringVar()
document_dropdown = ttk.Combobox(
    form_frame,
    textvariable=document_var,
    values=["Adhaar Card", "Voter ID", "Passport", "Driving License", "Pan Card", "Ration Card", "Birth Certificate"],
    font=("Helvetica", 12),
    state="readonly"
)
document_dropdown.grid(row=len(fields), column=1, padx=10, pady=5)
document_dropdown.current(0)

# Create a save button with animation
save_button = tk.Button(
    root,
    text="Save Data",
    font=("Helvetica", 14, "bold"),
    bg="#4CAF50",
    fg="white",
    command=save_to_excel,
    relief="flat"
)
save_button.pack(pady=20)
save_button.bind("<Enter>", on_enter)
save_button.bind("<Leave>", on_leave)

# Run the application
root.mainloop()