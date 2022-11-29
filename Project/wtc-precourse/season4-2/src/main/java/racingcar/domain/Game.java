package racingcar.domain;

import camp.nextstep.edu.missionutils.Randoms;
import racingcar.view.InputView;
import racingcar.view.OutputView;

import java.util.List;
import java.util.stream.Collectors;

public class Game {
    private static final int POWER_RANGE_MIN = 0;
    private static final int POWER_RANGE_MAX = 9;
    final List<Car> cars;
    final int goalLine;

    public Game(List<Car> cars, int goalLine) {
        this.cars = cars;
        this.goalLine = goalLine;
    }

    private void moveCars() {
        for (Car car : cars) {
            int power = makeRandomPower();
            car.move(power);
        }
    }

    private int makeRandomPower() {
        return Randoms.pickNumberInRange(POWER_RANGE_MIN, POWER_RANGE_MAX);
    }

    private List<String> checkWinning() {
        return cars.stream()
                .filter(car -> car.getPosition() >= goalLine)
                .map(car -> car.getName())
                .collect(Collectors.toList());
    }

    public void notificationWinner() {
    }
}
