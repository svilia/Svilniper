#!/usr/bin/env python3
import typer
from rich.console import Console
from rich.panel import Panel
from svilniper.config import load_config
from svilniper.modules.domain import domain_recon
from svilniper.modules.scan import ip_scan
from svilniper.modules.github import github_osint
from svilniper.utils.banner import show_banner

app = typer.Typer()
console = Console()

@app.callback()
def callback():
    show_banner()

@app.command()
def init():
    """Initialize API keys"""
    from svilniper.config import init_config
    init_config()

@app.command()
def domain(target: str, output: str = None):
    """Run domain reconnaissance"""
    domain_recon(target, output)

@app.command()
def scan(ip: str):
    """Scan IP/Host"""
    ip_scan(ip)

@app.command()
def github(username: str):
    """GitHub OSINT"""
    github_osint(username)

if __name__ == "__main__":
    app()