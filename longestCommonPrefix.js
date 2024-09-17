/**14. Longest Common Prefix
Easy
Topics
Companies
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters. */

function longestCommonPrefix(strs) {
    if (strs.length === 0) return "";

    // Find the minimum length of strings in the array
    const minLength = Math.min(...strs.map(str => str.length));

    let prefix = "";
    
    for (let i = 0; i < minLength; i++) {
        const currentChar = strs[0][i];
        
        // Check if the current character is the same in all strings
        for (let j = 1; j < strs.length; j++) {
            if (strs[j][i] !== currentChar) {
                return prefix;
            }
        }
        
        // If the current character is common in all strings, add it to the prefix
        prefix += currentChar;
    }
    
    return prefix;
}