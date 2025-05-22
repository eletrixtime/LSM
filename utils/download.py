from CTkMessagebox import CTkMessagebox

def download(url,force):
    import os
    import requests
    import zipfile
    import math


    if not os.path.exists("sandbox_images") or not os.listdir("sandbox_images") or force == True:
        print("Downloading ZIP please wait...")
        msg = CTkMessagebox(
            title="LSM - Downloading Images",
            message="Please click 'Ok' to continue and download a large amount of GB (you can see the progress in the terminal)",
            icon=""
        )
        response = msg.get()    
                
        response = requests.get(url, stream=True)
        response.raise_for_status()  
        total_size = int(response.headers.get('content-length', 0))
        downloaded = 0
        block_size = 8192
        
        with open("temp.zip", "wb") as f:
            for chunk in response.iter_content(chunk_size=block_size):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    percent = math.floor(downloaded / total_size * 100)
                    bar_length = 20
                    filled_length = math.floor(bar_length * downloaded / total_size)
                    bar = '=' * filled_length + '>' + ' ' * (bar_length - filled_length - 1)
                    print(f"\r[{bar}] {percent}% ({downloaded}/{total_size} bytes)", end='', flush=True)
        
        print("\nExtracting files...")
        with zipfile.ZipFile("temp.zip", 'r') as zip_ref:
            file_list = zip_ref.namelist()
            total_files = len(file_list)
            for i, file in enumerate(file_list, 1):
                zip_ref.extract(file, "sandbox_images")
                print(f"\rExtracting: {i}/{total_files} files", end='', flush=True)
        
        print("\nCleaning up...")
        os.remove("temp.zip")
        print("Finished !")
        return True
