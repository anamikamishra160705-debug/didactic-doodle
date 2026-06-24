```python
import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Weight and Height must be greater than 0")
            return

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal Weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(
            text=f"BMI: {round(bmi, 2)}\nCategory: {category}"
        )

        save_data(weight, height, round(bmi, 2), category)

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter valid numeric values."
        )

def save_data(weight, height, bmi, category):
    data = {
        "Weight (kg)": [weight],
        "Height (m)": [height],
        "BMI": [bmi],
        "Category": [category]
    }

    df = pd.DataFrame(data)

    if os.path.exists("bmi_records.csv"):
        df.to_csv(
            "bmi_records.csv",
            mode="a",
            header=False,
            index=False
        )
    else:
        df.to_csv(
            "bmi_records.csv",
            index=False
        )

def show_history():
    if os.path.exists("bmi_records.csv"):
        history = pd.read_csv("bmi_records.csv")

        history_window = tk.Toplevel(root)
        history_window.title("BMI History")
        history_window.geometry("600x400")

        text = tk.Text(history_window)
        text.pack(expand=True, fill="both")

        text.insert(tk.END, history.to_string(index=False))
    else:
        messagebox.showinfo("Info", "No records found.")

root = tk.Tk()
root.title("Advanced BMI Calculator")
root.geometry("400x350")

title = tk.Label(
    root,
    text="BMI Calculator",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)

tk.Label(root, text="Enter Weight (kg)").pack()
weight_entry = tk.Entry(root)
weight_entry.pack(pady=5)

tk.Label(root, text="Enter Height (m)").pack()
height_entry = tk.Entry(root)
height_entry.pack(pady=5)

tk.Button(
    root,
    text="Calculate BMI",
    command=calculate_bmi
).pack(pady=10)

tk.Button(
    root,
    text="View History",
    command=show_history
).pack()

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 12)
)
result_label.pack(pady=20)

root.mainloop()
```
