package racingcar.Controller;

import racingcar.domain.Car;
import racingcar.domain.Game;
import racingcar.view.InputView;
import racingcar.view.OutputView;

import java.util.List;

public class GameController {
    private Game game;

    public GameController() {
    }

    public List<Car> registerCars() {
        OutputView.printInputCarNameGuide();
        return InputView.readCarsName();
    }
}
