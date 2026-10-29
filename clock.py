import tkinter as tk
from time import strftime


def update_clock():
    time_string = strftime("%I:%M:%S %p")
    day_string = strftime("%A")
    date_string = strftime("%B %d, %Y")

    timelabel.config(text=time_string)
    daylabel.config(text=day_string)
    datelabel.config(text=date_string)

    window.after(1000, update_clock)


window = tk.Tk()
window.title("Digital Clock")
window.configure(bg="#0b1020")
window.geometry("420x320")
window.resizable(False, False)

# Center the window on the screen
window.update_idletasks()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = 420
window_height = 320
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Labels
timelabel = tk.Label(
    window,
    text="",
    font=("Segoe UI", 42, "bold"),
    fg="#7ef9a8",
    bg="#0b1020",
)
timelabel.pack(pady=(30, 8))

daylabel = tk.Label(
    window,
    text="",
    font=("Segoe UI", 28),
    fg="#67e8f9",
    bg="#0b1020",
)
daylabel.pack(pady=6)

datelabel = tk.Label(
    window,
    text="",
    font=("Segoe UI", 20),
    fg="#d5d9ff",
    bg="#0b1020",
)
datelabel.pack(pady=6)

update_clock()
window.mainloop()