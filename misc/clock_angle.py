def angleClock(hour,minutes):
    one_min_angle = 6
    one_hour_angle = 30
    
    minutes_angle = one_min_angle * minutes
    hour_angle = (hour % 12 + minutes / 60) * one_hour_angle
    
    diff = abs(hour_angle - minutes_angle)
    return min(diff, 360 - diff)

if __name__ == '__main__':

    # time and space: O(1)

    # Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.

    print(angleClock(hour = 12, minutes = 30))

