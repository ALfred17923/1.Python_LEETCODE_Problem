# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 17:49:16 2024

@author: ALFRED
"""

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        v=[]
        i=0
        while i<len(arr):
            count=1
            while i+1 <len(arr) and arr[i]==arr[i+1]:
                count+=1
                i=i+1
            v.append(count)
            i+=1
        v.sort()
        for i in range (1,len(v)):
            if v[i]==v[i-1]:
                return False
        return True
        