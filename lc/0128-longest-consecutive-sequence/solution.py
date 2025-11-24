class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_seq = 0
        nums_hashset = set(nums)
        for num in nums_hashset:
            if num - 1 not in nums_hashset:
                curr_seq = 1
                curr_num = num + 1
                while curr_num in nums_hashset:
                    curr_seq += 1
                    curr_num += 1
                
                longest_seq = max(longest_seq, curr_seq)
        return longest_seq
                    

