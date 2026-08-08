class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        divisions = 0
        positive = True

        if dividend < 0 and divisor < 0:
            dividend = -dividend
            divisor = -divisor
        elif dividend < 0:
            dividend = -dividend
            positive = False
        elif divisor < 0:
            divisor = -divisor
            positive = False
        
        while True:
            k = 0
            while (divisor << k) <= dividend:
                k +=1
            
            if k:
                divisions +=  1 << k-1
                dividend -= (divisor << k-1)
            else:
                break
                # handle the case where dividend == divisor and divisor > dividend

        while not ((dividend - divisor) < 0):
            dividend -= divisor
            divisions += 1
        
        if positive:
            if divisions > (1 << 31) - 1:
                return (1 << 31) - 1
            else:
                return divisions
        else:
            if -divisions < -(1 << 31):
                return -(1 << 31)
            else:
                return -divisions
        
       