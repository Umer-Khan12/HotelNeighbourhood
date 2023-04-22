import customtkinter as ctk

class MainFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.grid(row=0, column=0, sticky="news")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

        # Buttons to choose between Default or ChatGPT mode
        self.default_btn = ctk.CTkButton(self, text="Default Mode", command=controller.switch_frame_to_default)
        self.default_btn.grid(row=1, column=0, padx=20, pady=20)
        self.cgpt_btn = ctk.CTkButton(self, text="ChatGPT Mode", command=controller.switch_frame_to_cgpt)
        self.cgpt_btn.grid(row=1, column=1, padx=20, pady=20)


class DefaultFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.grid(row=0, column=0, sticky="news")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)

        self.test_label = ctk.CTkLabel(self, text="Default Mode")
        self.test_label.grid(row=0, column=0, padx=20, pady=20)

        # Create a back button in the centre of the frame by adding in empty grid spaces in between
        self.back_btn = ctk.CTkButton(self, text="Back", command=controller.switch_frame_to_main)
        self.back_btn.grid(row=3, column=0, padx=20, pady=20)

        # Hotel URL input
        self.url_lbl = ctk.CTkLabel(self, text="Enter a hotel URL from booking.com:")
        self.url_lbl.grid(row=1, column=0, padx=20, pady=20)
        self.url_input = ctk.StringVar()
        self.url_entry = ctk.CTkEntry(self, width=350, height=40, textvariable=self.url_input)
        self.url_entry.grid(row=2, column=0)


class ChatGPTFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.grid(row=0, column=0, sticky="news")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)

        self.test_label = ctk.CTkLabel(self, text="ChatGPT Mode")
        self.test_label.grid(row=0, column=0, padx=20, pady=20)

        self.back_btn = ctk.CTkButton(self, text="Back", command=controller.switch_frame_to_main)
        self.back_btn.grid(row=3, column=0, padx=20, pady=20, sticky="s")

        # Hotel URL input
        self.url_lbl = ctk.CTkLabel(self, text="Enter a hotel URL from booking.com:")
        self.url_lbl.grid(row=1, column=0, padx=20, pady=20)
        self.url_input = ctk.StringVar()
        self.url_entry = ctk.CTkEntry(self, width=350, height=40, textvariable=self.url_input)
        self.url_entry.grid(row=2, column=0)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Root window settings
        ctk.set_appearance_mode("System")
        self.geometry("1024x768")
        self.title("Hotel Neighbourhood")

        # Controller to stack frames on

        container = ctk.CTkFrame(self)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.grid(row=0, column=0, sticky="news")

        # Setting up the different frames in the program
        # Main window = 0, Default Mode window = 1, ChatGPT Mode window = 2
        self.frame_list = []
        self.frame_list.append(MainFrame(container, self))
        self.frame_list.append(DefaultFrame(container, self))
        self.frame_list.append(ChatGPTFrame(container, self))
        self.frame_list[0].tkraise()

    def switch_frame_to_default(self):
        self.frame_list[0].forget()
        self.frame_list[1].tkraise()

    def switch_frame_to_cgpt(self):
        self.frame_list[0].forget()
        self.frame_list[2].tkraise()

    def switch_frame_to_main(self):
        self.frame_list[1].forget()
        self.frame_list[2].forget()
        self.frame_list[0].tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()
