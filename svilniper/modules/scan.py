import subprocess
from rich.console import Console
from svilniper.config import load_config

console = Console()

def ip_scan(ip):
    config = load_config()
    console.print(f"[bold orange]Scanning {ip}...[/bold orange]")
    
    if config.get("shodan"):
        console.print("[yellow]Shodan lookup (mock for demo)...[/yellow]")
    
    try:
        result = subprocess.getoutput(f"nmap -sV -T3 -Pn {ip} --top-ports 100 2>&1 | head -50")
        console.print(result)
    except Exception as e:
        console.print(f"[red]Nmap error: {e}[/red]")