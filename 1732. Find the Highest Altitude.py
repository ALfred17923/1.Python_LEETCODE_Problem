# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 10:37:55 2024

@author: ALFRED
"""

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        current_altitude=0
        highest_altitude=0
        for g in gain:
            current_altitude+=g
            if current_altitude>highest_altitude:
                highest_altitude=max(current_altitude,highest_altitude)
        return highest_altitude