class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> num_map;
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            // Check if the complement exists in the map
            if (num_map.find(complement) != num_map.end()) {
                // Return the indices of the two numbers
                return {num_map[complement], i};
            }
            // Add the current number and its index to the map
            num_map[nums[i]] = i;
        }
        // If no solution is found, return an empty vector
        return {};

    }
};