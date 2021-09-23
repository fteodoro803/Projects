class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        # Gets all Substrings
        substringList = []
        currStr = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] in currStr:  # Ensures Unique Characters
                    break
                currStr += s[j]
                substringList.append(currStr)

            currStr = ""
        print(f"Substring List: {substringList}")

        # Gets Max Substring
        maxString = max(substringList, key=len)
        #print(f"\n\tString: {s}\n\tMax Substring: {maxString}\n\tLength: {len(maxString)}")
        return len(maxString)

# MAIN
if __name__ == '__main__':
    s = ["abcabcbb", "bbbbb", "pwwkew", "", "abcd"]

    test = Solution()
    print(test.lengthOfLongestSubstring(s[2]))