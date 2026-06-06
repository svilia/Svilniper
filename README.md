# Svilniper v1.0.0

Svilniper is a modern, high-performance, modular reconnaissance and intelligence-gathering framework inspired by the automated footprinting capabilities of Sn1per. Built specifically for security auditors, penetration testers, and open-source intelligence (OSINT) analysts, Svilniper delivers an automated offensive workflow encapsulated within a high-contrast Black & Orange terminal user interface.

Operating entirely on an asynchronous execution architecture, Svilniper orchestrates parallel lookups, network scans, and data mining operations across target domains, network infrastructures, and cloud repositories to consolidate disparate threat intelligence metrics into structured, actionable matrices.

---

## Key Features

* **High-Speed Domain Enumeration:** Aggregates passive DNS footprints, historical records, subdomains, and target structures utilizing robust OSINT scraping pipelines.
* **Infrastructure Intelligence:** Integrates deep network layer asset scanning, port state verification, and advanced metadata harvesting through targeted external APIs.
* **GitHub Behavioral Analysis:** Scrapes targeted organization and user repositories dynamically to parse access structures, public signatures, and operational patterns.
* **Rich Terminal UI Pipeline:** Utilizes an immersive, high-contrast black and orange visual interface powered by `Rich` for absolute data clarity, responsive progress indicators, and precise tables.
* **Extensible Architecture:** Designed with a clean object-oriented decoupling of data generation, verification pipelines, and routing modules to allow effortless injection of custom tools.

---

## Directory Layout

The framework adheres to an industry-standard Python packaging blueprint, ensuring a robust and clean workspace separation between modules:

