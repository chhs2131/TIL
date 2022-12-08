package lotto.view;

public class OutputView {
    public static void printInputPriceGuide() {
        System.out.println("구매금액을 입력해 주세요.");
    }

    public static void printMyLotto() {
        System.out.println("개를 구매했습니다.");
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
