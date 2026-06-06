from rich.console import Console
from pyfiglet import figlet_format

console = Console()

def show_banner():
    console.print(figlet_format("SVILNIPER", font="slant"), style="bold orange")
    console.print("Modern Recon Tool | Black & Orange Theme | v1.2.0\n", style="dim")