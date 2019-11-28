import requests
import tle2czml


if __name__=='__main__':
    all_stations = 'stations.tle'
    iss_tle = 'iss.tle'
    iss_czml = 'iss.czml'
    stations_tle = 'https://celestrak.com/NORAD/elements/stations.txt'
    r = requests.get(stations_tle)
    # This is getting the curent TLE for ALL space stations.
    fp = open(all_stations,'w')
    fp.write(r.text)
    fp.close()
    fn = open(all_stations,'r')
    # We only need the ISS values, which happen to be the first three lines
    line_0 = fn.readline()
    line_1 = fn.readline()
    line_2 = fn.readline()
    fp = open(iss_tle,'w')
    fp.writelines(line_0)
    fp.writelines(line_1)
    fp.writelines(line_2)
    fn.close()
    fp.close()
    # For Cesium, we need to work with czml files. Luckily, there's already a conversion program for that!
    # see https://github.com/kujosHeist/tle2czml
    # install with pip install tle2czml
    tle2czml.create_czml(iss_tle,outputfile_path='/var/www/apache/website/data/' + iss_czml)
