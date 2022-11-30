package racingcar.domain;

import camp.nextstep.edu.missionutils.Randoms;

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

    public List<Car> moveCars() {
        for (Car car : cars) {
            moveCar(car, makeRandomPower());
        }
        return cars;
    }

    public void moveCar(Car car, int power) {
        car.move(power);
    }

    private int makeRandomPower() {
        return Randoms.pickNumberInRange(POWER_RANGE_MIN, POWER_RANGE_MAX);
    }

    public List<String> checkWinning(List<Car> cars) {
        return cars.stream()
                .filter(car -> car.getPosition() >= goalLine)
                .map(Car::getName)
                .collect(Collectors.toList());
    }
}
