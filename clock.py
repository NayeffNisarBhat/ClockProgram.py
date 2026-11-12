import tkinter as tk
from time import strftime


def update_clock():
    time_string = strftime("%I:%M:%S %p")
    day_string = strftime("%A")
    date_string = strftime("%B %d, %Y")

    timelabel.config(text=time_string)
    timelabel_shadow.config(text=time_string)
    daylabel.config(text=day_string.upper())
    datelabel.config(text=date_string)

    window.after(1000, update_clock)


def build_clock():
    
    global window, timelabel, timelabel_shadow, daylabel, datelabel

    window = tk.Tk()
    window.title("Liquid Glass Clock")
    window.configure(bg="#08111f")
    window.resizable(False, False)

    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    width = 470
    height = 330
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

    # Main liquid-glass panel
    panel = tk.Frame(
        window,
        bg="#101827",
        bd=0,
        highlightbackground="#8b5cf6",
        highlightthickness=1,
        padx=30,
        pady=20,
    )
    panel.pack(expand=True, fill="both", padx=18, pady=18)

    # Soft blurred background glow effect using nested panels
    glow = tk.Label(
        panel,
        bg="#1e293b",
        bd=0,
        padx=0,
        pady=0,
    )
    glow.place(x=12, y=12, relwidth=1.0, relheight=1.0)

    heading = tk.Label(
        panel,
        text="LOCAL TIME",
        font=("Segoe UI", 10, "bold"),
        fg="#cbd5e1",
        bg="#101827",
    )
    heading.place(relx=0.5, y=18, anchor="n")

    timelabel_shadow = tk.Label(
        panel,
        text="",
        font=("Segoe UI", 42, "bold"),
        fg="#4ade80",
        bg="#101827",
    )
    timelabel_shadow.place(relx=0.5, y=82, anchor="n", x=4)

    timelabel = tk.Label(
        panel,
        text="",
        font=("Segoe UI", 42, "bold"),
        fg="#f8fafc",
        bg="#101827",
    )
    timelabel.place(relx=0.5, y=82, anchor="n")

    divider = tk.Canvas(panel, width=230, height=2, bg="#101827", highlightthickness=0)
    divider.create_line(0, 1, 230, 1, fill="#8b5cf6", width=2)
    divider.place(relx=0.5, y=150, anchor="n")

    daylabel = tk.Label(
        panel,
        text="",
        font=("Segoe UI", 22, "bold"),
        fg="#67e8f9",
        bg="#101827",
    )
    daylabel.place(relx=0.5, y=185, anchor="n")

    datelabel = tk.Label(
        panel,
        text="",
        font=("Segoe UI", 15),
        fg="#dfe7f5",
        bg="#101827",
    )
    datelabel.place(relx=0.5, y=230, anchor="n")

    update_clock()


if __name__ == "__main__":
    build_clock()
    window.mainloop()