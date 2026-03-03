#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> char_map(128,-1);
        int left = 0;
        int max_len = 0;
        int n = s.length();

        for (int right = 0; right < n; right++) {
            char current_char = s[right];

            if (char_map[current_char] >= left) {
                left = char_map[current_char] + 1;
            }
            char_map[current_char] = right;

            int current_len = right - left + 1;
            if (current_len > max_len) {
                max_len = current_len;
            }
        }
        return max_len;
        
    }
};