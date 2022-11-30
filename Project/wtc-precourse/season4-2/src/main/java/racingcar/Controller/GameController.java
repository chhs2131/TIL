package racingcar.Controller;

import racingcar.domain.Car;
import racingcar.domain.Game;
import racingcar.domain.GameProgress;
import racingcar.view.InputView;
import racingcar.view.OutputView;

import java.util.List;

public class GameController {
    List<Car> cars;
    int goalLine;
    private Game game;
    private GameProgress progress = GameProgress.START;

    public GameController() {
        progress = GameProgress.INPUT_CAR;
    }

    public void playGame() {
        boolean flag = false;

        // 우승 깃발이 올라갈 때까지 경기를 진행한다.
        while (!flag) {
            try {
                flag = doThisTurn();
            } catch (IllegalArgumentException e) {
                OutputView.printException(e.toString());
            }
        }
    }

    private boolean doThisTurn() {  // 현재 상태를 확인해서 해당하는 행동을 진행한다.
        if (progress == GameProgress.INPUT_CAR) {  // 참가 자동차 설정
            cars = registerCars();
            progress = GameProgress.INPUT_GOAL_LINE;
        }
        if (progress == GameProgress.INPUT_GOAL_LINE) {  // 골인하려면 몇 칸 가야되는지 설정
            goalLine = inputGoalLine();
            game = new Game(cars, goalLine);
            progress = GameProgress.PLAYING;
        }
        if (progress == GameProgress.PLAYING) {  // 레이싱 진행
            return racing();
        }
        return false;
    }

    private List<Car> registerCars() {
        OutputView.printInputCarNameGuide();
        return InputView.readCarsName();
    }

    private int inputGoalLine() {
        OutputView.printInputDestinationGuide();
        return InputView.readDestination();
    }

    private boolean racing() {
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
