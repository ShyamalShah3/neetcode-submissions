class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string base = strs[0];
        int n = base.size();

        for (int i = 0; i < n; i++) {
            for (string str : strs) {
                if (i == str.size() or str[i] != base[i]) {
                    return str.substr(0,i);
                }
            }
        }

        return base;
    }
};