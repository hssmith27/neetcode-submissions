class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> dict;
        for (int i = 0; i < nums.size(); i++) {
            int num = nums[i];
            if (dict.contains(num)) {
                return {dict[num], i};
            }
            dict[target - num] = i;
        }
    }
};
