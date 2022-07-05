class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int result = 0;
        unordered_map<int, int> count;
        for(int num : nums){
            result += count[num]++;
        }
        return result;
    }
};