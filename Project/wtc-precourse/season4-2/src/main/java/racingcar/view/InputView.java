package racingcar.view;

import camp.nextstep.edu.missionutils.Console;
import racingcar.domain.Car;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class InputView {
    public static List<Car> readCarsName() {
        String input = Console.readLine();

        return Arrays.stream(input.split(","))  // 쉼표로 각 이름을 구분한다.
                .map(Car::new)  // 각각의 이름을 가진 자동차를 생성한다.
                .collect(Collectors.toList());
    }

    public static void readDestination() {
    }

    private static void validateNumberOnly() {
    }
}
