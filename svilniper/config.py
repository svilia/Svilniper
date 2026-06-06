import json
import os
from rich.console import Console

console = Console()
CONFIG_FILE = "svilniper_config.json"

def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE) as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)

def init_config():
    config = load_config()
    console.print("[bold orange]Svilniper Config Setup[/bold orange]")
    config["shodan"] = input("Shodan API Key: ").strip()
    config["hunter"] = input("Hunter.io API (optional): ").strip() or ""
    save_config(config)
    console.print("[green]Config saved![/green]")