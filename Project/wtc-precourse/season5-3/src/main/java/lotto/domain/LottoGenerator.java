package lotto.domain;

import camp.nextstep.edu.missionutils.Randoms;
import java.util.ArrayList;
import java.util.List;
import lotto.domain.type.Lotto;

public class LottoGenerator {
    public static List<Lotto> generateLottos(int amount) {
        List<Lotto> result = new ArrayList<Lotto>();
        for (int i = 0; i < amount; i++) {
            result.add(makeLotto());
        }
        return result;
    }

    public static Lotto makeLotto() {
        List<Integer> numbers = Randoms.pickUniqueNumbersInRange(1, 45, 6);
        return new Lotto(numbers);
    }
}
