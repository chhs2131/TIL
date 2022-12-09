package lotto.controller;

import java.util.List;
import lotto.domain.LottoGame;
import lotto.domain.type.Lotto;
import lotto.domain.type.LottoResult;
import lotto.view.InputView;
import lotto.view.OutputView;

public class LottoGameController {
    private final LottoGame lottoGame = new LottoGame();

    public void system() {
        try {
            buyLotto();
            LottoResult lottoResult = setWinnerNumbers();
            checkLottoResult(lottoResult);
        } catch (IllegalArgumentException e) {
            OutputView.printError(e.toString());
        }
    }

    private void buyLotto() {
        OutputView.printInputPriceGuide();
        int price = InputView.readPrice();
        List<Lotto> lottos = lottoGame.buyLotto(price);
        OutputView.printMyLotto(lottos);
    }

    private LottoResult setWinnerNumbers() {
        OutputView.printInputWinnerNumbersGuide();
        Lotto winnerNumbers = InputView.readWinnerNumbers();
        OutputView.printInputBonusNumberGuide();
        int bonusNumber = InputView.readBounusNumber();

        return lottoGame.draw(winnerNumbers, bonusNumber);
    }

    private void checkLottoResult(LottoResult lottoResult) {
        OutputView.printLottoResult(lottoResult);
    }
}
