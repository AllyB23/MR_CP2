# AR 1st PERSONAl PORTFOLIO
import tkinter as tk
from tkinter import messagebox

# import your projects
from projects.financial_calculator import main as financial
from projects.fractal_pattern_generator import main as fractal
from projects.personal_library import main as library
from projects.random_password_generator import main as password

# main window
root = tk.Tk()
root.title("My Personal Portfolio")
root.geometry("600x400")
root.configure(bg="#f5e6f2")  # very light pink

current_project = None

# text area for descriptions
info_text = tk.Text(root, height=15, width=60)
info_text.pack(pady=10)


# intro text
def show_intro():
    info_text.delete("1.0", tk.END)
    info_text.insert(tk.END,
        "Welcome to my programming portfolio.\n\n"
        "Select a project to view its description.\n"
        "Click 'Run Project' to launch it."
    )


# project descriptions
def show_financial():
    global current_project
    current_project = financial
    info_text.delete("1.0", tk.END)
    info_text.insert(tk.END,
        "Financial Calculator\n\n"
        "What it does:\nCalculates financial values such as savings or interest.\n\n"
        "What I learned:\n"
        "- How to perform calculations using user input\n"
        "- How to organize code using functions\n\n"
        "Challenge:\nEnsuring calculations were accurate"
    )


def show_fractal():
    global current_project
    current_project = fractal
    info_text.delete("1.0", tk.END)
    info_text.insert(tk.END,
        "Fractal Pattern Generator\n\n"
        "What it does:\nGenerates visual patterns using recursion.\n\n"
        "What I learned:\n"
        "- How recursion works\n"
        "- How patterns are built using loops\n\n"
        "Challenge:\nUnderstanding recursive logic"
    )


def show_library():
    global current_project
    current_project = library
    info_text.delete("1.0", tk.END)
    info_text.insert(tk.END,
        "Personal Library\n\n"
        "What it does:\nStores and manages a list of books.\n\n"
        "What I learned:\n"
        "- How to store data in lists\n"
        "- How to organize information\n\n"
        "Challenge:\nKeeping data structured and easy to update"
    )


def show_password():
    global current_project
    current_project = password
    info_text.delete("1.0", tk.END)
    info_text.insert(tk.END,
        "Random Password Generator\n\n"
        "What it does:\nCreates random secure passwords.\n\n"
        "What I learned:\n"
        "- How to use the random module\n"
        "- How to work with strings\n\n"
        "Challenge:\nMaking passwords strong and random"
    )


# run selected project
def run_project():
    if current_project:
        try:
            current_project.run()
        except Exception as e:
            messagebox.showerror("Error", f"Could not run project:\n{e}")
    else:
        messagebox.showwarning("Warning", "Please select a project first.")


# buttons
tk.Button(root, text="Financial Calculator", command=show_financial).pack()
tk.Button(root, text="Fractal Generator", command=show_fractal).pack()
tk.Button(root, text="Personal Library", command=show_library).pack()
tk.Button(root, text="Password Generator", command=show_password).pack()

tk.Button(root, text="Run Project", command=run_project).pack(pady=10)

# start
show_intro()
root.mainloop()


