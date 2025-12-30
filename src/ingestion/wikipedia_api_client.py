"""
File to get the data from the api.
"""
import requests
from dotenv import load_dotenv
import yaml 
import os
from importlib.resources import files
from src.common.utils import load_yaml_config

load_dotenv()


def get_data():
    """
    3 devices -> desktop, mobile-web, mobile app
    data year wise collect 
    month wise collect 
    daily wise collect
    hourly wise collect
    """
    url = os.getenv("API_URL")
    config_data = load_yaml_config("ingestion_config.yaml")

    print(config_data)


