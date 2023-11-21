import tkinter as tk
import time

class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        self.passage_label = tk.Label(root, text="Type the following:")
        self.passage_label.pack(pady=10)

        self.passage_text = "The quick brown fox jumps over the lazy dog."
        self.passage_display = tk.Label(root, text=self.passage_text, wraplength=400)
        self.passage_display.pack(pady=10)

        self.entry_label = tk.Label(root, text="Your typing:")
        self.entry_label.pack(pady=10)

        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)

        self.start_button = tk.Button(root, text="Start Typing Test", command=self.start_test)
        self.start_button.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

        self.start_time = 0

    def start_test(self):
        self.start_time = time.time()
        self.start_button.config(state=tk.DISABLED)
        self.entry.bind("<KeyRelease>", self.check_typing)

    def check_typing(self, event):
        typed_text = self.entry.get()
        if typed_text == self.passage_text:
            elapsed_time = time.time() - self.start_time
            words_per_minute = int((len(self.passage_text.split()) / elapsed_time) * 60)
            self.result_label.config(text=f"Your typing speed: {words_per_minute} words per minute")
            self.start_button.config(state=tk.NORMAL)
            self.entry.unbind("<KeyRelease>")
        else:
            self.result_label.config(text="Keep typing...")

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()
