def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    dividend1, divisor1 = abs(dividend), abs(divisor)
    quotient = 0
    while dividend1 >= divisor1:
        temp, i = divisor1, 1
        while dividend1 >= temp:
            dividend1 -= temp
            temp += temp
            quotient += i
            i += i
    if (dividend < 0) is (divisor < 0):
        quotient = -quotient
    return min(max(quotient, -pow(2,31)),pow(2,31)-1)

if __name__ == '__main__':
    # time: O(logn) because of doubling
    # space: O(1)
    # divide without multiplication, modulo, and division
    # just subtract
    # double in size, two while loops, ^ for quotient
    print(divide(12,2))
    # temp=2,i=1,dividend1=12,dividend1=10,temp=4,quotient=1,i=2
    # temp=4,i=2,dividend1=10,dividend1=6,temp=8,quotient=3,i=4
    # temp=8,i=4,dividend1=6,temp=2,i=1,dividend1=4,temp=4,quotient=4,i=2
    # temp=4,i=2,dividend1=4,dividend1=0,temp=8,quotient=6,i=4