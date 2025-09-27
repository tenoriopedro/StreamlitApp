import os
import dotenv
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = PROJECT_ROOT / "dotenv_files/.env"
dotenv.load_dotenv(ENV_FILE)


def get_url_api():
    env_file = os.environ['API_URL']
    return env_file
