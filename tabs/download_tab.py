import customtkinter as ctk
import shared
import threading
import requests
from utils import download
class DownloadTab(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.source_list = ctk.CTkTextbox(self, corner_radius=0, height=100)
        self.source_list.pack(fill="x", pady=(0, 10))
        self.source_list.configure(state="disabled")  
        self.populate_sources()
        self.scrollable_frame = ctk.CTkScrollableFrame(self)
        self.scrollable_frame.pack(fill="both", expand=True)
        
        thread_populate = threading.Thread(target=self.populate_os)
        thread_populate.daemon = True
        thread_populate.start()
    
    def populate_sources(self):
        self.source_list.configure(state="normal")
        self.source_list.insert("end", "Source List:\n")
        if hasattr(shared, 'CONFIG_JSON') and "downloads" in shared.CONFIG_JSON:
            for source in shared.CONFIG_JSON["downloads"]:
                self.source_list.insert("end", f"{source}\n")
        else:
            self.source_list.insert("end", "No sources available\n")
        self.source_list.configure(state="disabled")
    
    def add_os(self, name, description, os_id, source_url):
        '''Thank of the help of GPT lol'''
        os_frame = ctk.CTkFrame(self.scrollable_frame)
        os_frame.pack(fill="x", pady=5, padx=5)
        os_frame.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(os_frame, text=name, font=("", 14, "bold")).grid(row=0, column=0, sticky="w", padx=5)
        ctk.CTkLabel(os_frame, text=description).grid(row=1, column=0, sticky="w", padx=5)
        ctk.CTkButton(
            os_frame, 
            text="Download", 
            command=lambda id=os_id, url=source_url: self.download_os(id, url)
        ).grid(row=0, column=1, rowspan=2, padx=5, sticky="e")
    
    def download_os(self, os_id, source_url):
        print(f"Downloading {os_id} from {source_url}")
        X_download_thread = threading.Thread(target=download.download, args=(source_url, True))
        X_download_thread.start()

    def populate_os(self):
        try:
            for i in shared.CONFIG_JSON["downloads"]:
                repo_url = i
                x = requests.get(repo_url+"/source.json")
                if x.status_code == 200:
                    print(x.json())
                    for i in x.json()["repo"]:
                        self.add_os(f"(REPO: {x.json()["repo_name"]}) "+i["name"], i["description"], i["id"], repo_url+"/qcow/"+i["zip_path"])
        except Exception as e:
            print(e)
            pass
            