# Author Name: Naimuddin Mohammad
# Ariticle Analysis chatbot GUI

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import textwrap

class ArticleAnalyzer(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("Article Analyzer")
        self.geometry("1200x800")
        
        # Configure grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Variables
        self.chat_history = []
        
        # Create main frames
        self.create_header()
        self.create_article_frame()
        self.create_chat_frame()

    def create_header(self):
        # Header frame
        header_frame = ctk.CTkFrame(self)
        header_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 0), sticky="ew")
        
        # Title
        title_label = ctk.CTkLabel(
            header_frame, 
            text="Article Analyzer", 
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title_label.pack(side="left", padx=10, pady=10)
        
        # Reset button
        reset_button = ctk.CTkButton(
            header_frame,
            text="Reset All",
            command=self.reset_all,
            width=100
        )
        reset_button.pack(side="right", padx=10, pady=10)

    def create_article_frame(self):
        # Article frame
        article_frame = ctk.CTkFrame(self)
        article_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        
        # Article label
        article_label = ctk.CTkLabel(
            article_frame,
            text="Paste your article here:",
            font=ctk.CTkFont(size=16)
        )
        article_label.pack(padx=10, pady=5, anchor="w")
        
        # Article text area
        self.article_text = ctk.CTkTextbox(article_frame, wrap="word")
        self.article_text.pack(fill="both", expand=True, padx=10, pady=5)

    def create_chat_frame(self):
        # Chat frame
        chat_frame = ctk.CTkFrame(self)
        chat_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        
        # Chat history
        self.chat_box = ctk.CTkTextbox(chat_frame, wrap="word")
        self.chat_box.pack(fill="both", expand=True, padx=10, pady=5)
        self.chat_box.configure(state="disabled")
        
        # Input frame
        input_frame = ctk.CTkFrame(chat_frame)
        input_frame.pack(fill="x", padx=10, pady=5)
        
        # Question entry
        self.question_entry = ctk.CTkEntry(
            input_frame,
            placeholder_text="Type your question here..."
        )
        self.question_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))
        
        # Send button
        send_button = ctk.CTkButton(
            input_frame,
            text="Send",
            command=self.send_question,
            width=100
        )
        send_button.pack(side="right")
        
        # Bind Enter key to send
        self.question_entry.bind("<Return>", lambda event: self.send_question())

    def send_question(self):
        question = self.question_entry.get().strip()
        if not question:
            return
            
        article_text = self.article_text.get("1.0", tk.END).strip()
        if not article_text:
            messagebox.showwarning("Warning", "Please paste an article first!")
            return
            
        # Add question to chat history
        self.chat_box.configure(state="normal")
        self.chat_box.insert(tk.END, f"\nYou: {question}\n")
        
        # Simulate response (replace this with actual processing logic)
        response = self.process_question(question, article_text)
        self.chat_box.insert(tk.END, f"Assistant: {response}\n")
        
        self.chat_box.configure(state="disabled")
        self.chat_box.see(tk.END)
        
        # Clear question entry
        self.question_entry.delete(0, tk.END)

    def process_question(self, question, article):
        # This is a placeholder for the actual processing logic
        # You can integrate any text processing or AI model here
        return f"This is a simulated response to your question about the article. You asked: {question}"

    def reset_all(self):
        # Clear article
        self.article_text.delete("1.0", tk.END)
        
        # Clear chat history
        self.chat_box.configure(state="normal")
        self.chat_box.delete("1.0", tk.END)
        self.chat_box.configure(state="disabled")
        
        # Clear question entry
        self.question_entry.delete(0, tk.END)

def main():
    app = ArticleAnalyzer()
    app.mainloop()

if __name__ == "__main__":
    main()