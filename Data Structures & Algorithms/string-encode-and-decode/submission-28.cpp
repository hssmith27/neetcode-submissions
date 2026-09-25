class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded = "";
        for (const string& str : strs) {
            int length = str.size();
            encoded += to_string(length) + "#" + str;
        }

        return encoded;
    }

    vector<string> decode(string s) {
        vector<string> res;

        int i = 0;

        while (i < s.size()) {
            int j = i;
            while (s[j] != '#') {
                j++;
            }
            int length = stoi(s.substr(i, j - i));
            i = j + 1;
            string str = s.substr(i, length);
            res.push_back(str);
            i = length + i;
        }

        return res;
    }
};
