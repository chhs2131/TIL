package baseball.domain;

import camp.nextstep.edu.missionutils.Randoms;

import java.util.ArrayList;
import java.util.List;

public class BaseballGame {
    private static final int NUMBERS_SIZE = 3;
    private static final int NUMBER_RANGE_MIN = 1;
    private static final int NUMBER_RANGE_MAX = 9;

    private BaseballNumbers answer;

    public void makeRandomNumbers() {
        List<Integer> computer = new ArrayList<>();
        while (computer.size() < NUMBERS_SIZE) {
            int randomNumber = Randoms.pickNumberInRange(NUMBER_RANGE_MIN, NUMBER_RANGE_MAX);
            if (!computer.contains(randomNumber)) {
                computer.add(randomNumber);
            }
        }
        answer = new BaseballNumbers(computer);
        System.out.println("정답=>" + answer.toString());
    }
    public GameResult compareNumbers(BaseballNumbers playerNumbers) {
        return answer.compare(playerNumbers);
    }
}
