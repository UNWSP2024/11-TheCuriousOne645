import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Favorite Saying")

# Add a label with the favorite saying
saying = "Men are like steel. When they lose their temper, they lose their worth. - Chuck Norris"
label = tk.Label(root, text=saying, wraplength=300, justify="center", padx=10, pady=10)
label.pack(pady=20)

# Start the GUI event loop
root.mainloop()
