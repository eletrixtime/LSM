import customtkinter as ctk
from PIL import Image
from tkinter import filedialog
import os
import shared

class AboutTab(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs) 
        self.pack(fill="both", expand=True, padx=10, pady=10)  
        
        # Logo
        self.logo_image = ctk.CTkImage(
            dark_image=Image.open("assets/images/logo.png"),
            light_image=Image.open("assets/images/logo.png"),
            size=(300, 300)
        )
        self.logo_label = ctk.CTkLabel(self, image=self.logo_image, text="")
        self.logo_label.pack(pady=20)

# ===================================================
        self.credit_text = ctk.CTkLabel(
            self, 
            text=f"Linux Sandbox (Manager) is a tool for creating temporary virtual machines.\nYou can run dangerous applications in a safe environment. \n \n Made with 💖 in the Baguette Country!\n\n\n Version : {shared.CONFIG_JSON['version']}",  
            text_color=("black", "white"), 
            font=("Arial", 12),  
            wraplength=400  
        )
        self.credit_text.pack(pady=10, padx=10, fill="x") 
