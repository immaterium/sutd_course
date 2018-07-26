def read_stations(f):
    output = {}
    for line in f:
        if '=' in line:
            linename = line.strip().strip('=')
            output[linename] = []
        elif ',' in line:
            try:
                stations = line.split(',')
                for station in stations:
                    output[linename].append(station.strip())
            except:
                raise SyntaxError
    return output

with open('mrt_lines_withnumber.txt', 'rt') as f:
    stations = read_stations(f)
    print(stations)
