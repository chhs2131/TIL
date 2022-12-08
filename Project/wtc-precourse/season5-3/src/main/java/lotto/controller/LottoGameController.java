package lotto.controller;

import lotto.domain.LottoGame;
import lotto.view.OutputView;

public class LottoGameController {
    private final LottoGame lottoGame = new LottoGame();

    public void system() {
        try {
            buyLotto();
            setWinnerNumbers();
            checkLottoResult();
        } catch (IllegalArgumentException e) {
            OutputView.printError(e.toString());
            throw e;  // 에러와 함께 프로그램이 종료되야 함
        }
    }

    private void buyLotto() {

    }

    private void setWinnerNumbers() {

    }

    private void checkLottoResult() {

    }
}
