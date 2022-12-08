package lotto.domain;

import java.util.ArrayList;
import java.util.List;
import lotto.domain.type.Lotto;
import lotto.domain.type.LottoResult;
import lotto.domain.type.Prize;

public class LottoGame {
    private static final int LOTTO_PRICE = 1000;
    List<Lotto> lottos = new ArrayList<Lotto>();
    LottoResult lottoResult;

    public List<Lotto> buyLotto(int money) {
        validateMoney(money);
        setLottoResult(money);

        int amount = money / LOTTO_PRICE;
        lottos = LottoGenerator.generateLottos(amount);
        return lottos;
    }

    private void setLottoResult(int money) {
        lottoResult = new LottoResult(money);
    }

    private void validateMoney(int money) {
        if (money == 0) {
            throw new IllegalArgumentException("0원으로는 로또를 살 수 없습니다.");
        }
        if (money % LOTTO_PRICE != 0) {
            throw new IllegalArgumentException("입력한 금액은 1000으로 나누어지지 않습니다. " + money);
        }
    }

    public LottoResult darw(Lotto winnerLotto, int bounusNumber) {
        for (Lotto lotto : lottos) {
            Prize prize = checkResult(lotto, winnerLotto, bounusNumber);
            lottoResult.addPrize(prize);
        }
        return lottoResult;
    }

    private Prize checkResult(Lotto lotto1, Lotto lotto2, int bonusNumber) {
        int count = lotto1.countSameNumbers(lotto2);
        boolean bonus = lotto1.isContainNumber(bonusNumber);
        return Prize.from(count, bonus);
    }
}
