import tkinter as tk
import keyboard
import threading
import time

class AutoTyperGUI:
    IMAGE_PATH = r"C:\Users\Nabelll\Desktop\VSCODEPROJECTS\AutoTyper\cartoontree.png"
    SLEEP_TIME = 0.085
    TEXT_PLACEHOLDER = "Enter Text Here"

    def __init__(self):
        self.root = tk.Tk()
        self.root.config(bg="#4B8B3B")
        self.root.geometry("700x450")
        self.root.title("AutoTyper - By: Nabeel-AR")

        # create the GUI
        self.create_gui()

        self.root.mainloop()

    def create_gui(self):
        self.create_image_labels()
        self.create_main_label()
        self.create_text_box()
        self.create_start_button()
        self.create_restart_button()
        self.creat_quit_button()

    def create_image_labels(self):
        self.tree_img = tk.PhotoImage(file=self.IMAGE_PATH).subsample(18, 18)
        tk.Label(self.root, image=self.tree_img, bg="#4B8B3B").place(anchor="se", relx=1, rely=1)
        tk.Label(self.root, image=self.tree_img, bg="#4B8B3B").place(anchor="sw", relx=0, rely=1)

    def create_main_label(self):
        tk.Label(self.root, text="AutoTyper", font=("Times New Roman", 20, "underline"), bg="white").pack(pady=20)

    def create_text_box(self):
        # create the text box for entering the text to be typed
        self.text_box = tk.Text(self.root, height=7, font=("Times New Roman", 12))
        self.text_box.pack(padx=10, pady=10)
        self.text_box.insert("7.0", self.TEXT_PLACEHOLDER)
        self.text_box.config(fg="#666")
        self.text_box.bind("<1>", self.clear_text)

    def create_start_button(self):
        tk.Button(self.root, text="Start", font=("Times New Roman", 15), bg="white", command=self.start_typing).pack(
            padx=100, pady=5)
        
    def create_restart_button(self):
        tk.Button(self.root, text="Restart", font=("Times New Roman", 15), bg="white", command=self.restart_app).pack(pady= 3)

    def creat_quit_button(self):
        tk.Button(self.root, text="Quit", font=("Times New Roman", 15), bg="white", command=self.quit_app).pack(pady= 3)

    def start_typing(self):
        if self.is_valid_text():
            threading.Thread(target=self.type).start()

    def type(self):
        # method for typing the text
        text_value = self.text_box.get("1.0", "end-1c")
        for i, char in enumerate(text_value):
            keyboard.write(char)
            time.sleep(self.SLEEP_TIME)

    def is_valid_text(self):
        # check if the text entered is valid
        text_value = self.text_box.get("1.0", "end-1c")
        if not text_value or text_value == self.TEXT_PLACEHOLDER:
            return False
        return True

    def clear_text(self, event):
        # method to clear text box when first clicked on to get rid of placeholder text
        if self.text_box.get("1.0", "end-1c") == self.TEXT_PLACEHOLDER:
            self.text_box.delete("1.0", "end")
            self.text_box.config(fg="#080808")

    def restart_app(self):
        self.root.destroy()
        AutoTyperGUI()

    def quit_app(self):
        self.root.quit()
    
AutoTyperGUI()
