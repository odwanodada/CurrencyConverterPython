from tkinter import *
import requests
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

w = Tk()
w.geometry("300x300")
w.title("Currency")
w.config(bg="pink")


def Currency_converter():
    country=ToCurrency_option.get()
    url = f'https://v6.exchangerate-api.com/v6/432283c2a5a8200001041f81/latest/{country}'

    response = requests.get(url)
    result = response.json()


    x =  float(amount_input.get())
    y =  FromCurrency_option.get()
    z = result['conversion_rates'][y]


    calculate= x/z
    answer_label.config(text=round(calculate, 2))


def reset():
    amount_input.delete(0, END)
    FromCurrency_option.delete(0,END)
    ToCurrency_option.delete(0,END)
    answer_label.config(text="")



def exit():
    message_box = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application')
    if message_box == 'yes':
        w.destroy()
    else:
        pass

# Create a frame
frame = LabelFrame(w, bg="pink", text="Currency Converter", font=("arial", 10, "bold"), pady=45, padx=45)
frame.grid(row=0, columnspan=2, padx=10, pady=10)

# pack label and Entry inside the frame
label1 = Label(frame, text="Enter Amount:", bg="pink", font=("arial", 10, "bold"))
label1.pack()
amount_input = Entry(frame)
amount_input.pack()

From = Label(w,text="From",bg="green")
To = Label(w,text="To",bg="green")

From.grid(row=3, column=0)
To.grid(row=3, column=1)

n = tk.StringVar()
FromCurrency_option = ttk.Combobox(w, width=10, textvariable=n)

# Adding combobox drop down list
FromCurrency_option['values'] = (" ","INR", "USD", "CAD", "CNY", "DKK", "EUR")

FromCurrency_option.grid(row=5, column=0)
FromCurrency_option.current(0)
#ToCurrency_option.grid(row=5, column=1)

n = tk.StringVar()
ToCurrency_option = ttk.Combobox(w, width=10, textvariable=n)

# Adding combobox drop down list
ToCurrency_option['values'] = (" ","INR", "USD", "CAD", "CNY", "DKK", "EUR")

ToCurrency_option.grid(row=5, column=1)
ToCurrency_option.current(0)



convert_button = Button(w, text="Convert", bg="gold",font=("arial", 15, "bold"),command=Currency_converter)
convert_button.grid(row=10, column=0)

reset_button = Button(w, text="Reset", bg="red", font=("arial", 15, "bold"),command=reset)
reset_button.grid(row=10, column=1)

answer_label = Label(w)
answer_label.grid(row=12, columnspan=2, pady=10)


exit_button = Button(w, text="Exit", bg="blue", font=("arial", 15, "bold"),command=exit)
exit_button.grid(row=14, columnspan=1,pady=10)

w.mainloop()


