# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 17:48:30 2024

@author: ALFRED
"""

class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        # Convert both lists to sets to eliminate duplicates
        set1=set(nums1)
        set2=set(nums2)
        #nums11 unique element
        diff1=list(set1-set2)
        #nums2 unique element
        diff2=list(set2-set1)
        return [diff1,diff2]
