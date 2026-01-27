"""
File to get the data from the api.
"""
import requests # type: ignore
from dotenv import load_dotenv # type: ignore
import os
from src.common.utils import load_yaml_config
from datetime import datetime, timedelta, date

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

def get_data(_from, _to):
    """
    3 devices -> desktop, mobile-web, mobile app
    data year wise collect 
    month wise collect 
    daily wise collect
    hourly wise collect
    """
    url = os.getenv("API_URL")

    if (url is None):
        return 
    
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

    desktop_url = url + f"/{desktop_config['project']}/{desktop_config['access']}/{desktop_config['agent']}/{desktop_config['granularity']}/{_from}/{_to}"
    mobile_web_url = url + f"/{mobile_web_config['project']}/{mobile_web_config['access']}/{mobile_web_config['agent']}/{mobile_web_config['granularity']}/{_from}/{_to}"
    mobile_app_url = url + f"/{mobile_app_config['project']}/{mobile_app_config['access']}/{mobile_app_config['agent']}/{mobile_app_config['granularity']}/{_from}/{_to}"
    
    data = {
        "desktop": get_from_api(desktop_url),
        "mobile_web": get_from_api(mobile_web_url),
        "mobile_app": get_from_api(mobile_app_url),
    }
    
    return data
    

def check_for_completeness(dataframe, engine):
    """
    check_for_completeness
    check the daily average data in the weekly data
    to do, it requires dataframe and engine (spark) 
    returs just a report, 
    it is not responsible for any further decisions
    """

    
    



