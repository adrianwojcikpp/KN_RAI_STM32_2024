import tkinter as tk
import serial

# Set up the serial connection
try:
    ser = serial.Serial('COM3', baudrate=115200, timeout=1)
except Exception as e:
    print(f"Could not open serial port: {e}")
    ser = None

def send_value(event):
    """
    Send the slider value as a 4-digit number to the serial port when the slider is released.
    """
    value = 10*slider.get()
    formatted_value = f"{value:04}"
    if ser:
        ser.write(formatted_value.encode())
    print(f"Sent: {formatted_value}")

# Create the main window
root = tk.Tk()
root.title("Percentage Slider")

# Slider widget
slider = tk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',
    length=300,
    label="Percentage"
)
slider.pack(pady=20)

# Bind slider release event
slider.bind("<ButtonRelease-1>", send_value)

# Run the application
root.mainloop()

# Close the serial connection when done
if ser:
    ser.close()
