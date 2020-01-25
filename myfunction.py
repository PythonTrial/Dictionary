def minutes_to_hours(minutes):
    hours = minutes / 60
    return hours


def seconds_to_hours(seconds):
    hours = seconds / 3600
    return hours

def __minutes_to_hours__(minutes, seconds):
    hours = (minutes / 60) + (seconds / 3600)
    return hours

print (minutes_to_hours(70))
print (__minutes_to_hours__(70,260))
