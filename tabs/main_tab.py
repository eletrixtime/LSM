import customtkinter as ctk
from tkinter import filedialog
import os
import subprocess
from CTkMessagebox import CTkMessagebox
import shared
import json

class MainTab(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs) 
        self.pack(fill="both", expand=True)  
        
        self.OS_QCOW = None

        self.info_text = ctk.CTkLabel(self,text="Welcome to Linux Sandbox Manager")
        self.info_text.pack(pady=30)
        self.dropdown_var = ctk.StringVar(value="Select a OS")
        
        self.dropdown_options = [f for f in os.listdir("os_imgs") if f.endswith(('.qcow','.qcow2'))]        
     
        self.dropdown = ctk.CTkOptionMenu(
            self,
            variable=self.dropdown_var,
            values=self.dropdown_options,
            command=self.on_dropdown_select
        )
        
        self.dropdown.configure(
            fg_color="#2b2b2b",          
            button_color="#3b3b3b",      
            button_hover_color="#4b4b4b",
            text_color="white",           
            dropdown_fg_color="#2b2b2b",  
            dropdown_text_color="white",   
            dropdown_hover_color="#3b3b3b",
            font=("Arial", 12)            
        )
        
        self.dropdown.pack(pady=10)

        # OPTIONS 

        self.checkbox_run_in_temp_mode = ctk.CTkCheckBox(
            self,
            text="Run in temporary mode",
            variable=ctk.BooleanVar(value=True),
            command=self.checkbox_run_in_temp_mode_func
        )

        self.checkbox_run_in_temp_mode.pack(pady=10)

        self.launch_button = ctk.CTkButton(self, text=shared.translate("home","launch_sandbox","Launch Sandbox!"), command=self.launch_sandbox)
        self.launch_button.pack(pady=20)
        
    
    def on_dropdown_select(self, choice):
        self.OS_QCOW = os.path.join("os_imgs", choice)
        tmp_json = json.loads(open(self.OS_QCOW +".json","r").read())
        self.info_text.configure(text="Welcome to Linux Sandbox Manager \n-------\n\n Selected OS : \n"+tmp_json["text"]+"\n\n Login :\n"+f"Username: {tmp_json["login"]["username"]}\nPassword: {tmp_json["login"]["password"]}")

    def checkbox_run_in_temp_mode_func(self):  

            if self.checkbox_run_in_temp_mode.get():
                shared.TEMP_MODE = True
            else:
                msg = CTkMessagebox(
                title="Disabling Temporary Mode",
                message="This will disable the temporary mode\n\n In other words : Modyfing the OS will be permanent\n \n Are you sure ?",
                option_1="NO",
                option_2="YES",
                icon="question"
            )
            
                response = msg.get()    
                if response == "YES":
                    shared.TEMP_MODE = False
                else:
                    self.checkbox_run_in_temp_mode.select()
                    shared.TEMP_MODE = True
                    return
                
    def launch_sandbox(self):
        print("[LSM/Manager] Launching OS :", self.OS_QCOW)
        print("[LSM/Manager] Temporary mode :", shared.TEMP_MODE)
        
        drive_options = ",if=virtio,snapshot=on" if shared.TEMP_MODE else ",if=virtio"
        
        command_exec = (
            f"qemu-system-x86_64 -m {shared.CONFIG_JSON["vm"]["memory"]} -smp {shared.CONFIG_JSON["vm"]["cpu_core"]} -cpu qemu64 "
            f"-drive file={self.OS_QCOW},format=qcow2{drive_options} "
            "-boot d -net nic,model=virtio -net user -vga virtio "
            "-usb -device usb-tablet"
            
        )
        
        print(command_exec)
        process = subprocess.Popen(command_exec, shell=True)
        def kill_sandbox():
            msg = CTkMessagebox(
                title="Killing Sandbox",
                message="This will end the session.",
                option_1="NO",
                option_2="YES",
                icon="question"
            )
            
            response = msg.get()
            if response == "YES":
                import psutil
                for proc in psutil.process_iter(['name']):
                    if 'qemu' in proc.info['name'].lower():
                        proc.kill()
                print("[LSM/Manager] Sandbox killed")
                # make the button normal again
                self.launch_button.configure(
                    state="normal", 
                    text=shared.translate("home", "launch_sandbox", "Launch Sandbox!"),
                    command=self.launch_sandbox
                )
            else:
                pass

        self.launch_button.configure(
            state="normal", 
            text=shared.translate("home", "launching_sandbox", "Kill Sandbox"),
            command=kill_sandbox
        )
    