#!/usr/bin/env python3
"""Generate static blog article HTML pages (no React/Babel)."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATIC = ROOT / "scripts" / "generate-blog-static.py"

if __name__ == "__main__":
    subprocess.run([sys.executable, str(STATIC)], check=True)
