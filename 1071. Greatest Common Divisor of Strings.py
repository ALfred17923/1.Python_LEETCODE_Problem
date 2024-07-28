# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 12:26:28 2024

@author: ALFRED
"""

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        # Check if str1 and str2 are concatenations of the same substring
        if str1 + str2 == str2 + str1:
            # Calculate the length of the gcd of the lengths of str1 and str2
            greatest_common_divisor_length = gcd(len(str1), len(str2))
            # Return the substring of length gcd
            return str1[:greatest_common_divisor_length]
        return ""