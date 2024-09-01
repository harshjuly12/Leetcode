class Solution {
 public:
  bool find132pattern(vector<int>& nums) {
    stack<int> stack;  
    int ak = INT_MIN;  

    for (int i = nums.size() - 1; i >= 0; --i) {
      if (nums[i] < ak)
        return true;
      while (!stack.empty() && stack.top() < nums[i])
        ak = stack.top(), stack.pop();
      stack.push(nums[i]);  
    }

    return false;
  }
};