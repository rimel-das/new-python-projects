import tkinter as tk
import random
import time

# Sample text for the typing test
# This list contains different texts that will be randomly selected for the typing test
test_texts = [
    "The quick brown fox jumps over the lazy dog.",
    "Programming is an art that requires logic and creativity.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "Typing quickly improves productivity and enhances communication skills.",
    "Python is a powerful programming language known for its simplicity and readability.",
    "Hard work beats talent when talent doesn’t work hard."
]

class TypingSpeedTest:
    def __init__(self, root):
        # Initialize the GUI window
        self.root = root
        self.root.title("Monkeytype-Inspired Typing Test")
        self.root.geometry("900x500")  # Set window size
        self.root.configure(bg="#1e1e1e")  # Set background color
        
        # Variables to store selected text and start time
        self.selected_text = ""
        self.start_time = None
        self.history = []  # List to store past test results
        
        # Title label
        tk.Label(root, text="Typing Speed Test", font=("Arial", 20, "bold"), bg="#1e1e1e", fg="white").pack(pady=10)
        
        # Label to display the text to be typed
        self.text_display = tk.Label(root, text="", wraplength=800, font=("Arial", 14), bg="#1e1e1e", fg="lightgray")
        self.text_display.pack(pady=10)
        
        # Entry box for typing input
        self.entry = tk.Entry(root, font=("Arial", 14), width=70, bg="#2e2e2e", fg="white", insertbackground="white")
        self.entry.pack()
        self.entry.bind("<KeyRelease>", self.check_typing)  # Detects when a key is released
        
        # Label to display results
        self.result_label = tk.Label(root, text="", font=("Arial", 12), bg="#1e1e1e", fg="lightgray")
        self.result_label.pack()
        
        # Start button
        self.start_button = tk.Button(root, text="Start Test", command=self.start_test, font=("Arial", 12), bg="#4CAF50", fg="white")
        self.start_button.pack(pady=5)
        
        # Reset button
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_test, font=("Arial", 12), bg="#FF9800", fg="white")
        self.reset_button.pack(pady=5)
        
        # Label to display past test history
        self.history_label = tk.Label(root, text="History:", font=("Arial", 12), bg="#1e1e1e", fg="lightgray")
        self.history_label.pack()
        
        # Entry box for custom text input
        self.custom_text_entry = tk.Entry(root, font=("Arial", 12), width=50, bg="#2e2e2e", fg="white", insertbackground="white")
        self.custom_text_entry.pack()
        
        # Button to use custom text
        self.custom_text_button = tk.Button(root, text="Use Custom Text", command=self.use_custom_text, font=("Arial", 12), bg="#2196F3", fg="white")
        self.custom_text_button.pack(pady=5)
    
    def start_test(self):
        # Select a random text from the list
        self.selected_text = random.choice(test_texts)
        self.text_display.config(text=self.selected_text)
        self.entry.delete(0, tk.END)  # Clear previous input
        self.result_label.config(text="")
        self.start_time = time.time()  # Start timing
    
    def check_typing(self, event):
        if not self.start_time:
            return
        
        # Calculate typing speed and accuracy
        end_time = time.time()
        user_input = self.entry.get()
        time_taken = round(end_time - self.start_time, 2)
        
        # Count errors by comparing typed text with given text
        errors = sum(1 for a, b in zip(self.selected_text, user_input) if a != b)
        
        # Calculate words per minute (WPM)
        words_per_minute = round(len(user_input.split()) / (time_taken / 60)) if time_taken > 0 else 0
        
        # Display typing speed and errors
        self.result_label.config(text=f"Speed: {words_per_minute} WPM | Errors: {errors} | Time: {time_taken} sec")
    
    def reset_test(self):
        if self.start_time:
            # Calculate final results before resetting
            end_time = time.time()
            time_taken = round(end_time - self.start_time, 2)
            user_input = self.entry.get()
            words_per_minute = round(len(user_input.split()) / (time_taken / 60)) if time_taken > 0 else 0
            errors = sum(1 for a, b in zip(self.selected_text, user_input) if a != b)
            
            # Store the result in history
            self.history.append(f"WPM: {words_per_minute}, Errors: {errors}, Time: {time_taken}s")
            
            # Display last 5 results
            self.history_label.config(text="History:\n" + "\n".join(self.history[-5:]))
        
        # Reset UI elements
        self.text_display.config(text="")
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.start_time = None
    
    def use_custom_text(self):
        # Get custom text from input box
        custom_text = self.custom_text_entry.get().strip()
        if custom_text:
            self.selected_text = custom_text
            self.text_display.config(text=self.selected_text)
            self.entry.delete(0, tk.END)
            self.result_label.config(text="")
            self.start_time = time.time()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    TypingSpeedTest(root)
    root.mainloop()