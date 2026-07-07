from dotenv import load_dotenv
load_dotenv()

from src.app import create_app

app = create_app()