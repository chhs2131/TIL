import java.util.*;

class Solution {
    public int solution(int[] citations) {
        Arrays.sort(citations);
        
        int h = 0;
        for (int i=0; i<citations.length; i++) {
            int citation = citations[i];
            int left = citations.length - i;
            
            h = citation > left ? left : citation;
			if (citation >= left) break;
        }
        return h;
    }
}

// H-Index: min(ccitation, len-i)
