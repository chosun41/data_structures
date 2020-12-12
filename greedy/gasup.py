import collections

MPG=20

def find_ample_city(gallons, distances):

    remaining_gallons = 0
    CityAndRemainingGas = collections.namedtuple('CityAndRemainingGas',
                                                 ('city', 'remaining_gallons'))
    city_remaining_gallons_pair = CityAndRemainingGas(0, 0)
    num_cities = len(gallons)
    for i in range(1, num_cities):
        remaining_gallons += gallons[i - 1] - distances[i - 1] // MPG
        if remaining_gallons < city_remaining_gallons_pair.remaining_gallons:
            city_remaining_gallons_pair = CityAndRemainingGas(i, remaining_gallons)
    return city_remaining_gallons_pair.city

if __name__ == '__main__':
    
    # time: O(n), space: O(1)
    # find a city from which you can fill up and travel to each without running out of gas
    # basically find the city from which you'll have the most gas left over after going to next city
    print(find_ample_city([50,20,5,30,25,10,10],[900,600,200,400,600,200,100]))
    
    # gallons left - [5,-10,-5,10,-5,0,5]