# HackDavis 2018
# @Author - Guang(Kevin) Wu, Andersen Huey, Samantha Mark, Rajdeep Singh
# 21 January 2018
#
#Description: This program uses the concept of color detection in order to make judgments about the environment. It
# identifies the general color of grass and combines this data with weather and temperature in order to make
# adequate judgments about more efficiently maintain and sustain a lawn without human involvement.

import weather
from PIL import Image

global red
global green
global blue
global diff

# Takes in an image and an arbitrary temperature and identifies and most frequently identified color in the image
# in RGB form.
def main_color(file, temp, zipcode):
    img = Image.open(file)
    colors = img.getcolors(11111111)
    max_occurence, most_present = 0, 0
    try:
        for c in colors:
            if c[0] > max_occurence:
                (max_occurence, most_present) = c
    except TypeError:
        raise Exception("Image too crowded")

    red = most_present[0]
    green = most_present[1]
    blue = most_present[2]
    diff = abs(green - red)

    print most_present
    print red
    print green
    print blue
    print diff

    need_water(temp, red, green, diff, zipcode)


# Takes in the variables created from main_color and determines whether grass needs to be watered.
def need_water(temp, red, green, diff, zipcode):
    amount = "None needed"
    water = False
    cond = weather.get_sky(zipcode)

    if temp >= 90:
        print "Too hot to water"
    elif temp <= 32:
        print "Too cold for watering"
    elif "rain" in cond or "snow" in cond:
        print "Not optimal weather to water"
    else:
        print "Checking grass condition"
        if red > green and (diff >= 100 or diff <= 20):
            water = True
            if diff <= 20:
                amount = "a lot"
            else:
                amount = "a little"

    print water
    print amount

#Checks main_color and need_water using different images and varying temperatures from different zipcodes.
def check():
    img = ["grass.jpg", "drygrass.jpg", "hddesert.jpg"]
    zips = [65733, 95616, 94133]
    dataw = []
    datat = []

    for z in zips[:]:
        weather.get_weather(z)
        dataw.append(weather.get_sky(z))
        datat.append(weather.get_temp(z))
    print dataw
    print datat

    for z in zips[:]:
        for i in img[:]:
            for t in datat[:]:
                main_color(i, t, z)
