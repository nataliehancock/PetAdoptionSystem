import tkinter as tk  # Import tkinter for GUI development
from tkinter import messagebox  # Import messagebox for error and info pop-ups
from PIL import Image, ImageTk  # Import Pillow to handle images

# Function to add a pet to the system
def add_pet():
    pet_name = name_entry.get()  # Retrieve the pet's name from the input field
    pet_age = age_entry.get()  # Retrieve the pet's age from the input field
    pet_breed = breed_entry.get()  # Retrieve the pet's breed from the input field

    # Check if any fields are left empty
    if not pet_name or not pet_age or not pet_breed:
        messagebox.showerror("Input Error", "All fields are required!")  # Show error message for missing fields
        return  # Exit the function if validation fails

    # Validate that the age input is a numeric value
    if not pet_age.isdigit():
        messagebox.showerror("Input Error", "Age must be a number!")  # Show error message for non-numeric age
        return  # Exit the function if validation fails

    # Display a success message with the pet's details
    result_label.config(text=f"Added {pet_name}, Age: {pet_age}, Breed: {pet_breed}.")
    name_entry.delete(0, tk.END)  # Clear the name input field after adding
    age_entry.delete(0, tk.END)  # Clear the age input field after adding
    breed_entry.delete(0, tk.END)  # Clear the breed input field after adding

# Function to open the "Manage Pets" window
def open_manage_pets_window():
    manage_pets_window = tk.Toplevel(window)  # Create a new top-level window
    manage_pets_window.title("Manage Pets")  # Set the title for the new window

    # Add a label and entry field for the pet's name
    tk.Label(manage_pets_window, text="Pet Name:").grid(row=0, column=0, padx=10, pady=5)
    global name_entry  # Declare the name entry field as global to access it in the add_pet function
    name_entry = tk.Entry(manage_pets_window)  # Create an input field for the pet's name
    name_entry.grid(row=0, column=1, padx=10, pady=5)  # Position the entry field in the grid

    # Add a label and entry field for the pet's age
    tk.Label(manage_pets_window, text="Pet Age:").grid(row=1, column=0, padx=10, pady=5)
    global age_entry  # Declare the age entry field as global
    age_entry = tk.Entry(manage_pets_window)  # Create an input field for the pet's age
    age_entry.grid(row=1, column=1, padx=10, pady=5)  # Position the entry field in the grid

    # Add a label and entry field for the pet's breed
    tk.Label(manage_pets_window, text="Pet Breed:").grid(row=2, column=0, padx=10, pady=5)
    global breed_entry  # Declare the breed entry field as global
    breed_entry = tk.Entry(manage_pets_window)  # Create an input field for the pet's breed
    breed_entry.grid(row=2, column=1, padx=10, pady=5)  # Position the entry field in the grid

    # Add a button to submit the pet details
    tk.Button(manage_pets_window, text="Add Pet", command=add_pet).grid(row=3, column=1, pady=10)

    # Add a label to display success or error messages after adding a pet
    global result_label  # Declare the result label as global
    result_label = tk.Label(manage_pets_window, text="")  # Create an empty label for displaying messages
    result_label.grid(row=4, column=0, columnspan=2)  # Position the label in the grid

    # Add the second image with the main label and the description
    image2 = Image.open("pet_image2.jpg")  # Load the second image
    image2 = image2.resize((100, 100))  # Resize the image to fit the UI
    photo2 = ImageTk.PhotoImage(image2)  # Convert the image to a format compatible with tkinter
    tk.Label(manage_pets_window, image=photo2, text="Add Pet Details", compound="top").grid(row=5, column=0, columnspan=2)
    manage_pets_window.photo2 = photo2  # Keep a reference to the image to prevent garbage collection

    # Add italicized, smaller description for the second image
    tk.Label(
        manage_pets_window,
        text="Image Description: Pitbull Rottweiler smiling",  # Add the description for the image
        font=("Arial", 8, "italic"),  # Set the font to italic and smaller size
    ).grid(row=6, column=0, columnspan=2)  # Position the description below the image

# Function to open the "Help" window
def open_help_window():
    help_window = tk.Toplevel(window)  # Create a new top-level window
    help_window.title("Help")  # Set the title for the help window

    # Add a label with instructions on how to use the application
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
        padx=10,  # Add padding around the text
        pady=10,  # Add padding around the text
    ).pack()

    # Add a button to close the help window
    tk.Button(help_window, text="Close", command=help_window.destroy).pack(pady=10)

# Main application window
window = tk.Tk()  # Create the main window
window.title("Pet Adoption Management System")  # Set the title of the main window

# Add a welcome message
tk.Label(window, text="Welcome to the Pet Adoption Management System").grid(row=0, column=0, columnspan=2, pady=10)

# Add the first image with the main label and the description
image1 = Image.open("pet_image1.jpg")  # Load the first image
image1 = image1.resize((100, 100))  # Resize the image to fit the UI
photo1 = ImageTk.PhotoImage(image1)  # Convert the image to a format compatible with tkinter
tk.Label(window, image=photo1, text="Adopt a Pet!", compound="top").grid(row=1, column=0, columnspan=2)
window.photo1 = photo1  # Keep a reference to the image to prevent garbage collection

# Add italicized, smaller description for the first image
tk.Label(
    window,
    text="Image Description: Russian Blue kitten resting",  # Add the description for the first image
    font=("Arial", 8, "italic"),  # Set the font to italic and smaller size
).grid(row=2, column=0, columnspan=2)  # Position the description below the image

# Add a button to open the "Manage Pets" window
tk.Button(window, text="Manage Pets", command=open_manage_pets_window).grid(row=3, column=0, pady=10)

# Add a button to open the "Help" window
tk.Button(window, text="Help", command=open_help_window).grid(row=3, column=1, pady=10)

# Add a button to exit the application
tk.Button(window, text="Exit", command=window.destroy).grid(row=4, column=0, columnspan=2, pady=10)

# Run the application
window.mainloop()  # Start the tkinter event loop
