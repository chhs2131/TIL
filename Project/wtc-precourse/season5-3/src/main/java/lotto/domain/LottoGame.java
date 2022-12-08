package lotto.domain;

import java.util.ArrayList;
import java.util.List;
import lotto.domain.type.Lotto;

public class LottoGame {
    private static final int LOTTO_PRICE = 1000;
    List<Lotto> lottos = new ArrayList<Lotto>();

    public List<Lotto> buyLotto(int money) {
        validateMoney(money);
        int amount = money / LOTTO_PRICE;
        lottos = LottoGenerator.generateLottos(amount);
        return lottos;
    }

    private void validateMoney(int money) {
        if (money == 0) {
            throw new IllegalArgumentException("0원으로는 로또를 살 수 없습니다.");
        }
        if (money % LOTTO_PRICE != 0) {
            throw new IllegalArgumentException("입력한 금액은 1000으로 나누어지지 않습니다. " + money);
        }
    }

}
