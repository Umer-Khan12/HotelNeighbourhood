import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Root window settings
        ctk.set_appearance_mode("System")
        self.geometry("1024x768")
        self.title("Hotel Neighbourhood")

        # Hotel URL input
        self.url_lbl = ctk.CTkLabel(self, text="Enter a hotel URL from booking.com:")
        self.url_lbl.pack(padx=20, pady=20)
        self.url_input = ctk.StringVar()
        self.url_entry = ctk.CTkEntry(self, width=350, height=40, textvariable=self.url_input)
        self.url_entry.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
