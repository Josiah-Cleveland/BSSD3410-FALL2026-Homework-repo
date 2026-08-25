# Josiah Cleveland
# Homework 1.2
# BSSD 3410 (Applied Algorithms & Architecture)
# 24 August 2026
#
# We will use an API to look up 2 addresses and get their lat & long
# coordinates. Then we'll adapt a formula from the internet to our
# code so that we can calculate the unobstructed (as-the-crow-flies)
# distance between the 2 locations
#
# 1) Combine distance code with selection sort algorithm
# 2) Programmatically find the distance between the NMHU in Las Vegas and 5
#    other locations of your choosing. Save those locations in a
#    list, and sort the list from shortest to longest using
#    selection sort
# 3) Print the names from the sorted list


#===============================================================
#run this in terminal to add 'requests' package to virtual environment: pip install requests

import requests
import math

#===============================================================
def selection_sort(array):
    '''
    the algorithm used for sorting distances from shortest to longest
    '''
    # step 1: loop from the beginning of the array to the second to last item
    currentIndex = 0
    while (currentIndex < len(array) - 1):
        # step 2: save a copy of the currentIndex
        minIndex = currentIndex
        # step 3: loop through all indexes that proceed the currentIndex
        i = currentIndex + 1
        while (i < len(array)):
            # step 4:   if the value of the index of the current loop is less
            #           than the value of the item at minIndex, update minIndex
            #           with the new lowest value index
            if (array[i] < array[minIndex]):
                # update minIndex with the new lowest value index
                minIndex = i
            i += 1
        # step 5: if minIndex has been updated, swap the values at minIndex and currentIndex
        if (minIndex != currentIndex):
            temp = array[currentIndex]
            array[currentIndex] = array[minIndex]
            array[minIndex] = temp
        currentIndex += 1

#===============================================================
# variable with URL string to use with GET request with an API
URL_PATH = 'https://nominatim.openstreetmap.org/search'
def get_lat_lon(location):
    '''
    function to take string argument with a 'unique name' or 'physical address'
    '''
    # dictionary used for optional parameter in upcoming GET request
    PARAMS = {'q': location, 'format': 'jsonv2'}
    # dictionary used for optional parameter in upcoming GET request
    headers = {
        'User-Agent': 'DistanceCalc/1.0'
    }
    # 'requests' package allows us to use GET method
    # 'url=' parameter is required
    r = requests.get(url=URL_PATH, params=PARAMS, headers=headers)
    # extract data from response object & parse JSON data
    data = r.json()
    # print(data)

    # access first object index with 'data[0]' & use 'lat' key to access latitude value
    latitude = float(data[0]['lat'])
    # access first object index with 'data[0]' & use 'lon' key to access longitude value
    longitude = float(data[0]['lon'])
    # print(latitude, longitude)
    return [latitude, longitude]
#end def get_lat_lon(location);

#===============================================================
def calculate_distance(orig, dest):
    '''
    function used to calculate the distance between two points on a map using
    latitude and longitude coordinates. The Haversine Formula is used to accomplish this
    '''
    # access second float after using 'get_lat_lon()'
    dlon = dest[1] - orig[1]
    # access first float after using 'get_lat_lon()'
    dlat = dest[0] - orig[0]
    a = (math.sin(math.radians(dlat/2))) ** 2 + \
         math.cos(math.radians(orig[0])) * \
         math.cos(math.radians(dest[0])) * \
        (math.sin(math.radians(dlon/2))) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    R = 3961 # radius of the Earth in miles
    d = R * c
    return d
#end def calulate_distance(orig, dest):

#===============================================================
def main():
    place1 = 'New Mexico Highlands University'
    place2 = 'New Mexico Museum of Natural History & Science'
    place3 = 'Brook Haven Park East'
    place4 = ['201 E Jefferson St, Phoenix, Arizona 85004', 'Mortgage Matchup Center']
    place5 = ['1400 S Milton Rd, Flagstaff, AZ 86001', 'The Habit Burger & Grill']
    place6 = 'Pikes Peak Center'
    place7 = ['609 Gillis St, Jacksonville, FL 32212', 'Freedom Lanes Bowling & Entertainment Center']

    # return latitude & longitude floats
    loc1 = get_lat_lon(place1)
    loc2 = get_lat_lon(place2)
    loc3 = get_lat_lon(place3)
    loc4 = get_lat_lon(place4[0])
    loc5 = get_lat_lon(place5[0])
    loc6 = get_lat_lon(place6)
    loc7 = get_lat_lon(place7[0])

    # return distances in miles
    dist1 = calculate_distance(loc1, loc2)
    dist2 = calculate_distance(loc1, loc3)
    dist3 = calculate_distance(loc1, loc4)
    dist4 = calculate_distance(loc1, loc5)
    dist5 = calculate_distance(loc1, loc6)
    dist6 = calculate_distance(loc1, loc7)

    # a list of tuples
    distances = [
        (dist1, place2),
        (dist2, place3),
        (dist3, place4[1]),
        (dist4, place5[1]),
        (dist5, place6),
        (dist6, place7[1])
    ]
    # print(distances)

    print('UNSORTED LIST:')
    for obj in distances:
        print(f'{obj[1]} is ~{round(obj[0])} miles away from NMHU main campus')

    selection_sort(distances)

    print('\nSORTED LIST FROM CLOSEST TO FURTHEST:')
    for obj in distances:
        print(round(obj[0]), obj[1])
#end def main():

#===============================================================
if __name__ == '__main__':
    main()