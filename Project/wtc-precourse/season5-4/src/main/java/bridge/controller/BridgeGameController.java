package bridge.controller;

import bridge.BridgeMaker;
import bridge.BridgeNumberGenerator;
import bridge.BridgeRandomNumberGenerator;
import bridge.domain.BridgeGame;
import bridge.domain.type.Bridge;
import bridge.domain.type.Command;
import bridge.domain.type.Direction;
import bridge.domain.type.GameResult;
import bridge.view.InputView;
import bridge.view.OutputView;
import java.util.function.Supplier;

public class BridgeGameController {
    private final BridgeGame bridgeGame = new BridgeGame();

    // 잘못된 사용자 입력 발생시 다시 시도하도록 지정
    private <T> T repeat(Supplier<T> inputReader) {
        try {
            return inputReader.get();
        } catch (IllegalArgumentException e) {
            OutputView.printError(e.getMessage());
            return repeat(inputReader);
        }
    }

    public void system() {
        OutputView.printWelcome();
        makeBridge();

        GameResult gameResult = playGame();
        gameEnd(gameResult);
    }

    private GameResult playGame() {
        GameResult gameResult = new GameResult();

        while (gameResult.isPlaying()) {
            gameResult = goMove();
            checkMap(gameResult);
            if (gameResult.isFailed()) {
                checkRetry();
            }
        }
        return gameResult;
    }

    public void makeBridge() {
        OutputView.printBridgeSizeGuide();
        int bridgeSize = repeat(InputView::readBridgeSize);
        bridgeGame.makeBridge(bridgeSize);
    }

    public GameResult goMove() {
        OutputView.printMoveGuide();
        Direction direction = repeat(InputView::readMoving);
        return bridgeGame.move(direction);
    }

    public void checkMap(GameResult gameResult) {
        OutputView.printMap(gameResult);
    }

    public void checkRetry() {
        OutputView.printRetryGuide();
        Command command = repeat(InputView::readGameCommand);
        bridgeGame.retry(command);
    }

    public void gameEnd(GameResult gameResult) {
        OutputView.printResult(gameResult);
    }
}
