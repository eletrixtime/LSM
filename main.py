import customtkinter as ctk
from tabs.main_tab import MainTab
from tabs.about_tab import AboutTab
import shared 
from CTkMessagebox import CTkMessagebox
import psutil
import os
import traceback
import time
#====

os.makedirs(name="assets",exist_ok=True)
os.makedirs(name="os_imgs",exist_ok=True)

#=====
def download():
    import os
    import requests
    import zipfile
    if not os.path.exists("os_imgs") or not os.listdir("os_imgs"):
        print("Downloading ZIP of build-in images please wait...")
        
        response = requests.get("https://cdn.eletrix.fr/public/static/image.zip", stream=True)
        response.raise_for_status()  
        with open("temp.zip", "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        
        with zipfile.ZipFile("temp.zip", 'r') as zip_ref:
            zip_ref.extractall("os_imgs")
        
        os.remove("temp.zip")
        print("Download and extraction completed successfully! \n Launching app!")
download()
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

    {os.listdir("os_imgs")}


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
