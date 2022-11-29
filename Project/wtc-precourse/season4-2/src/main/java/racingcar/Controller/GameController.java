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
}
