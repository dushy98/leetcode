class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        Morse = [".-","-...","-.-.","-..",".","..-.","--.",
                 "....","..",".---","-.-",".-..","--","-.",
                 "---",".--.","--.-",".-.","...","-","..-",
                 "...-",".--","-..-","-.--","--.."]
        
        seen = {"".join(Morse[ord(c) - ord('a')] for c in word) for word in words}
        return len(seen)
        