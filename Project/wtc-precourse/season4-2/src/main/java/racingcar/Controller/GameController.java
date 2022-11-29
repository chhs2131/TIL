package racingcar.Controller;

import racingcar.domain.Car;
import racingcar.domain.Game;
import racingcar.domain.GameProgress;
import racingcar.view.InputView;
import racingcar.view.OutputView;

import java.util.List;

public class GameController {
    private Game game;
    private GameProgress progress = GameProgress.START;

    public GameController() {
        progress = GameProgress.INPUT_CAR;
        //game = new Game(registerCars(), inputGoalLine());
    }

    public void playGame() {
        List<Car> cars = null;
        int goalLine;
        boolean flag = false;

        while (!flag) {
            try {
                if (progress == GameProgress.INPUT_CAR) {
                    cars = registerCars();
                    progress = GameProgress.INPUT_GOAL_LINE;
                }
                if (progress == GameProgress.INPUT_GOAL_LINE) {
                    goalLine = inputGoalLine();
                    game = new Game(cars, goalLine);
                    progress = GameProgress.PLAYING;
                }
                if (progress == GameProgress.PLAYING) {
                    flag = racing();
                }
            } catch (IllegalArgumentException e) {
                OutputView.printException(e.toString());
            }
        }
    }

    public List<Car> registerCars() {
        OutputView.printInputCarNameGuide();
        return InputView.readCarsName();
    }

    public int inputGoalLine() {
        OutputView.printInputDestinationGuide();
        return InputView.readDestination();
    }

    public boolean racing() {
        List<Car> cars = game.moveCars();  // 경주를 진행하고 그 결과를 출력한다.
        OutputView.printRacingResult(cars);

        List<String> winners = game.checkWinning(cars);  // 승리자가 있는지 확인한다.
        if (!winners.isEmpty()) {
            notificationWinner(winners);
            return true;
        }
        return false;
    }

    private static void notificationWinner(final List<String> winners) {
        OutputView.printWinner(winners);
    }
}
