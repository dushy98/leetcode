class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        dict_ = defaultdict(list)
        count = 0
        
        for word in words:
            dict_[word[0]].append(word)
            
        for char in s:
            words_expecting_char = dict_[char]
            dict_[char] = []
            for word in words_expecting_char:
                if len(word) == 1:
                    count += 1
                else:
                    dict_[word[1]].append(word[1:])
            
        return count
    