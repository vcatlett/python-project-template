import argparse
from pathlib import Path
from typing import List, Union

import IPython
from traitlets.config import Config

from PythonProject import __version__
from PythonProject.shell.messages import *

DEFAULT_PROFILE = "PythonProject"
DEFAULT_COLORS = "LightBG"


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Dysh interactive shell.\n\n All CLI arguments other than those defined below are passed through "
            "to ipython; see $ ipython --help for more details"
        )
    )
    parser.add_argument("paths", help="FITS file paths to load initially", nargs="*", type=Path)
    parser.add_argument("-p", "--profile", help="The IPython profile to use", default=DEFAULT_PROFILE)
    parser.add_argument("-L", "--fits-loader", help="The SDFITS loader class name to use", default="GBTFITSLoad")
    parser.add_argument(
        "--colors",
        help="Set the color scheme",
        choices=["NoColor", "Neutral", "Linux", "LightBG"],
        default=DEFAULT_COLORS,
    )
    return parser.parse_known_args()


def init_shell(*ipython_args, colors=DEFAULT_COLORS, profile: Union[str, Path] = "DEFAULT_PROFILE"):
    c = Config()
    import numpy as np
    import pandas as pd
    from astropy.io import fits
    from astropy.table import Table

    user_ns = {"pd": pd, "np": np, "Table": Table, "fits": fits}
    
    c.BaseIPythonApplication.profile = profile
    c.InteractiveShell.colors = colors
    hello()
    IPython.start_ipython(ipython_args, config=c, user_ns=user_ns)

def main():
    args, remaining_args = parse_args()
    init_shell(*remaining_args, colors=args.colors, profile=args.profile)
    goodbye()


if __name__ == "__main__":
    main()