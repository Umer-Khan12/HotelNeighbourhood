import customtkinter as ctk

class MainFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # Buttons to choose between Default or ChatGPT mode
        self.default_btn = ctk.CTkButton(parent, text="Default Mode", command=controller.switch_frame_to_default)
        self.default_btn.grid(row=0, column=0, padx=20, pady=20)
        self.cgpt_btn = ctk.CTkButton(parent, text="ChatGPT Mode", command=controller.switch_frame_to_cgpt)
        self.cgpt_btn.grid(row=0, column=1, padx=20, pady=20)


class DefaultFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.test_label = ctk.CTkLabel(parent, text="This is the Default window")
        self.test_label.grid(padx=20, pady=20)

        # Hotel URL input
        self.url_lbl = ctk.CTkLabel(parent, text="Enter a hotel URL from booking.com:")
        self.url_lbl.grid(padx=20, pady=20)
        self.url_input = ctk.StringVar()
        self.url_entry = ctk.CTkEntry(parent, width=350, height=40, textvariable=self.url_input)
        self.url_entry.grid()


class ChatGPTFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.test_label = ctk.CTkLabel(parent, text="This is the ChatGPT window")
        self.test_label.grid(padx=20, pady=20)

        # Hotel URL input
        self.url_lbl = ctk.CTkLabel(parent, text="Enter a hotel URL from booking.com:")
        self.url_lbl.grid(padx=20, pady=20)
        self.url_input = ctk.StringVar()
        self.url_entry = ctk.CTkEntry(parent, width=350, height=40, textvariable=self.url_input)
        self.url_entry.grid()


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Root window settings
        ctk.set_appearance_mode("System")
        self.geometry("1024x768")
        self.title("Hotel Neighbourhood")

        # Controller to stack frames on
        container = ctk.CTkFrame(self)
        container.grid(row=0, column=0, sticky="nsew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Setting up the different frames in the program
        # Main window = 0, Default Mode window = 1, ChatGPT Mode window = 2
        self.frame_list = []
        self.frame_list.append(MainFrame(container, self))
        self.frame_list.append(DefaultFrame(container, self))
        self.frame_list.append(ChatGPTFrame(container, self))
        self.frame_list[0].grid(row=0, column=0, sticky="nsew")
        self.frame_list[1].grid(row=0, column=0, sticky="nsew")
        self.frame_list[2].grid(row=0, column=0, sticky="nsew")
        self.frame_list[0].tkraise()

    def switch_frame_to_default(self):
        self.frame_list[0].forget()
        self.frame_list[1].tkraise()
        print("Default button clicked")

    def switch_frame_to_cgpt(self):
        self.frame_list[0].forget()
        self.frame_list[2].tkraise()
        print("CGPT button clicked")


if __name__ == "__main__":
    app = App()
    app.mainloop()
