package lotto.domain.type;

import java.util.Arrays;
import java.util.HashMap;
import java.util.stream.Collectors;

public class LottoResult {
    private final int startMoney;
    private HashMap<Prize, Integer> result = new HashMap<Prize, Integer>();

    public LottoResult(int startMoney) {
        this.startMoney = startMoney;
    }
    public void addPrize(Prize prize) {
        // 당첨되지 않은 경우는 제외
        if (prize == null) {
            return;
        }
        // 당첨된 곳에 갯수를 추가한다.
        Integer count = result.putIfAbsent(prize, 1);
        if (count != null) {
            result.put(prize, count + 1);
        }
    }

    public int getPrizeCount(Prize prize) {
        return result.getOrDefault(prize, 0);
    }

    public float getPercent() {
        long endMoney = getAllPrizeMoney();
        System.out.println(startMoney +" "+ endMoney);
        float calc = (float)endMoney / startMoney * 100;
        long percent = Math.round(calc * 100);
        return (float)percent / 100;
    }

    public long getAllPrizeMoney() {
        return Arrays.stream(Prize.values())
                .map(this::getPrizeMoney)
                .reduce(Long::sum)
                .orElseThrow(() -> new IllegalStateException("엥"));
    }

    public long getPrizeMoney(Prize prize) {
        int count = getPrizeCount(prize);
        return (long) count * prize.getMoney();
    }
}
