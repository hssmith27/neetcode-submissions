class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<std::string, vector<string>> dict;
        for (int i = 0; i < strs.size(); i++) {
            string word = strs[i];
            std::vector<int> count(26, 0);
            for (int j = 0; j < word.size(); j++) {
                count[word[j] - 'a']++;
            }
            string key = to_string(count[0]);
            for (int i = 1; i < 26; i++) {
                key += ',' + to_string(count[i]);
            }
            dict[key].push_back(word);
        }
        vector<vector<string>> result;
        for (const auto& pair : dict) {
            result.push_back(pair.second);
        }
        return result;
    }
};
