class Solution {
public:
    int firstUniqChar(string s) {
        
        unordered_map <char,int> alphabets(26);
        
        for (int i = 0; i < s.size(); i++){
            alphabets[s[i]]++;
        }
        
        for (int i = 0; i < s.size(); i++){
            if (alphabets[s[i]] == 1) 
                return i;
        }
        return -1;
    }
};