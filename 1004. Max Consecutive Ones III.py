# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 20:56:56 2024

@author: ALFRED
"""

class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        zero_count=0
        max_one=0
        start=0
        for i in range(len(nums)):
            if nums[i]==0:
                zero_count+=1
            while zero_count>k:
                if nums[start]==0:
                    zero_count-=1
                start+=1
            max_one = max(max_one,i-start+1)
        return max_one
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
sol=Solution()
print(sol.longestOnes(nums,k))