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

HEADERS = {
   "User-Agent": "MyWikiStatsBot/1.0"
}

def get_from_api(url, timeout=10):
    try:
        response = requests.get(url, timeout=timeout, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        raise RuntimeError("API Request timed out")
    except requests.exceptions.HTTPError as e:
        raise RuntimeError(f"HTTP Error: {e}")
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Request failed: {e}")

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

    desktop_config = {
        "project": config_data['project'][0],
        "access": config_data['access'][1],
        "agent": config_data['agent'][0],
        "granularity": config_data['granularity'][0]
    }

    mobile_web_config = {
        "project": config_data['project'][0],
        "access": config_data['access'][2],
        "agent": config_data['agent'][0],
        "granularity": config_data['granularity'][0]
    }
    
    mobile_app_config = {
        "project": config_data['project'][0],
        "access": config_data['access'][3],
        "agent": config_data['agent'][0],
        "granularity": config_data['granularity'][0]
    }

    start = "2023010100"
    end = "2023010112"


    desktop_url = url + f"/{desktop_config['project']}/{desktop_config['access']}/{desktop_config['agent']}/{desktop_config['granularity']}/{start}/{end}"
    mobile_web_url = url + f"/{mobile_web_config['project']}/{mobile_web_config['access']}/{mobile_web_config['agent']}/{mobile_web_config['granularity']}/{start}/{end}"
    mobile_app_url = url + f"/{mobile_app_config['project']}/{mobile_app_config['access']}/{mobile_app_config['agent']}/{mobile_app_config['granularity']}/{start}/{end}"
    
    data = {
        "desktop": get_from_api(desktop_url),
        "mobile_web": get_from_api(mobile_web_url),
        "mobile_app": get_from_api(mobile_app_url),
    }
    
    return data


