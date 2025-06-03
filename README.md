# 🚀 LSM - Linux Sandbox Manager  

**LSM** (*Linux Sandbox Manager*) is a GUI tool for creating and managing ephemeral virtual machines ("Sandbox Machines"). Perfect for development, testing.  

---

## 🔥 Key Features  
- **Instant VM Creation** – Spin up lightweight, disposable sandboxes in seconds.  
- **Ephemeral by Design** – Machines self-destruct after use (no leftovers).  
- **Secure Isolation** – Run untrusted code or apps in a contained environment.  
- **Minimal Overhead** – Optimized for performance (QEMU-based).  
- **Customizable** – Choose OS images.

---

## 🛠️ Quick Start  

### Prerequisites  
- Linux/Windows (MacOS is not tested) host (with QEMU)  
- `qemu`, `python3` installed  

### Install & Run  
```bash
git clone https://github.com/eletrixtime/lsm.git  
cd lsm  
pip install -r requirements.txt --user
python3 main.py
```


## 🎯 Use Cases  
- **Developers**: Test apps in clean environments.  
- **DevOps**: Rapid prototype infrastructure.  

---

## 🤝 Contribute  
PRs welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.  

**License**: GPLV V3.0  
