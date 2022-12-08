package lotto.view;

import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;
import lotto.domain.type.Lotto;

public class OutputView {
    public static void printInputPriceGuide() {
        System.out.println("구매금액을 입력해 주세요.");
    }

    public static void printMyLotto(List<Lotto> lottos) {
        System.out.println(lottos.size() + "개를 구매했습니다.");
        for (Lotto lotto : lottos) {
            List<Integer> numbers = lotto.getNumbers().stream().sorted().collect(Collectors.toList());
            System.out.println(numbers);
        }
    }

    public static void printInputWinnerNumbersGuide() {
        System.out.println("당첨 번호를 입력해 주세요.");
    }

    public static void printInputBonusNumberGuide() {
        System.out.println("보너스 번호를 입력해 주세요.");
    }

    public static void printLottoResult() {
        System.out.println("당첨 통계");
        System.out.println("---");
    }

    public static void printError(String e) {
        System.out.println("[ERROR] " + e);
    }
}
