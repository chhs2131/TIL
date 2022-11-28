package baseball.controller;

import baseball.domain.*;
import baseball.view.InputView;
import baseball.view.OutputView;

public class BaseballGameController {
    private final InputView inputView = new InputView();
    private final OutputView outputView = new OutputView();
    private final BaseballGame game = new BaseballGame();

    public BaseballGameController() {
        outputView.printWelcome();
    }

    public void playGame() {
        GameCommand command = GameCommand.KEEP_PLAYING;

        while (command.isKeepPlaying()) {
            gameStart();
            GameProgress progress = GameProgress.PLAYING;
            while (progress == GameProgress.PLAYING) {
                progress = chooseNumbers();
            }
            command = chooseContinue();
            System.out.println(command.toString());
        }
    }

    public void gameStart() {
        game.makeRandomNumbers();
    }

    public GameProgress chooseNumbers() {
        BaseballNumbers numbers = inputView.readBaseballNumbers();
        GameResult gameResult = game.compareNumbers(numbers);
        outputView.printGameResult(gameResult);
        return gameResult.getProgress();
    }

    public GameCommand chooseContinue() {
        outputView.printContinueGuide();
        GameCommand command = inputView.readGameCommand();
        return command;
    }
}
