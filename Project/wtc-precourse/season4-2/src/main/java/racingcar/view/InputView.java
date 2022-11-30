package racingcar.view;

import camp.nextstep.edu.missionutils.Console;
import racingcar.domain.Car;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class InputView {
    private static final String ONLY_NUMBER_PATTERN = "^[0-9]+$";
    private static final String NAME_PATTERN = "^[0-9|가-힣|a-z|A-Z|,]+$";

    public static List<Car> readCarsName() {
        String input = Console.readLine();
        validateName(input);

        return Arrays.stream(input.split(","))  // 쉼표로 각 이름을 구분한다.
                .map(Car::new)  // 각각의 이름을 가진 자동차를 생성한다.
                .collect(Collectors.toList());
    }

    private static void validateName(String input) {
        if (!input.matches(NAME_PATTERN)) {
            throw new IllegalArgumentException("이름에는 숫자, 영어, 한글만 입력될 수 있습니다. (입력:" + input + ")");
        }
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
