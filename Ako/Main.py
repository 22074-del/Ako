import tkinter as tk

def home_page():
    # Create the main window
    root = tk.Tk()
    root.title("Home Page")
    root.geometry("1900x1000")
    
    # Create a label for the home page
    label = tk.Label(root, text="  ")
    label.pack(pady=20)

    # Create the status label
    status = tk.Label(root, text="Welcome to the Home Page!", font=("Arial", 24, "bold"))
    status.pack(pady=20)

    # Define the button click event
    def onclick():
        status.config(text="Button Clicked!")

    # Create the button
    quiz_button = tk.Button(root, text="Click Me", command=onclick, width=20, height=2)
    quiz_button.pack(pady=20)
    game_button = tk.Button(root, text="Click Me", command=onclick, width=20, height=2)
    game_button.pack(pady=20)
    threebutton = tk.Button(root, text="Click Me", command=onclick, width=20, height=2)
    threebutton.pack(pady=20)
    fourbutton = tk.Button(root, text="Click Me", command=onclick, width=20, height=2)
    fourbutton.pack(pady=20)


    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    home_page()