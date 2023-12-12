from rich import print as rprint
from rich.panel import Panel

def hello():
    rprint(Panel("Hello, [red]World!"))

def goodbye():
    rprint(Panel("Goodbye!"))