import tkinter as tk
from tkinter import messagebox
import pickle
from sklearn.feature_extraction.text import CountVectorizer

# Load the trained model and CountVectorizer
try:
    with open("spam.pkl", "rb") as model_file, open("vectorizer.pk1", "rb") as vectorizer_file:
        model1 = pickle.load(model_file)
        cv = pickle.load(vectorizer_file)
except FileNotFoundError:
    print("Model or vectorizer file not found. Please ensure 'spam.pkl' and 'vectorizer.pk1' are in the same directory.")
    exit()

# Define the result function
def classify_message():
    message = text_entry.get("1.0", tk.END).strip()  # Get input text from Text widget
    if not message:
        messagebox.showwarning("Input Error", "Please enter a message!")
        return

    # Process the message
    data = [message]
    vect = cv.transform(data).toarray()
    prediction = model1.predict(vect)
    if prediction[0] == 1:
        result_label.config(text="Result: Spam Mail", fg="red")
    else:
        result_label.config(text="Result: Not Spam Mail", fg="green")

# Create the main tkinter window
root = tk.Tk()
root.title("Email Spam Classification")
root.geometry("500x400")

# UI Components
title_label = tk.Label(root, text="Email Spam Classification", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

instruction_label = tk.Label(root, text="Enter your message below:", font=("Arial", 12))
instruction_label.pack(pady=5)

text_entry = tk.Text(root, height=10, width=50, font=("Arial", 12))
text_entry.pack(pady=10)

classify_button = tk.Button(root, text="Classify", font=("Arial", 12), command=classify_message)
classify_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

# Run the application
root.mainloop()