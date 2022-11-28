package baseball.view;

import baseball.domain.BaseballNumbers;
import baseball.domain.GameCommand;
import camp.nextstep.edu.missionutils.Console;

import java.util.List;

public class InputView {
    private static final String ALL_NUMBERS = "^[0-9]+$";
    public BaseballNumbers readBaseballNumbers() {
        String input = Console.readLine();
    }

    private List<Integer> stringToIntegerList(String input) {

    }

    private void validateStringNumber(String number) {
        if (!number.matches(ALL_NUMBERS)) {
            throw new IllegalArgumentException("[ERROR] 숫자가 아닌 값이 입력되었습니다.");
        }
    }
    public GameCommand readGameCommand() {
        return GameCommand.RESTART;
    }
}
