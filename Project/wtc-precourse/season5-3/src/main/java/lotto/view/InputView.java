package lotto.view;

import camp.nextstep.edu.missionutils.Console;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import lotto.domain.type.Lotto;

public class InputView {
    public static int readPrice() {
        String input = Console.readLine();
        return Integer.parseInt(input);
    }

    public static Lotto readWinnerNumbers() {
        try {
            String input = Console.readLine();
            List<String> splitNumbers = splitString(input, ",");
            List<Integer> numbers = toIntegerList(splitNumbers);
            return new Lotto(numbers);
        } catch (NumberFormatException e) {
            throw new IllegalArgumentException("숫자가 아닌 값이 들어왔습니다.");
        }
    }

    private static List<String> splitString(String input, String delimiter) {
        List<String> result = new ArrayList<String>();
        result.addAll(Arrays.asList(input.split(delimiter)));
        return result;
    }

    private static List<Integer> toIntegerList(List<String> numbers) {
        return numbers.stream()
                .map(Integer::parseInt)
                .collect(Collectors.toList());
    }

    public static int readBounusNumber() {
        try {
            String input = Console.readLine();
            return Integer.parseInt(input);
        } catch (NumberFormatException e) {
            throw new IllegalArgumentException("숫자가 아닌 값이 입력되었습니다.");
        }
    }
}
