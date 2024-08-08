import tkinter as tk
from tkinter import messagebox

def show_start_page():
    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()
    
    # Create starting page components
    start_label = tk.Label(root, text="Let's Start the Quiz! 😊", font=("Helvetica", 24), bg="deepskyblue", fg="orange")
    start_label.pack(pady=50)

    yes_button = tk.Button(root, text="Yes", font=("Helvetica", 16), width=10, height=2, bg="lightgreen", fg="black", command=start_quiz)
    yes_button.place(relx=0.4, rely=0.6, anchor=tk.CENTER)
    
    no_button = tk.Button(root, text="No", font=("Helvetica", 16), width=10, height=2, bg="lightcoral", fg="black", command=root.destroy)
    no_button.place(relx=0.6, rely=0.6, anchor=tk.CENTER)

def start_quiz():
    # Clear the starting page
    for widget in root.winfo_children():
        widget.destroy()
    
    # Create quiz components
    global question_text
    global buttons
    global shadow_question_text
    global submit_button
    
    question_text = tk.Text(root, wrap=tk.WORD, font=("Algerian", 18), bg="lightpink", fg="white", height=4, width=50, bd=0, padx=10, pady=10)
    question_text.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    # Create shadow for 3D effect
    shadow_question_text = tk.Text(root, wrap=tk.WORD, font=("Algerian", 18), fg="gray", bg="lightpink", height=4, width=50, bd=0, padx=10, pady=10)
    shadow_question_text.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    buttons = [
        create_3d_button(root, "", lambda: None),
        create_3d_button(root, "", lambda: None),
        create_3d_button(root, "", lambda: None),
        create_3d_button(root, "", lambda: None),
    ]

    # Position the buttons with reduced gap and centered
    button_gap = 5  # Reduced gap between buttons
    for i, btn in enumerate(buttons):
        btn.place(relx=0.5, rely=0.4 + i * (0.07 + button_gap / 600), anchor=tk.CENTER)

    # Create Submit button (hidden initially)
    submit_button = tk.Button(root, text="Submit", font=("Helvetica", 16), width=10, height=2, bg="lightblue", fg="black", command=show_result)
    submit_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
    submit_button.pack_forget()  # Hide it initially
    
    load_question()

def create_3d_button(root, text, command):
    return tk.Button(root, text=text, font=("Helvetica", 14), width=20, height=2,
                     relief="raised", bd=5, bg="lightgrey", fg="black", command=command)

# Initialize the main window
root = tk.Tk()
root.title("Supercar Quiz")
root.geometry("1366x768")  # Adjusted to match the screen resolution

# Set a vibrant background color
root.configure(bg="lightpink")

# Get window width and button width
window_width = 1366  # Width of the window
button_width = 200  # Width of the buttons
x_position = (window_width - button_width) // 2  # Center position for buttons

# Questions for the quiz
questions = [
    {"question": "Which car is known as the fastest production car in the world?", "options": ["Bugatti Chiron", "Hennessey Venom GT", "Koenigsegg Agera RS", "McLaren P1"], "answer": "Koenigsegg Agera RS"},
    {"question": "Which classic car is known for its distinctive gullwing doors?", "options": ["Mercedes-Benz 300SL", "Ferrari 250 GTO", "Jaguar E-Type", "Porsche 356"], "answer": "Mercedes-Benz 300SL"},
    {"question": "What was the top speed of the Ferrari F40 when it was first released?", "options": ["201 mph", "187 mph", "217 mph", "193 mph"], "answer": "201 mph"},
    {"question": "Which vintage supercar was famously known as the 'Bluebird'?", "options": ["Bugatti Type 35", "McLaren F1", "Jaguar XK120", "Napier-Railton"], "answer": "Napier-Railton"},
    {"question": "What was the primary purpose of the Lamborghini Miura when it was first developed?", "options": ["Racing", "Daily Driving", "Luxury", "Track Use"], "answer": "Racing"},
    {"question": "Which vintage supercar is often considered the first 'hypercar'?", "options": ["McLaren P1", "Ferrari LaFerrari", "Porsche 918 Spyder", "Bugatti Veyron"], "answer": "Bugatti Veyron"},
]

current_question = 0
score = 0

# Function to load the current question
def load_question():
    global current_question
    question = questions[current_question]
    
    # Clear the text widgets
    question_text.delete("1.0", tk.END)
    shadow_question_text.delete("1.0", tk.END)
    
    # Insert multi-colored question text
    question_text.insert(tk.END, question["question"], "color1")
    shadow_question_text.insert(tk.END, question["question"], "color2")
    
    # Tag configuration for colorful text
    question_text.tag_configure("color1", foreground="cyan")
    shadow_question_text.tag_configure("color2", foreground="gray")
    
    # Update shadow text after placing the question label
    root.after(100, update_shadow_text)
    
    for i, option in enumerate(question["options"]):
        buttons[i].config(text=option, command=lambda opt=option: check_answer(opt))
    
    # Show or hide the Submit button based on the question
    if current_question == len(questions) - 1:
        submit_button.pack()  # Show the Submit button
    else:
        submit_button.pack_forget()  # Hide the Submit button

def update_shadow_text():
    # Position shadow text slightly offset from the original
    shadow_question_text.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

# Function to check the selected answer
def check_answer(selected_option):
    global current_question, score
    correct_answer = questions[current_question]["answer"]
    
    if selected_option == correct_answer:
        score += 1
        messagebox.showinfo("Correct!", "That's the right answer!")
    else:
        messagebox.showinfo("Incorrect", f"The correct answer was {correct_answer}.")
    
    current_question += 1
    
    if current_question < len(questions):
        load_question()
    else:
        show_result()

# Function to show the final result
def show_result():
    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()
    
    # Show result
    result_label = tk.Label(root, text=f"Your Score: {score}/{len(questions)}", font=("Helvetica", 24), bg="lightpink", fg="black")
    result_label.pack(pady=50)

    close_button = tk.Button(root, text="Close", font=("Helvetica", 16), width=10, height=2, bg="lightcoral", fg="black", command=root.destroy)
    close_button.pack(pady=20)

# Show the starting page
show_start_page()

# Start the Tkinter loop
root.mainloop()