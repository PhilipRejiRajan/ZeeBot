import json
import tkinter as tk
import tkinter.font as tkfont
from tkinter import scrolledtext, simpledialog
from difflib import get_close_matches

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]

def send_message():
    user_input = user_entry.get().strip()
    if not user_input:
        return

    chat_display.insert(tk.END, f"You: {user_input}\n")
    user_entry.delete(0, tk.END)

    best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

    if best_match:
        answer: str = get_answer_for_question(best_match, knowledge_base)
        chat_display.insert(tk.END, f"ZeeBot: {answer}\n")
    else:
        chat_display.insert(tk.END, "ZeeBot: I don't know the answer. Can you teach me?\n")
        new_answer = tk.simpledialog.askstring("Teach ZeeBot","Type the answer or press Cancel to skip:")

        if new_answer:
            knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
            save_knowledge_base('knowledge_base.json', knowledge_base)
            chat_display.insert(tk.END, "ZeeBot: Thank you! I learned a new response!\n")


knowledge_base: dict = load_knowledge_base("knowledge_base.json")

root = tk.Tk()
root.title("ZeeBot")
root.geometry("1000x700")
root.configure(bg="#1F1F1F")

custom_font1 = tkfont.Font(family="Cascadia Mono", size=14, weight="bold")

chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
chat_display.pack(pady=30)
chat_display.configure(font=custom_font1)
chat_display.configure(bg="#0C0C0C", fg="#1EF113")

user_entry = tk.Entry(root, width=50)
user_entry.pack(pady=10)
user_entry.configure(font=custom_font1)
user_entry.configure(bg="#0C0C0C", fg="#1EF113")
user_entry.configure(insertbackground="#1EF113")
user_entry.bind("<Return>", lambda event: send_button.invoke())

send_button = tk.Button(root, text="Ask ZeeBot", command=send_message)
send_button.pack(pady=5)
send_button.configure(font=(custom_font1), relief="raised", padx=10, pady=5)
send_button.configure(bg="#C6C6C6", fg="#0C0C0C", activebackground="#1EF113")

root.mainloop()