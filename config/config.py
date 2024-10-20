# config/config.py

from pathlib import Path

# Define the base directory (the root of your project)
BASE_DIR = Path(__file__).resolve().parent.parent  # Navigates up to the project root

# Define paths for data and other directories
RAW_DATA_PATH = BASE_DIR / 'data' / 'raw'
PROCESSED_DATA_PATH = BASE_DIR / 'data' / 'processed'
NOTEBOOKS_PATH = BASE_DIR / 'notebooks'
SRC_DATA_PATH = BASE_DIR / 'src' / 'data'
SRC_MODELS_PATH = BASE_DIR / 'src' / 'models'
SRC_UTILS_PATH = BASE_DIR / 'src' / 'utils'
TESTS_PATH = BASE_DIR / 'tests'
MODELS_PATH = BASE_DIR / 'models'
SCRIPTS_PATH = BASE_DIR / 'scripts'
WORKFLOWS_PATH = BASE_DIR / '.github' / 'workflows'

# Example function to print paths (for debugging)
def print_paths():
    print("Base Directory:", BASE_DIR)
    print("Raw Data Path:", RAW_DATA_PATH)
    print("Processed Data Path:", PROCESSED_DATA_PATH)
