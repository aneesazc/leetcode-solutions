# O (n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # Initialize a dictionary to store the frequency of each element in nums.

        # Create a list of empty lists for frequencies, with length one more than the list nums.
        freq = [[] for i in range(len(nums) + 1)] 

        # Count the frequency of each element in nums.
        for n in nums:
            count[n] = 1 + count.get(n, 0)  # Increment the count for each occurrence of n.

        # Group numbers in nums by their frequency.
        for n, c in count.items():
            freq[c].append(n)  # Append the number n to its corresponding frequency list in freq.

        res = []  # Initialize the result list to store the top k frequent elements.
        # Iterate over the frequency list in reverse order to start with the most frequent.
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:  # Iterate over elements in the current frequency list.
                res.append(n)  # Add the element to the result list.
                if len(res) == k:  # If the result list has k elements, return it.
                    return res
