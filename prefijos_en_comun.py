"""Write a function to find the longest common prefix string amongst 
an array of strings.
If there is no common prefix, return an empty string"""

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        prefijo_comun= ""
        longitud_minima= min(len(str) for str in strs)
        for i in range(longitud_minima):
            if all(str[i]==strs[0][i]for str in strs):
                prefijo_comun += strs[0][i]
            else:
                break
        return prefijo_comun
objeto = Solution()
list=["flower","flow","flight"]
resultado= objeto.longestCommonPrefix(list)
print(resultado)