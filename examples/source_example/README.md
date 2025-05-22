# Custom Repository Guide

## Creating a Custom Repo

1. **Copy the template folder**  
   Start by duplicating the `source_example` folder as your base.

2. **Customize the configuration**  
   Edit the `source.json` file to customize it.

### Testing Your Repo
To test your repository locally, run this command (replace `[YOUR PORT]` with your preferred port number):
```bash
python -m http.server [YOUR PORT]
```

---

## Adding Sandbox Images

### Preparation
1. Package your files:
   - The QCOW2 image file
   - Its corresponding JSON configuration file  
   *(See the `examples` folder for reference formats)*
   
2. Compress these files into a `.zip` archive

### Installation
1. Place the `.zip` file in the `qcow` directory
2. Add an entry to `source.json` following this format:
```json
{
    "name": "example",
    "description": "description here",
    "zip_path": "qcow/filename.zip",
    "id": 2  // IMPORTANT: Ensure each ID is unique
}
```

That's all you need to do!