```text
svilniper/
├── .github/
│   └── workflows/
│       └── publish.yml          # Automated CI/CD PyPI release engine
├── assets/
│   └── banner.png               # Project branding asset
├── data/
│   ├── signatures.json          # Pattern database for active identification
│   └── templates/
│       └── report_clean.json    # Standard structure schema for internal exports
├── docs/
│   └── ARCHITECTURE.md          # System flow and data pipeline specifications
├── logs/
│   └── .gitkeep                 # Persistent runtime log workspace tracking
├── output/
│   └── .gitkeep                 # Output directory for generated reconnaissance reports
├── src/
│   └── svilniper/
│       ├── __init__.py          # Base package declaration and core metadata
│       ├── cli.py               # Main Typer execution pipeline and command routers
│       ├── config.py            # Local configurations, API credentials, and constants
│       ├── exceptions.py        # Project-specific fallback routines and error handlers
│       ├── api/
│       │   ├── __init__.py      # External integration package container
│       │   ├── github_client.py # REST client pipeline for dynamic GitHub scraping
│       │   ├── shodan_client.py # Infrastructure exposure manager via Shodan APIs
│       │   └── whois_client.py  # Wrapper mapping active python-whois objects
│       ├── core/
│       │   ├── __init__.py      # Core intelligence controller engine
│       │   ├── engine.py        # Central multi-threaded processing & analysis logic
│       │   └── validator.py     # Schema sanity verification and string formatting
│       └── ui/
│           ├── __init__.py      # Terminal formatting ecosystem wrapper
│           ├── display.py       # Layout grids, custom text tables, and block renders
│           └── themes.py        # Strict Black & Orange color palettes
├── tests/
│   ├── __init__.py              # Automation testing suite declarations
│   ├── test_cli.py              # Functional testing rules for argument parsing
│   └── test_core.py             # Unit testing matrices for internal logic engines
├── LICENSE                      # MIT License agreement
├── MANIFEST.in                  # Packaging manifest for structural releases
├── README.md                    # Core operational manual and developer index
├── pyproject.toml               # Modern build isolation configuration and dependencies
└── setup.py                     # Legacy compatibility wrapper linking setup tools
Prerequisites & DependenciesSvilniper relies entirely on native Python 3 execution frameworks paired with production-tested open-source modules designed for asynchronous data processing:DependencyMinimum VersionOperational Domain within FrameworkPython>= 3.8Core Interpreter & Execution EnvironmentTyper[all]>= 0.9.0Command Line Interface compilation, autocompletion, and validationRich>= 13.0Layout execution, color mapping, live rendering grids, and loading indicatorsRequests>= 2.0Synchronous REST API transportation and session routingShodan>= 1.0Hardware asset classification, exposed service mapping, and deep vulnerability indexingPython-Whois>= 0.8Autonomous registrar analysis, legal record indexing, and epoch state trackingInstallation & InitializationFollow the structural instructions below to provision a clean deployment environment for Svilniper.1. Clone the RepositoryBashgit clone [https://github.com/svilia/svilniper.git](https://github.com/svilia/svilniper.git)
cd svilniper
2. Set Up a Virtual Environment (Recommended)To protect host-level operating system modules from dependency drift, execute the sequence within an isolated Python environment:Bashpython3 -m venv venv

# For Linux / MacOS architectures:
source venv/bin/activate

# For Windows command line architectures (Command Prompt):
# venv\Scripts\activate.bat

# For Windows PowerShell execution environments:
# .\venv\Scripts\Activate.ps1
3. Install in Editable ModeDeploy the application in development state to dynamically link local source changes directly to your active execution engine:Bashpip install -e .
4. Initialize the FrameworkBashsvilniper init
Operational ConfigurationUpon running svilniper init, the tool establishes a runtime context configuration file. To unleash the full capabilities of external intelligence collection, populate your authorization metrics inside the environment configurations:Python# Location: src/svilniper/config.py

SVILNIPER_THEME_PRIMARY = "#FF8C00"  # Rich Deep Dark Orange Color Value
SVILNIPER_THEME_DARK    = "#1A1A1A"  # Dark High-Contrast Workspace Palette

# Threat Intelligence Token Pools
SHODAN_API_KEY = "YOUR_PRODUCTION_SHODAN_API_TOKEN_HERE"
GITHUB_TOKEN   = "YOUR_PERSONAL_GITHUB_ACCESS_TOKEN_HERE"

# Core Operational Throttle Defaults
DEFAULT_NETWORK_TIMEOUT = 12.0
MAX_CONCURRENT_THREADS  = 25
Usage & Command ReferenceSvilniper exposes a structured command syntax with automated type verification and contextual terminal hints built directly into the core terminal console.Global Help CommandBashsvilniper --help
1. Workspace InitializationGenerates default configuration files, verifies host pipeline parameters, and sets up internal workspace routing paths.Bashsvilniper init
2. Domain Infrastructure FootprintingLaunches a deep targeted intelligence footprint analysis against a domain infrastructure name, parsing WHOIS registration tables, chronological lifecycle paths, and peripheral data markers.Bashsvilniper domain google.com
3. Network Exposure ScanningRoutes structured inquiries directly against the Shodan Threat Intelligence grid, processing open port vectors, protocol fingerprints, operating system configurations, and physical geo-location data points.Bashsvilniper scan 8.8.8.8
4. GitHub OSINT MiningInitiates active metadata mining routines targeting the public GitHub repository platform to flag user profiles, organizational footprints, contribution patterns, and structural code markers.Bashsvilniper github user:elonmusk
Operational WorkflowsTo accurately demonstrate the internal automation sequence and conditional logic handling built into Svilniper, refer to the step-by-step procedural workflows detailed below.Domain Intel Gathering PipelineSanitization Check: The user input string passes through the validation library to strip extraneous protocols (http://, https://) or trailing path characters via regex filters.WHOIS Target Dispatch: The engine builds a wrapper object via whois_client.py and establishes an outbound port connection to root domain registries.Chronological Timeline Structuring: Raw date strings returned from registries are captured, transformed into ISO-standard datetime stamps, and converted into an ongoing operational lifecycle model.UI Layout Matrix Construction: The parsed elements are passed directly to the display controller, which binds the variables into high-contrast tables using the official black and orange UI rules before rendering to standard output.Plaintext[ User Input ] -> ( validator.py ) -> [ Clean Domain Name ]
                                             |
                   +-------------------------+-------------------------+
                   |                                                   |
         ( whois_client.py )                                 ( Passive DNS Lookups )
                   |                                                   |
          [ Raw Registry Data ]                               [ Mapping Record Arrays ]
                   |                                                   |
                   +-------------------------+-------------------------+
                                             |
                                    ( core/engine.py )
                                             |
                                    [ Structured Model ]
                                             |
                                     ( ui/display.py )
                                             |
                                   ====== TERMINAL ======
                                   Orange/Black UI Render
                                   ======================
Code Implementation BlueprintsBelow are reference-grade architecture blueprints demonstrating how the core files within Svilniper communicate to parse data sets and generate the visual layout interface.Core Entry Router: cli.pyPythonimport typer
from rich.console import Console
from svilniper.core.engine import IntelligenceEngine
from svilniper.ui.display import RenderFactory

app = typer.Typer(help="Svilniper: Modern Black & Orange Recon Framework Engine")
console = Console()

@app.command()
def init():
    """Initialize local environments and build out baseline configurations."""
    console.print("[bold #FF8C00][*][/bold #FF8C00] [white]Initializing workspace environments...[/white]")
    # System folder structure and workspace setup routines execute here
    console.print("[bold green][+][/bold green] [white]Workspace generated successfully.[/white]")

@app.command()
def domain(target: str = typer.Argument(..., help="The explicit target domain string to audit")):
    """Audit domain infrastructure footprints, lifecycle dates, and DNS routing."""
    engine = IntelligenceEngine()
    with console.status("[bold #FF8C00]Executing deep query modules...[/bold #FF8C00]"):
        results = engine.execute_domain_pipeline(target)
    RenderFactory.render_domain_table(results)

if __name__ == "__main__":
    app()
Intelligence Engine: engine.pyPythonimport whois
from svilniper.exceptions import TargetResolutionError

class IntelligenceEngine:
    def __init__(self):
        self.active_state = True

    def execute_domain_pipeline(self, domain_str: str) -> dict:
        try:
            raw_whois = whois.whois(domain_str)
            if not raw_whois.domain_name:
                raise TargetResolutionError("Registry returned an empty identity response mapping")
            
            processed_payload = {
                "identity": domain_str.lower(),
                "registrar": raw_whois.registrar or "Unknown Authority",
                "creation_epoch": str(raw_whois.creation_date),
                "expiration_epoch": str(raw_whois.expiration_date),
                "name_servers": raw_whois.name_servers or []
            }
            return processed_payload
        except Exception as e:
            raise TargetResolutionError(f"Pipeline execution engine stalled during collection: {str(e)}")
Troubleshooting & Diagnostics1. External Asset Resolution TimeoutsSymptom: Terminal transitions into an infinite wait block or triggers a network execution timeout error during heavy lookups.Resolution Check: Ensure your underlying system environment has functional DNS routes. Increase the total permissible operational wait time within the system variables:Bashexport SVILNIPER_DEFAULT_TIMEOUT=30.0
2. PyPI Build Packaging DiscrepanciesSymptom: Modifying standard file systems or adding static source files does not correctly cascade into active application paths during runtime tests.Resolution Check: Force a complete cache purging sequence and re-link the setup tools environment to rebuild the internal symbol reference mappings:Bashpip uninstall svilniper -y
rm -rf *.egg-info build/ dist/
pip install -e .
Open Source LicensingThis project is open-source software licensed under the terms of the MIT License.The framework architecture permits complete freedom regarding integration adaptation, commercial packaging distributions, and remote system usage, provided that the original copyright notice and permission notice are included in all copies or substantial portions of the software.Contact & Team InformationFor active framework bug submissions, module contribution setups, vulnerability disclosures, or community engineering syncs, contact the infrastructure development core across the following official channels:Lead Engineering Support: sviliadestek@gmail.comHCKTeam Operations Command: sviliahckteam@gmail.comSecure Operational Telegram: @Lmfao1ys
