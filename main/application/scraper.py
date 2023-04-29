import threading

def run_scraper():
    print("ree")

    # Schedule the next execution after a specific time interval
    interval = 10  # Interval in seconds (e.g., 1 hour)
    threading.Timer(interval, run_scraper).start()