def read_stations(f):
    output = {}
    for line in f:
        if '=' in line:
            linename = line.strip().strip('=')
            output[linename] = []
        elif ',' in line:
            stations = line.split(',')
            for station in stations:
                output[linename].append(station.strip()) 
    return output

with open('mrt_lines.txt', 'rt') as f:
    stations = read_stations(f)
    print(stations)