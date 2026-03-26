class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        // check if 1 already present & set out of bounds num to 1
        bool onePresent = false;
        int n = nums.size();

        for(int i = 0; i < n; i++){
            if (nums[i] == 1){
                onePresent = true;
            }
            else if (nums[i] > n || nums[i] < 1){
                nums[i] = 1;
            }
        }

        if (!onePresent) return 1;

        // mark presence of num by setting nums[num - 1] = negative
        for(int i = 0; i < n; i++){
            if (nums[abs(nums[i]) - 1] < 0){
                continue;
            }
            nums[abs(nums[i]) - 1] *= -1;
        }

        // if nums[idx] > 0 => idx + 1 was absent
        for(int i = 0; i < n; i++){
            if(nums[i] > 0){
                return i + 1;
            }
        }

        return n + 1;

    }
};