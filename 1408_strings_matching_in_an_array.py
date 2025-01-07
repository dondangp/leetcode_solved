# Given an array of string words, 
# return all strings in words that is a substring of another word. 
# You can return the answer in any order.
# A substring is a contiguous sequence of characters within a string

# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]

class Solution:
    def stringMatching(self, words):
        # initialize an empty list to store the substrings
        res = []

        # Loop through each words in the list
        for i, word in enumerate(words):
            # check if the current word is a substring of any other word in the list
            for other_word in words:
                # avoid comparing to each other
                if word != other_word and word in other_word:
                    res.append(word)
                    break # No need to continue checking
        
        return res
    
sol = Solution()

testCase = ["mass","as","hero","superhero"]

print(sol.stringMatching(testCase))
        
        
