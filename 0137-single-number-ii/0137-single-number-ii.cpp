class Solution {
public:
    int singleNumber(vector<int>& nums) {
        // brute force cpp
        unordered_map<int, int> n;
       
       for(auto i:nums){
           n[i]++;
       }

        for (auto i: n){
            if(i.second == 1){
                return i.first;
            }
        }

        return -1;
    }
};