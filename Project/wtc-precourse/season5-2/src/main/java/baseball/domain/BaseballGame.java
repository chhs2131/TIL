package baseball.domain;

import camp.nextstep.edu.missionutils.Randoms;

import java.util.ArrayList;
import java.util.List;

public class BaseballGame {
    private static final int NUMBERS_SIZE = 3;
    private static final int NUMBER_RANGE_MIN = 1;
    private static final int NUMBER_RANGE_MAX = 9;
    public BaseballNumbers makeRandomNumbers() {
        List<Integer> computer = new ArrayList<>();
        while (computer.size() < 3) {
            int randomNumber = Randoms.pickNumberInRange(NUMBER_RANGE_MIN, NUMBER_RANGE_MAX);
            if (!computer.contains(randomNumber)) {
                computer.add(randomNumber);
            }
        }
        return new BaseballNumbers(computer);
    }
    public void compareNumbers() {
    }
}
