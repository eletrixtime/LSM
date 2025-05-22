def check_for_qemu():
    import os
    import subprocess

    try:
        subprocess.run(["qemu-system-x86_64", "-version"], capture_output=True, text=True)
        return True
    except:
        return False