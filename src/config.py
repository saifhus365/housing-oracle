"""
Central configuration — paths, model names, API keys (via env vars),
chunking parameters, retrieval settings, etc.
"""

from pathlib import Path

# ── Project paths ──────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
TEXT_DATA_DIR = DATA_DIR / "text"
CSV_DATA_DIR = DATA_DIR / "csv"
RAW_DATA_DIR = DATA_DIR / "raw"
