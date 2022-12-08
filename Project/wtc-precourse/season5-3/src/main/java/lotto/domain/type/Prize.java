package lotto.domain.type;

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
}
