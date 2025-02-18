import tkinter as tk
from tkinter import messagebox
import sys
import time
from threading import Thread, Event

# Global stop event to interrupt code execution
stop_event = Event()

# Function to execute code in a separate thread
def execute_code():
    code = text_widget.get("1.0", "end-1c")  # Get the code from the text widget
    output_text.delete("1.0", "end")  # Clear the previous output
    output_text.insert("1.0", "Running...\n")  # Show that code is running
    stop_event.clear()  # Reset the stop event (in case of previous run)

    def execute():
        try:
            # Redirecting the output to the output text widget
            sys.stdout = TextRedirector(output_text)
            sys.stderr = TextRedirector(output_text)

            # Run the code
            exec_with_stop(code)

        except Exception as e:
            output_text.insert("end", f"Error: {e}\n")
            sys.stdout = sys.__stdout__  # Reset stdout back to default

    # Create a separate thread for executing code to prevent GUI freeze
    thread = Thread(target=execute)
    thread.start()

# Function to execute code with stop checking
def exec_with_stop(code):
    # Execute code in a controlled manner to check the stop flag
    local_vars = {}
    try:
        exec(code, {}, local_vars)
        # Check periodically if stop is triggered
        for _ in range(1000):  # Modify this for finer granularity
            if stop_event.is_set():
                output_text.insert("end", "\nExecution stopped by user.\n")
                return
            time.sleep(0.01)  # Avoid blocking the UI too long during checks
    except Exception as e:
        output_text.insert("end", f"Error: {e}\n")
        sys.stdout = sys.__stdout__  # Reset stdout back to default

# Class to redirect output to text widget
class TextRedirector:
    def __init__(self, widget):
        self.widget = widget

    def write(self, string):
        self.widget.insert("end", string)
        self.widget.yview("end")  # Auto-scroll to the bottom

    def flush(self):
        pass  # Necessary for compatibility with file-like objects

# Function to stop code execution
def stop_execution():
    stop_event.set()  # Set the stop event, signaling to interrupt the code execution
    output_text.insert("end", "\nStopping execution...\n")

# Function to safely interrupt infinite code
def on_closing():
    messagebox.showwarning("Warning", "Cannot execute infinite loop code.")
    root.quit()

# Create the main window
root = tk.Tk()
root.title("Python Code Executor")

# Create a text widget for code input
text_widget = tk.Text(root, height=10, width=40)
text_widget.pack(pady=10)

# Create an output text widget to display execution results
output_text = tk.Text(root, height=10, width=40)
output_text.pack(pady=10)

# Create an execute button
execute_button = tk.Button(root, text="Execute Code", command=execute_code)
execute_button.pack(pady=5)

# Create a stop button
stop_button = tk.Button(root, text="Stop Execution", command=stop_execution)
stop_button.pack(pady=5)

# Set up the event loop for closing the window
root.protocol("WM_DELETE_WINDOW", on_closing)

# Start the Tkinter event loop
root.mainloop()
