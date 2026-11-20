# Kirill M16P2 11/20/2026

from tkinter import *
from tkinter import messagebox

# Define function for three methods
def compute(quantity, price, discount_rate):
# Finding total value, discount value and final price
    total = quantity * price
    discount = total * (discount_rate / 100)
    final_price = total - discount
    return total, discount, final_price

# Define function with the quantity, price, and discount rate
def on_calculate():
    try:
        quantity = int(qty_entry.get())
        price = float(price_entry.get())
        discount_rate = float(disc_entry.get())
        total, discount, final_price = compute(quantity, price, discount_rate)
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers")
        return

    result_text.set(
        f"Quantity: {quantity}"
        f"Price: ${price:,.2f}"
        f"Discount rate: %{discount_rate}"
        f"Discount amount: ${discount}"
        f"Discount price: ${final_price}"
    )

# Define function for saving our result into the file
def save_result():
    text = result_text.get()
    if not text:
        messagebox.showwarning("Nothing to save")
        return
    try:
        with open("results.txt", "a") as f:
            f.write(text)
    except OSError as e:
        messagebox.showerror("Save error")
        return
    messagebox.showinfo("Saved")

# Define window, it size and color
window = Tk()
window.geometry("800x500")
window.resizable(False, False)
window.title("Compute")
window.config(background='light blue')

# Define each input on the window
Label(window, text="Quantity:", bg="light blue").grid(row=0, column=0, padx=10, pady=5, sticky="e")
qty_entry = Entry(window)
qty_entry.grid(row=0, column=1, padx=10, pady=5)

Label(window, text="Price:", bg="light blue").grid(row=1, column=0, padx=10, pady=5, sticky="e")
price_entry = Entry(window)
price_entry.grid(row=1, column=1, padx=10, pady=5)

Label(window, text="Discount rate:", bg="light blue").grid(row=2, column=0, padx=10, pady=5, sticky="e")
disc_entry = Entry(window)
disc_entry.grid(row=2, column=1, padx=10, pady=5)

# Define button for calucalting final result
Button(window, text="Calculate", command=on_calculate).grid(row=3, column=0, columnspan=2, pady=10)

# Define printing method on the window
result_text = StringVar()
Label(window, textvariable=result_text, justify="left", bg="light blue",
    font=("Courier", 11)).grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Define button for saving result
Button(window, text="Save result", command=save_result).grid(row=5, column=0, columnspan=2, pady=5)

# Calling for the window
window.mainloop()