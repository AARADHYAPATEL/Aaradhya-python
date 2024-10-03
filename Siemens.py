from datetime import timedelta, datetime


def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")


print(arrival_time("Orbit", hours=0.13))
