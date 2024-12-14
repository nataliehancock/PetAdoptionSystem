import tkinter as tk  # Import tkinter for GUI development
from tkinter import messagebox  # Import messagebox for error and info pop-ups
from PIL import Image, ImageTk  # Import Pillow to handle images

# Function to add a pet to the system
def add_pet():
    """
    Purpose:
        Collects pet details (name, age, breed) from the user,
        validates the inputs, and displays a success or error message.
    """
    pet_name = name_entry.get()  # Get the pet's name from the input field
    pet_age = age_entry.get()  # Get the pet's age from the input field
    pet_breed = breed_entry.get()  # Get the pet's breed from the input field

    # Validate that no fields are empty
    if not pet_name or not pet_age or not pet_breed:
        messagebox.showerror("Input Error", "All fields are required!")  # Show error if fields are missing
        return

    # Validate that the age is numeric
    if not pet_age.isdigit():
        messagebox.showerror("Input Error", "Age must be a number!")  # Show error if age is not a number
        return

    # If validation passes, display a success message and clear the input fields
    result_label.config(text=f"Added {pet_name}, Age: {pet_age}, Breed: {pet_breed}.")  # Display success message
    name_entry.delete(0, tk.END)  # Clear the name input field
    age_entry.delete(0, tk.END)  # Clear the age input field
    breed_entry.delete(0, tk.END)  # Clear the breed input field

# Function to open the Manage Pets window
def open_manage_pets_window():
    """
    Purpose:
        Opens a new window to manage pet information.
        Allows the user to input pet details and add them to the system.
    """
    manage_pets_window = tk.Toplevel(window)  # Create a new top-level window
    manage_pets_window.title("Manage Pets")  # Set the title of the new window

    # Add labels and input fields for pet details
    tk.Label(manage_pets_window, text="Pet Name:").grid(row=0, column=0, padx=10, pady=5)  # Label for name
    global name_entry
    name_entry = tk.Entry(manage_pets_window)  # Input field for name
    name_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(manage_pets_window, text="Pet Age:").grid(row=1, column=0, padx=10, pady=5)  # Label for age
    global age_entry
    age_entry = tk.Entry(manage_pets_window)  # Input field for age
    age_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(manage_pets_window, text="Pet Breed:").grid(row=2, column=0, padx=10, pady=5)  # Label for breed
    global breed_entry
    breed_entry = tk.Entry(manage_pets_window)  # Input field for breed
    breed_entry.grid(row=2, column=1, padx=10, pady=5)

    # Add a button to submit the pet details
    tk.Button(manage_pets_window, text="Add Pet", command=add_pet).grid(row=3, column=1, pady=10)

    # Label to display success or error messages
    global result_label
    result_label = tk.Label(manage_pets_window, text="")
    result_label.grid(row=4, column=0, columnspan=2)

    # Add an image to the Manage Pets window
    image2 = Image.open("pet_image2.jpg")  # Load the second image
    image2 = image2.resize((100, 100))  # Resize the image
    photo2 = ImageTk.PhotoImage(image2)  # Convert the image to a tkinter-compatible format
    tk.Label(manage_pets_window, image=photo2, text="Add Pet Details", compound="top").grid(row=5, column=0, columnspan=2)
    manage_pets_window.photo2 = photo2  # Keep a reference to avoid garbage collection

# Function to open the Help window
def open_help_window():
    """
    Purpose:
        Opens a new window that provides instructions on how to use the application.
    """
    help_window = tk.Toplevel(window)  # Create a new top-level window
    help_window.title("Help")  # Set the title of the Help window

    # Add instructions as a label
    tk.Label(
        help_window,
        text=(
            "Instructions:\n\n"
            "1. Click 'Manage Pets' to add details about pets.\n"
            "2. Fill in all fields (Name, Age, Breed) and click 'Add Pet'.\n"
            "3. Ensure all inputs are valid (e.g., Age must be a number).\n"
            "4. Click 'Exit' to close the application."
        ),
        justify="left",  # Align the text to the left
        padx=10,  # Add padding
        pady=10,  # Add padding
    ).pack()
    tk.Button(help_window, text="Close", command=help_window.destroy).pack(pady=10)  # Button to close the Help window

# Main application window
window = tk.Tk()  # Create the main window
window.title("Pet Adoption Management System")  # Set the window title

# Add a welcome label
tk.Label(window, text="Welcome to the Pet Adoption Management System").grid(row=0, column=0, columnspan=2, pady=10)

# Add an image to the main dashboard
image1 = Image.open("pet_image1.jpg")  # Load the first image
image1 = image1.resize((100, 100))  # Resize the image
photo1 = ImageTk.PhotoImage(image1)  # Convert the image to a tkinter-compatible format
tk.Label(window, image=photo1, text="Adopt a Pet!", compound="top").grid(row=1, column=0, columnspan=2)
window.photo1 = photo1  # Keep a reference to avoid garbage collection

# Add navigation buttons
tk.Button(window, text="Manage Pets", command=open_manage_pets_window).grid(row=2, column=0, pady=10)  # Button for Manage Pets
tk.Button(window, text="Help", command=open_help_window).grid(row=2, column=1, pady=10)  # Button for Help
tk.Button(window, text="Exit", command=window.destroy).grid(row=3, column=0, columnspan=2, pady=10)  # Button to exit

# Run the application
window.mainloop()  # Start the tkinter event loop