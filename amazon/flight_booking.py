def corpFlightBookings(bookings, n):
    res = [0] * (n + 1)
    for i, j, k in bookings:
        res[i - 1] += k
        res[j] -= k
    for i in range(1, n):
        res[i] += res[i - 1]
    return res[:-1]

if __name__ == '__main__':
    
    # There are n flights that are labeled from 1 to n.

    # You are given an array of flight bookings bookings, where bookings[i] = [firsti, lasti, seatsi] represents a booking for flights firsti through lasti (inclusive) with seatsi seats reserved for each flight in the range.

    # Return an array answer of length n, where answer[i] is the total number of seats reserved for flight i.

    

    # Example 1:

    # Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
    # Output: [10,55,45,25,25]
    # Explanation:
    # Flight labels:        1   2   3   4   5
    # Booking 1 reserved:  10  10
    # Booking 2 reserved:      20  20
    # Booking 3 reserved:      25  25  25  25
    # Total seats:         10  55  45  25  25
    # Hence, answer = [10,55,45,25,25]
    # Example 2:

    # Input: bookings = [[1,2,10],[2,2,15]], n = 2
    # Output: [10,25]
    # Explanation:
    # Flight labels:        1   2
    # Booking 1 reserved:  10  10
    # Booking 2 reserved:      15
    # Total seats:         10  25
    # Hence, answer = [10,25]

    

    # Constraints:

    # 1 <= n <= 2 * 104
    # 1 <= bookings.length <= 2 * 104
    # bookings[i].length == 3
    # 1 <= firsti <= lasti <= n
    # 1 <= seatsi <= 104

    print(corpFlightBookings(bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5))

    # bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5 res= [0,0,0,0,0,0]
    # i,j,k = 1,2,19, res= [10,0,-10,0,0,0]
    # i,j,k = 2,3,20, res= [10,20,-10,-20,0,0]
    # i,j,k = 2,5,25, res= [10,45,-10,-20,-0,-25]

    # [10, 55, 45, 25, 25]

    print(corpFlightBookings(bookings = [[1,2,10],[2,2,15]], n = 2))