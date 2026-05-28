import tkinter as tk

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Spreadsheet App")
        self.geometry("700x500")
        self.create_widgets()

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()


