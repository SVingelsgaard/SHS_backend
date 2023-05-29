from datetime import datetime
from .models import BusTime, TimeValue

def create_bus_time(location, destination, bus_number, time_values):
    pass
    bus_time = BusTime.objects.create(location=location, destination=destination, bus_number=bus_number)# Create the BusTime instance

    # Create TimeValue instances for each time value
    for time_str in time_values:
        time_value = TimeValue.objects.create(time=time_str)
        bus_time.times.add(time_value)

    return bus_time

def run_scrape():
    #bustime = create_bus_time('some_location', 'some_destination', 2, ['22.10','22.11'])
    return {'location':'Ladeveien', 'destination':'Lund via Lade-Sentrum-Kolstad', 'bus_number':2, 'times':'22.10'}
