class Solution {
    boolean solution(String s) {
        s = s.toLowerCase();
        
        int p_count = 0;
        int y_count = 0;
        
        for (char c : s.toCharArray()) {
            if (c == 'p') p_count++;
            if (c == 'y') y_count++;
        }
        
        return p_count == y_count;
    }
}