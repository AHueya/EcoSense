import urllib2
import json

def get_weather(zip):
    zipc = str(zip)
    f = urllib2.urlopen('http://api.wunderground.com/api/c0881649b5f98a3e/geolookup/conditions/q/IA/'+zipc+'.json')
    json_string = f.read()
    parsed_json = json.loads(json_string)
    location = parsed_json['location']['city']
    temp_f = parsed_json['current_observation']['temp_f']
    sky = parsed_json['current_observation']['weather']
    f.close()

    print("The weather for " + location + ":")
    print(temp_f)
    print(sky)


def get_temp(zip):
    zipc = str(zip)
    f = urllib2.urlopen('http://api.wunderground.com/api/c0881649b5f98a3e/geolookup/conditions/q/IA/'+zipc+'.json')
    json_string = f.read()
    parsed_json = json.loads(json_string)
    temp_f = parsed_json['current_observation']['temp_f']
    f.close
    return temp_f

def get_sky(zip):
    zipc = str(zip)
    f = urllib2.urlopen('http://api.wunderground.com/api/c0881649b5f98a3e/geolookup/conditions/q/IA/'+zipc+'.json')
    json_string = f.read()
    parsed_json = json.loads(json_string)
    sky = parsed_json['current_observation']['weather']
    f.close
    return sky
