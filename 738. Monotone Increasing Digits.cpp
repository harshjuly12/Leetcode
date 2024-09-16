class Solution {
public:
    int monotoneIncreasingDigits(int n) {
        string numStr = to_string(n);
        int marker = 1;
      
        while (marker < numStr.size() && numStr[marker - 1] <= numStr[marker]) {
            ++marker;
        }
      
        if (marker < numStr.size()) {
            while (marker > 0 && numStr[marker - 1] > numStr[marker]) {
                numStr[marker - 1]--;
                --marker;
            }
            for (int i = marker + 1; i < numStr.size(); ++i) {
                numStr[i] = '9';
            }
        }
      
        return stoi(numStr);
    }
};
