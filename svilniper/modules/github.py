import requests
from rich.console import Console
from rich.table import Table

console = Console()

def github_osint(username):
    console.print(f"[bold orange]GitHub OSINT for {username}[/bold orange]")
    try:
        r = requests.get(f"https://api.github.com/users/{username}")
        if r.status_code == 200:
            data = r.json()
            table = Table(title="GitHub Profile")
            table.add_column("Key")
            table.add_column("Value")
            for k, v in list(data.items())[:15]:
                table.add_row(str(k), str(v)[:100])
            console.print(table)
        else:
            console.print("[red]User not found[/red]")
    except:
        console.print("[red]GitHub API error[/red]")