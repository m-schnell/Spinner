import tkinter as tk

# Function to update the spinner shading
def update_spinner():
    try:
        percentage = float(percentage_entry.get())
        if 0 <= percentage <= 100:
            if percentage == 100: # special case because the extent is equal to the start at 360 degrees
                canvas.itemconfig(pie_slice, extent=359.99999)
            else:
                angle = -(360 * percentage / 100)  # Convert percentage to angle
                canvas.itemconfig(pie_slice, start=90, extent=angle)
        else:
            raise ValueError("Percentage must be between 0 and 100.")
    except ValueError as e:
        result_label.config(text=str(e))

def on_enter(event):
    update_spinner()

# Create the main window
root = tk.Tk()
root.title("Spinner GUI")

# Create a canvas to draw the spinner
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

# Create the spinner wheel
canvas.create_oval(50, 50, 150, 150, fill="white", outline="black")

# Create a pie slice for shading
pie_slice = canvas.create_arc(50, 50, 150, 150, start=90, extent=0, fill="yellow", outline="black")

# Create an arrow
canvas.create_line(100, 50, 100, 100, width=2)
canvas.create_polygon(95, 60, 100, 50, 105, 60, fill="black")
#canvas.create_polygon(95, 30, 100, 20, 105, 30, fill="black")

# Create a text box to enter the percentage
percentage_label = tk.Label(root, text="Enter Percentage:")
percentage_label.pack()
percentage_entry = tk.Entry(root)
percentage_entry.pack()

# Create an update button
update_button = tk.Button(root, text="Update Spinner", command=update_spinner)
update_button.pack()

# Create a label to display validation errors
result_label = tk.Label(root, text="", fg="red")
result_label.pack()

# Bind enter key to enter button
root.bind("<Return>", on_enter)

# Set the focus to the input box
percentage_entry.focus_set()

# Run the application
root.mainloop()
