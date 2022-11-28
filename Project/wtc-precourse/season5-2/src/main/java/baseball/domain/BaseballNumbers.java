package baseball.domain;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class BaseballNumbers {
    private static final int NUMBERS_SIZE = 3;
    private static final int NUMBER_RANGE_MIN = 1;
    private static final int NUMBER_RANGE_MAX = 9;
    private final List<Integer> numbers;

    public BaseballNumbers(List<Integer> numbers) {
        validate(numbers);
        this.numbers = numbers;
    }
    private void validate(List<Integer> numbers) {
        validateSize(numbers);
        validateRange(numbers);
        validateDuplicate(numbers);
    }
    private void validateSize(List<Integer> numbers) {
        if (numbers.size() != NUMBERS_SIZE) {
            throw new IllegalArgumentException("[ERROR] wrong size");
        }
    }
    private void validateRange(List<Integer> numbers) {
        for (int n : numbers) {
            if (n < NUMBER_RANGE_MIN || NUMBER_RANGE_MAX < n) {
                throw new IllegalArgumentException("[ERROR] out of range");
            }
        }
    }
    private void validateDuplicate(List<Integer> numbers) {
        Set<Integer> withoutDuplicate = new HashSet<>(numbers);
        if (withoutDuplicate.size() != NUMBERS_SIZE) {
            throw new IllegalArgumentException("[ERROR] duplicate number");
        }
    }

    public GameResult compare(BaseballNumbers other) {
        GameResult gameResult = new GameResult();
        List<Integer> otherNumbers = other.getNumbers();

        for (int i = 0; i < NUMBERS_SIZE; i++) {
            if (numbers.get(i) == otherNumbers.get(i)) {
                gameResult.addStrike();
            }
            else if (numbers.contains(otherNumbers.get(i))) {
                gameResult.addBall();
            }
        }
        return gameResult;
    }

    public List<Integer> getNumbers() {
        return numbers;
    }
    @Override
    public String toString() {
        String result = "";
        for (int n : numbers) {
            result += n;
        }
        return result;
    }
}
