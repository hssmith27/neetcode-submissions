class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> dictionary;
        for (int i = 0; i < nums.size(); i++) {
            if (dictionary.contains(nums[i])) {
                return true;
            }
            dictionary[nums[i]] = 1;
        }
        return false;
    }
};