import tkinter as tk
import customtkinter as ctk

# Window setup
ctk.set_appearance_mode("System")
mainWindow = ctk.CTk()
mainWindow.geometry("1024x768")
mainWindow.title("Hotel Neighbourhood")

# Hotel URL input
urlLabel = ctk.CTkLabel(mainWindow, text="Enter a hotel URL from booking.com:")
urlLabel.pack(padx=20, pady=20)
urlInput = tk.StringVar()
urlEntry = ctk.CTkEntry(mainWindow, width=350, height=40, textvariable=urlInput)
urlEntry.pack()


mainWindow.mainloop()
