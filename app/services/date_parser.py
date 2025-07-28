from datetime import datetime

def parse_datetime(dt_str: str):
    if dt_str:
        # Remove the 'Z' and convert to datetime
        return datetime.fromisoformat(dt_str.replace("Z", "+00:00"))
    return None