class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        neg = []
        pos = []

        # Splitting negative and positive numbers
        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)

        # If no negative numbers, return the smallest positive number
        if not neg:
            return min(pos)

        # If no positive numbers, return the largest negative number
        elif not pos:
            return max(neg)

        # Otherwise, compare closest to zero
        else:
            a = max(neg)  # Largest negative number (closest to 0)
            b = min(pos)  # Smallest positive number (closest to 0)

            # Return the number with the minimum absolute value (prefer larger number in case of tie)
            return abs(a) if (abs(a) == abs(b)) else (b if abs(b) < abs(a) else a)