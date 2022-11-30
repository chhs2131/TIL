package racingcar.view;

import camp.nextstep.edu.missionutils.Console;
import racingcar.domain.Car;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class InputView {
    private static final String ONLY_NUMBER_PATTERN = "^[0-9]+$";

    public static List<Car> readCarsName() {
        String input = Console.readLine();

        return Arrays.stream(input.split(","))  // 쉼표로 각 이름을 구분한다.
                .map(Car::new)  // 각각의 이름을 가진 자동차를 생성한다.
                .collect(Collectors.toList());

        // 이름이 없는 경우도 허용되나? ,,
    }

    public static int readDestination() {
        String input = Console.readLine();
        validateNumberOnly(input);
        return Integer.parseInt(input);
    }

    private static void validateNumberOnly(String input) {
        if (!input.matches(ONLY_NUMBER_PATTERN)) {
            throw new IllegalArgumentException("숫자만 입력할 수 있습니다. (입력:" + input + ")");
        }
    }
}
