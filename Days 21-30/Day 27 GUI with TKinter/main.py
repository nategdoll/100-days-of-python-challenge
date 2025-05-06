import tkinter as tk

window = tk.Tk()
window.title("Miles to Km Converter")
window.minsize(width=250, height=20)
window.config(padx=20, pady=20)
window.config(bg="white")

# Labels
miles_label = tk.Label(text="Miles", bg="white", font=("Arial", 12, "bold"))
miles_label.grid(column=3, row=0)
km_label = tk.Label(text="Kilometers", bg="white", font=("Arial", 12, "bold"))
km_label.grid(column=3, row=1)
equal_label = tk.Label(text="is equal to", bg="white", font=("Arial", 12, "bold"))
equal_label.grid(column=1, row=1)
result_label = tk.Label(text="0", bg="white", font=("Arial", 12, "bold"))
result_label.grid(column=2, row=1)

# Entry
entry = tk.Entry(width=10, font=("Arial", 12, "bold"))
entry.grid(column=2, row=0)
entry.focus()

# Button
def calculate():
    miles = float(entry.get())
    km = miles * 1.60934
    result_label.config(text=km)

calculate_button = tk.Button(text="Calculate", command=calculate, bg="white", font=("Arial", 12, "bold"))
calculate_button.grid(column=2, row=2)

# Has to be at the end
window.mainloop()