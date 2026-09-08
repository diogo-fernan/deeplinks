"""Benign test fixture for MCP install deeplink research.

Pops the platform calculator on run so an MCP install deeplink that
fetches and runs this package (via uvx, pip, npx-python equivalents)
is directly observable. Prints a marker line first so a run that
fails to pop calc (headless CI, unsupported platform) still leaves
evidence in the terminal. Not intended for any other use.
"""

import platform
import subprocess
import sys


MARKER = "deeplink-test-live-marker"


def main() -> int:
    sys.stdout.write(MARKER + "\n")
    sys.stdout.flush()
    system = platform.system()
    if system == "Darwin":
        subprocess.Popen(["open", "-a", "Calculator"])
    elif system == "Windows":
        subprocess.Popen(["cmd.exe", "/c", "start", "calc.exe"])
    else:
        sys.stdout.write(
            "deeplinks: platform %s has no default calc; marker printed only\n" % system
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
