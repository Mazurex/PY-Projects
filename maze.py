import tkinter as tk

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Hello World App")

    # Set the window to full screen
    root.attributes('-fullscreen', True)

    # Create a label with "Hello World!" text
    label = tk.Label(root, text="Hello World!", font=("Arial", 40))
    label.pack(expand=True)

    # Bind the escape key to exit full screen
    root.bind("<Escape>", lambda event: root.destroy())

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    main()