class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        negative = (dividend < 0) != (divisor < 0)
        
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0
        multiple = 1
        
        while (divisor << 1) <= dividend:
            divisor <<= 1
            multiple <<= 1
        
        while multiple:
            if divisor <= dividend:
                dividend -= divisor
                quotient += multiple

            divisor >>= 1
            multiple >>= 1
        
        if negative:
            quotient = -quotient
            
        if quotient > (1 << 31) - 1:
            return (1 << 31) - 1

        elif quotient < -(1 << 31):
            return -(1 << 31)

        else:
            return quotient
        
       