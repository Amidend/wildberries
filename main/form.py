import customtkinter as ctk


class MainForm(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        self.geometry("700x500")
        self.title("Основное окно")

        self.testBtn = ctk.CTkButton(self, text="Привет мир!", command=lambda: print("Я ЧМО!"))
        self.testEntry = ctk.CTkEntry(self, placeholder_text="ВВЕДИ В МЕНЯ ПОЛНОСТЬЮ")
        self. paste_elements()

        self.mainloop()

    def paste_elements(self):
        self.testBtn.pack(side="top")
        self.testEntry.pack(side="top")



if __name__ == "__main__":
    MainForm()