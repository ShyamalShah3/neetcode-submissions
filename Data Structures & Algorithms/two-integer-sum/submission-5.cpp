class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> seen;

        for (int i = 0; i < nums.size(); i++) {
            int val = nums[i];
            int diff = target - val;

            if (seen.count(diff)) {
                return {seen[diff],i};
            }

            seen[val] = i;
        }
    }
};
