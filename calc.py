speed_of_light = 299792458 #m / s
nanosecond_conversion_factior = 1/1000000000


def latency_distance ( latency ): #latency in seconds
    return latency * speed_of_light #latency_distance in meters

print( latency_distance(1) / 1000 ) #in km - for a lightbulb
print( latency_distance(0.4 * nanosecond_conversion_factior) ) #for a CPU Register
print( latency_distance(12 * nanosecond_conversion_factior) ) #DRAM
print(latency_distance(7 /1000)/1000) #in km - HD
