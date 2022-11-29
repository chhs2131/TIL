package racingcar.Controller;

import racingcar.domain.Car;
import racingcar.domain.Game;
import racingcar.view.InputView;
import racingcar.view.OutputView;

import java.util.List;

public class GameController {
    private Game game;

    public GameController() {
        game = new Game(registerCars(), inputGoalLine());
    }

    public List<Car> registerCars() {
        OutputView.printInputCarNameGuide();
        return InputView.readCarsName();
    }

    public int inputGoalLine() {
        OutputView.printInputDestinationGuide();
        return InputView.readDestination();
    }

    public void racing() {
        while(true) {
            List<Car> cars = game.moveCars();  // 경주를 진행하고 그 결과를 출력한다.
            OutputView.printRacingResult(cars);

            List<String> winners = game.checkWinning(cars);  // 승리자가 있는지 확인한다.
            if (!winners.isEmpty()) {
                notificationWinner(winners);
                break;
            }
        }
    }

    private static void notificationWinner(final List<String> winners) {
        OutputView.printWinner(winners);
    }
}
