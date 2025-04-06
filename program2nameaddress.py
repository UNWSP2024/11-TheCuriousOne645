import tkinter as tk

# Function to display name and address
def show_info():
    info_label.config(text="Austin Tobin\n5130 Hermantown Rd.\nMN")

# Create the main window
root = tk.Tk()
root.title("Name and Address")

# Add a label to display info
info_label = tk.Label(root, text="", font=("Arial", 12), pady=10)
info_label.pack()

# Add "Show Info" button
show_button = tk.Button(root, text="Show Info", command=show_info, padx=10, pady=5)
show_button.pack(pady=5)

# Add "Quit" button
quit_button = tk.Button(root, text="Quit", command=root.destroy, padx=10, pady=5)
quit_button.pack(pady=5)

# Start the GUI event loop
root.mainloop()
