import customtkinter as ctk

class DefaultFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.test_label = ctk.CTkLabel(self, text="This is the Default window")
        self.test_label.pack(padx=20, pady=20)

        # Hotel URL input
        self.url_lbl = ctk.CTkLabel(self, text="Enter a hotel URL from booking.com:")
        self.url_lbl.pack(padx=20, pady=20)
        self.url_input = ctk.StringVar()
        self.url_entry = ctk.CTkEntry(self, width=350, height=40, textvariable=self.url_input)
        self.url_entry.pack()


class ChatGPTFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.test_label = ctk.CTkLabel(self, text="This is the ChatGPT window")
        self.test_label.pack(padx=20, pady=20)

        # Hotel URL input
        self.url_lbl = ctk.CTkLabel(self, text="Enter a hotel URL from booking.com:")
        self.url_lbl.pack(padx=20, pady=20)
        self.url_input = ctk.StringVar()
        self.url_entry = ctk.CTkEntry(self, width=350, height=40, textvariable=self.url_input)
        self.url_entry.pack()


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Root window settings
        ctk.set_appearance_mode("System")
        self.geometry("1024x768")
        self.title("Hotel Neighbourhood")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # Buttons to choose between Default or ChatGPT mode
        self.default_btn = ctk.CTkButton(self, text="Default Mode", command=self.switch_frame_to_default())
        self.default_btn.grid(row=0, column=0, padx=20, pady=20)
        self.cgpt_btn = ctk.CTkButton(self, text="ChatGPT Mode", command=self.switch_frame_to_cgpt())
        self.cgpt_btn.grid(row=0, column=1, padx=20, pady=20)

    def switch_frame_to_default(self):
        pass

    def switch_frame_to_cgpt(self):
        pass




if __name__ == "__main__":
    app = App()
    app.mainloop()
