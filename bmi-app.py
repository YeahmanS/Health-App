import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import matplotlib.pyplot as plt

def plot_bmi(data_file):
    weights = []
    heights = []
    bmis = []

    # Read data from file
    with open(data_file, "r") as file:
        for line in file:
            weight, height, bmi = line.strip().split(',')
            weights.append(float(weight))
            heights.append(float(height))
            bmis.append(float(bmi))

    # Plot BMI data
    plt.figure(figsize=(10, 6))
    plt.plot(bmis, marker='o', color='b', linestyle='-')

    # Add labels and title
    plt.title('BMI Over Time')
    plt.xlabel('Record Number')
    plt.ylabel('BMI')

    # Show grid
    plt.grid(True)

    # Show plot
    plt.show()

def plotit():
    data_file = "bmi.csv"
    plot_bmi(data_file)

def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index (BMI) based on weight (in kilograms) and height (in centimeters).
    Formula: BMI = weight (kg) / (height (CM))^2
    """
    return round((weight / ((height/100) ** 2)),2)

def save_bmi_data(weight, height, bmi):
    with open("bmi.csv", "a") as file:
        file.write(f"{weight},{height},{bmi}\n")

def add_to_data():
    height=height_int.get()
    weight=Weight_int.get()
    bmi=calculate_bmi(weight, height)
    save_bmi_data(weight, height, bmi)

def convert():
    height=height_int.get()
    weight=Weight_int.get()
    bmi=calculate_bmi(weight, height)
    print_statement = "YOUR BMI IS - " + str(bmi)
    output_str.set(print_statement)

#window
window =tk.Tk()
window.title('BMI APP')
window.geometry('400x400')

#title
title_label = ttk.Label(master=window, text= 'BMI CALCULATOR', font='Calibri 24 bold')
title_label.pack()

#Hieght Input

height_frame = ttk.Frame(master = window)
height_int = tk.IntVar()
height_entry= ttk.Entry(master = height_frame , textvariable=height_int)
height_label = ttk.Label(master=height_frame, text= 'Height in cm', font='Calibri 16')
height_entry.pack(side='left', padx= 10)
height_label.pack(side='right', padx= 10)
height_frame.pack(pady=10)

#Weight input

Weight_frame = ttk.Frame(master = window)
Weight_int = tk.IntVar()
Weight_entry= ttk.Entry(master = Weight_frame , textvariable=Weight_int)
Weight_label = ttk.Label(master=Weight_frame, text= 'Weight in kg', font='Calibri 16')
Weight_entry.pack(side='left', padx= 10)
Weight_label.pack(side='right', padx= 10)
Weight_frame.pack(pady=10)

#date entry
date_frame = ttk.Frame(master = window)
date = ttk.DateEntry(master=date_frame, bootstyle="dark")
add_button=ttk.Button(master= date_frame , text= 'Add to Data', bootstyle = DARK , command= add_to_data)
add_button.pack(side='right',padx=10)
date.pack(side='left', padx= 10)
date_frame.pack(pady=10)

#button frame
convert_frame = ttk.Frame(master = window)
convert_button = ttk.Button(master= convert_frame , text= 'Convert', bootstyle = SUCCESS , command= convert)
progress_button = ttk.Button(master=convert_frame , text='Show Progress',  bootstyle = SUCCESS , command= plotit )
convert_button.pack(side='left', padx= 10)
progress_button.pack()
convert_frame.pack(pady=10)

#OUTPUT
output_str=tk.StringVar()
output_label = ttk.Label(master=window, text= 'Output', font='Calibri 24 ', textvariable=output_str)
output_label.pack()

#run
window.mainloop()
