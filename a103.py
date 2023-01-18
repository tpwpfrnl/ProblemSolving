'''
A103 Unique Morse Code Words
Problem : https://leetcode.com/problems/unique-morse-code-words/description/
Date : 20230119
'''

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        encode = dict(zip(alpha, morse))
        out = []
        for i in words:
            word = ""
            for j in i:
                word = word + encode[j]
            if word not in out:
                out.append(word)
        return len(out)