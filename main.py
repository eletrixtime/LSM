import customtkinter as ctk
from tabs.main_tab import MainTab
from tabs.about_tab import AboutTab
from tabs.download_tab import DownloadTab
import shared 
from CTkMessagebox import CTkMessagebox
import psutil
import os
import traceback
import time
from utils.download import download
from utils.chk_qemu import check_for_qemu
#====

os.makedirs(name="assets",exist_ok=True)
os.makedirs(name="sandbox_images",exist_ok=True)

#=====
print("LSM - Welcome to Linux Sandbox Manager")
print(f"Version : {shared.CONFIG_JSON['version']}")
print("\n")
#download("https://cdn.eletrix.fr/public/static/image.zip",False) not required anymore
if not check_for_qemu():
    msg = CTkMessagebox(
        title="LSM - Missing QEMU",
        message="LSM requires QEMU to work properly.\n\nPlease install it and relaunch LSM.",
        icon=""
    )
    response = msg.get()
    exit()
try:
   
    class Core(ctk.CTk):
        def __init__(self):
            super().__init__()
            self.title(shared.translate("home","tab_title",f"Linux Sandbox Manager (LSM) - V{shared.CONFIG_JSON["version"]}"))
            self.geometry("800x600")
        
            
            self.tabview = ctk.CTkTabview(self)
            self.tabview.pack(fill="both", expand=True, padx=10, pady=10)
            
            self.home_tab = self.tabview.add("Home")
            self.download_tab = self.tabview.add("Download")

            self.about_tab = self.tabview.add("About")

            
            self.maintab_prime = MainTab(self.home_tab) 
            self.download_tab = DownloadTab(self.download_tab)
            self.about_tab = AboutTab(self.about_tab)
    if __name__ == "__main__":
#        0/0
        app = Core()
        app.mainloop()
except Exception as e:
    CRASH_REPORT = f"""
Linux Sandbox Manager Manager has crashed :(

# Error :
{e}

{traceback.format_exc()}
==========================================

# LSM Version

    - {shared.CONFIG_JSON["version"]}

# System Info :
    
    - CPU : {psutil.cpu_count()} @ {psutil.cpu_freq()}
    - Memory : {psutil.virtual_memory()}
    - OS Name : {os.name}
    
# Installed OS

    {os.listdir("sandbox_images")}


Timestamp : {time.time()}
    """
    with open("report.txt","w") as f:
        f.write(CRASH_REPORT)
    msg = CTkMessagebox(
                title="LSM - Has crashed",
                message="Linux Sandbox Manager Manager has crashed: \n\n "+str(e)+ "\n\n\n A crash report has been generated in the LSM directory.",
                icon=""
            )
    response = msg.get()    
