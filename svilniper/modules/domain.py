import requests
import subprocess
import json
from rich.console import Console
from rich.progress import Progress
from rich.table import Table
from datetime import datetime
from svilniper.utils.helpers import save_report

console = Console()

def domain_recon(target, output=None):
    console.print(f"[bold orange]Starting recon on {target}...[/bold orange]")
    
    results = {
        "target": target,
        "time": datetime.now().isoformat(),
        "subdomains": [],
        "whois": "",
        "shodan": None
    }
    
    with Progress() as progress:
        task = progress.add_task("[orange]Enumerating...", total=4)
        
        # Subdomains
        try:
            r = requests.get(f"https://crt.sh/?q=%25.{target}&output=json", timeout=15)
            if r.status_code == 200:
                data = r.json()
                subs = list(set(e["name_value"].splitlines()[0] for e in data[:100]))
                results["subdomains"] = subs[:50]
                console.print(f"[green]Found {len(subs)} subdomains[/green]")
        except:
            console.print("[yellow]Subdomain enum failed[/yellow]")
        progress.update(task, advance=1)
        
        # WHOIS
        try:
            whois = subprocess.getoutput(f"whois {target} | head -30")
            results["whois"] = whois
        except:
            pass
        progress.update(task, advance=1)
    
    save_report(results, output)
    console.print("[bold green]Domain recon completed![/bold green]")