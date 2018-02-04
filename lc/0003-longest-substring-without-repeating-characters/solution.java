// class Solution {
//     public int lengthOfLongestSubstring(String s) {
//         int result = findSubstring(s, 0, 0);
//         return result;
//     }
    
//     public boolean duplicateCheck(String s, char ch) {
//         if (s.indexOf(ch) == -1) return false;
//         else return true;
//     }
    
//     public int findSubstring(String s, int startPoint, int maxCnt) {
//         StringBuilder str = new StringBuilder();
//         int counter = 0;
//         while (startPoint < s.length()) {
//             if (!duplicateCheck(str.toString(), s.charAt(startPoint))) {
//                 str.append(s.charAt(startPoint));
//                 counter++;
//             } else {
//                 counter = counter > maxCnt ? counter : maxCnt;
//                 findSubstring(s, startPoint + 1, counter);
//             }
            
//             startPoint++;
//         }
//         return counter;
//     }
    
    
    
    
// }

public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        Set<Character> set = new HashSet<>();
        int ans = 0, i = 0, j = 0;
        while (i < n && j < n) {
            // try to extend the range [i, j]
            if (!set.contains(s.charAt(j))){
                set.add(s.charAt(j++));
                ans = Math.max(ans, j - i);
            }
            else {
                set.remove(s.charAt(i++));
            }
        }
        return ans;
    }
}
