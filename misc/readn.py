class Solution:
    def __init__(self):
        self.temp, self.start, self.num = [""] * 4, 0, -1

    def read(self, buf, n, idx=0):
        while n > 0:
            while self.start < self.num and n:
                buf[idx] = self.temp[self.start]
                idx, self.start, n = idx + 1, self.start + 1, n - 1
            if not n: 
                break
            self.num, self.start = read4(self.temp), 0 # 4,0
            if not self.num: 
                break
        return idx # return number of characters read, else 0 if nomore from buffer

if __name__=='__main__':

    # The API read4 reads four consecutive characters from file, then writes those characters into the buffer array buf4.

    # The return value is the number of actual characters read.

    # By using the read4 method, implement the method read that reads n characters from file and store it in the buffer array buf. Consider that you cannot manipulate file directly.

    # The return value is the number of actual characters read.

    # Consider that you cannot manipulate the file directly. The file is only accessible for read4 but not for read.
    # The read function may be called multiple times.
    # Please remember to RESET your class variables declared in Solution, as static/class variables are persisted across multiple test cases. Please see here for more details.
    # You may assume the destination buffer array, buf, is guaranteed to have enough space for storing n characters.
    # It is guaranteed that in a given test case the same buffer buf is called by read.

    buf = "abc";
    sol = Solution()
    sol.read(buf, 1); # After calling your read method, buf should contain "a". We read a total of 1 character from the file, so return 1.
    sol.read(buf, 2); # Now buf should contain "bc". We read a total of 2 characters from the file, so return 2.
    sol.read(buf, 1); # We have reached the end of file, no more characters can be read. So return 0.
