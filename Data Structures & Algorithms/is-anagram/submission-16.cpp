class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        std::unordered_map<char, int> sDict;
        std::unordered_map<char, int> tDict;
        for (int i = 0; i < s.size(); i++) {
            sDict[s[i]]++;
            tDict[t[i]]++;
        }

        return sDict == tDict;
    }
};
