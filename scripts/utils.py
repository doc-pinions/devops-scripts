# utils.py

import os
import re
import json
import logging
from datetime import datetime
from typing import Dict, List, Any

def load_config(filename: str) -> Dict[str, Any]:
    """Load configuration from JSON file."""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error(f"Config file '{filename}' not found.")
        return {}

def validate_email(email: str) -> bool:
    """Validate email address."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def get_current_date() -> str:
    """Get current date in YYYY-MM-DD format."""
    return datetime.now().strftime('%Y-%m-%d')

def list_files(directory: str, extension: str) -> List[str]:
    """List files in directory with specified extension."""
    return [f for f in os.listdir(directory) if f.endswith(extension)]

def get_logger(name: str) -> logging.Logger:
    """Get logger instance."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger

def save_data(data: Dict[str, Any], filename: str) -> None:
    """Save data to JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)