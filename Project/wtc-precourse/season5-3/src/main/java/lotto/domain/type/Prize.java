package lotto.domain.type;

import java.text.DecimalFormat;
import java.util.Arrays;

public enum Prize {
    FIRST(6, false, 2000000000),
    SECOND(5, true, 30000000),
    THIRD(5, false, 1500000),
    FOURTH(4, false, 50000),
    FIFTH(3, false, 5000);

    private int sameNumber;
    private boolean bonus;
    private int money;

    Prize(int sameNumber, boolean bonus, int money) {
        this.sameNumber = sameNumber;
        this.bonus = bonus;
        this.money = money;
    }

    public static Prize from(int sameNumber, boolean bonus) {
        return Arrays.stream(Prize.values())
                .filter(prize -> prize.getSameNumber() == sameNumber)
                .filter(prize -> !prize.isSecondPrize() || prize.getBonus() == bonus)
                .findAny()
                .orElse(null);
    }

    private boolean isSecondPrize() {
        return this == SECOND;
    }

    private int getSameNumber() {
        return sameNumber;
    }

    private boolean getBonus() {
        return bonus;
    }

    public int getMoney() {
        return money;
    }

    private static final DecimalFormat decimalFormat = new DecimalFormat("###,###");
    public static String makeSentence(Prize prize) {
        String sentence = prize.getSameNumber() + "개 일치";
        sentence += makeBonusSentence(prize.getBonus());
        sentence += " (" + decimalFormat.format(prize.getMoney()) + "원)";

        return sentence;
    }

    private static String makeBonusSentence(boolean bonus) {
        if (bonus) {
            return ", 보너스 볼 일치";
        }
        return "";
    }
}
