import logging
import json
import pandas as pd
from datetime import datetime

def setup_logging(level='INFO'):
    logging.basicConfig(
        level=getattr(logging, level),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(__name__)

def save_results(results, filename):
    results['exported_at'] = datetime.now().isoformat()
    with open(filename, 'w') as f:
        json.dump(results, f, indent=2)

def load_config(config_path):
    with open(config_path, 'r') as f:
        return json.load(f)