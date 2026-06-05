class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        const string& base = strs[0];
        int n = base.size();

        for (int i = 0; i < n; i++) {
            for (const string& str : strs) {
                if (i == str.size() || str[i] != base[i]) {
                    return str.substr(0,i);
                }
            }
        }

        return base;
    }
};