import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> ps = Arrays.stream(progresses).boxed().collect(Collectors.toList());
        
        List<Integer> answer = new ArrayList<>();
        for (int i=0; i<ps.size(); i++) {
            // 젤 앞에꺼 100% 만드는데 n번 반복해야됨
            int n = getN(ps.get(i), speeds[i]);
            
            // n회만큼 다들 증가시켜
            for (int j=i; j<ps.size(); j++) {
                ps.set(j, ps.get(j) + (speeds[j] * n));
            }
           
            // 앞에서부터 100% 넘은거 몇갠지 체크
            int count = 0;
            for (int j=i; j<ps.size(); j++) {
                if (ps.get(j) < 100) break;
                count++;
                i = j;
            }
            answer.add(count);
        }
        
        return answer.stream().mapToInt(i->i).toArray();
    }
    
    private int getN(int progress, int speed) {
        int n = (100 - progress) / speed;
        n += (100 - progress) % speed != 0 ? 1 : 0;
        return n;
    }
}

// 젤앞에꺼 100%로 만드는데 n번 필요함
// 전체에 n번*speed 만큼 플러스
// 100넘은거 체크
// 아직 100안된놈 찾아서 반복
