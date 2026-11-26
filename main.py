"""Copy the day's news poster into the grader's output directory."""

import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SOURCE, OUTPUT_DIR / "entry.png")
