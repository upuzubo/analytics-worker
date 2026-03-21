# utils.py
import logging
import os
import json
from datetime import datetime, timedelta
import pytz

def get_utc_now():
    return datetime.now(pytz.UTC)

def get_utc_time(delta=timedelta(minutes=0)):
    return get_utc_now() + delta

def log_event(context, level=logging.INFO, **kwargs):
    logger = logging.getLogger('analytics-worker')
    log_message = json.dumps(context)
    logger.log(level, log_message, **kwargs)

def get_config():
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"Failed to load config file: {e}")
        raise

def get_analytics_config():
    config = get_config()
    return config.get('analytics', {})

def get_cache_expiration():
    config = get_config()
    return config.get('cache_expiration', 60)