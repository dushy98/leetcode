class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
      sort(nums.begin(), nums.end()); // sort 
      int n = nums.size();
      for(int i = 1; i < n; i++){       // then linear search
          if(nums[i]==nums[i-1])
            return true;
      }
      return false;
    }
};