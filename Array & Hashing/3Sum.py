# O (n^2) Time
# O (n) or O(1) time depends on sort

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue
            
            L = i + 1
            R = len(nums) - 1

            while L < R:
                threeSum = a + nums[L] + nums[R]
                if threeSum > 0:
                    R -= 1
                elif threeSum < 0:
                    L += 1
                else:
                    res.append([a, nums[L], nums[R]])
                    L += 1
                    # R -= 1

                    while nums[L] == nums[L - 1] and L < R:
                        L += 1
                
        return res
