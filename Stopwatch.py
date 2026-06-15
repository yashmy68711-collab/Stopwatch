import tkinter as tk

running = False
seconds = 0

def update():
    global seconds

    if running:
        seconds += 1

        mins = seconds // 60
        secs = seconds % 60

        timer_label.config(
            text=f"{mins:02}:{secs:02}"
        )

        window.after(1000, update)

def start():
    global running
    if not running:
        running = True
        update()

def stop():
    global running
    running = False

def reset():
    global running, seconds
    running = False
    seconds = 0
    timer_label.config(text="00:00")

window = tk.Tk()
window.title("Stopwatch")
window.geometry("400x300")

title = tk.Label(
    window,
    text="Stopwatch",
    font=("Arial", 18, "bold")
)
title.pack(pady=15)

timer_label = tk.Label(
    window,
    text="00:00",
    font=("Arial", 30)
)
timer_label.pack(pady=20)

tk.Button(
    window,
    text="Start",
    command=start,
    width=15
).pack(pady=5)

tk.Button(
    window,
    text="Stop",
    command=stop,
    width=15
).pack(pady=5)

tk.Button(
    window,
    text="Reset",
    command=reset,
    width=15
).pack(pady=5)

window.mainloop()