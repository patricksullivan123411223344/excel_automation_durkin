import tkinter as tk
from tkinter import ttk
from excel_controller import dynamic_write, dynamic_read, dynamic_update, dynamic_delete
import json

# Define main menu / window size / initial drop box data
options = ["Student Rentals", "Add Managed Properties"]
app = tk.Tk()
app.title("Excel CRUD Operations")
app.geometry("600x400")
label = tk.Label(app, text="Excel CRUD Operations Main Menu", font=("Arial", 16))
combo_mm = ttk.Combobox(app, values=options, state="readonly")

def on_selection_handler(event) -> None:
    selected_value = combo_mm.get()
    print(f"User selected: {selected_value}")
    handle_menu_selection(selected_value)

def handle_menu_selection(selected_value: str) -> None:
    if selected_value == "Student Rentals":
        student_rental_menu()
    elif selected_value == "Add Managed Properties":
        add_property_menu()
    else:
        print("Invalid selection. Please choose a valid option.")

def student_rental_menu():
    win = tk.Toplevel(app)
    win.title("Student Rentals")
    tk.Label(win, text="Student Rentals Menu", font=("Arial", 14)).pack(padx=20, pady=10)

    form_frame = ttk.Frame(win)
    form_frame.pack(padx=10, pady=10, fill="x")

    # Group Members / Properties Input
    tk.Label(form_frame, text="Group Members").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    group_entry = tk.Entry(form_frame)
    group_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    tk.Label(form_frame, text="Desired Properties").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    properties_entry = tk.Entry(form_frame)
    properties_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    def submit():
        group_value = group_entry.get().strip()
        properties_value = properties_entry.get().strip()
        payload = {
            "group_members": group_value,
            "desired_properties": properties_value,
        }
        # append payload to student_rentals.json
        try:
            with open("student_rentals.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                if not isinstance(data, list):
                    data = []
        except FileNotFoundError:
            data = []
        data.append(payload)
        with open("student_rentals.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print("Saved payload to student_rentals.json:", payload)
        win.destroy()

    submit_button = tk.Button(win, text="Submit", command=submit)
    submit_button.pack(pady=10)

def add_property_menu() -> None:
    win = tk.Toplevel(app)
    win.title("Add Managed Properties")
    tk.Label(win, text="Add Managed Properties Menu", font=("Arial", 14)).pack(padx=20, pady=10)
    # TODO: build add-property controls here

# Main loop for the application's main menu.
def main_menu():
    label.pack(pady=20)
    combo_mm.set("Select an option")
    combo_mm.pack(pady=20)
    combo_mm.bind("<<ComboboxSelected>>", on_selection_handler)

if __name__ == "__main__":
    main_menu()
    app.mainloop()


