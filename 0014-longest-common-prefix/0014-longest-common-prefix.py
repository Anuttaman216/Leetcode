class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        first = strs[0]
        ans = ""

        for i in range(len(first)):
            ch = first[i]

            for word in strs[1:]:
                if i >= len(word) or word[i] != ch:
                    return ans

            ans += ch

        return ans