import json
from datetime import datetime
from rich.console import Console

console = Console()

def save_report(data, output=None):
    if not output:
        output = f"reports/svilniper_{data.get('target', 'report')}_{datetime.now().strftime('%Y%m%d')}.json"
    os.makedirs("reports", exist_ok=True)
    with open(output, "w") as f:
        json.dump(data, f, indent=2, default=str)
    console.print(f"[green]Report saved: {output}[/green]")

import os