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

    public boolean compare() {
        return false;
    }
    public int strikeCount() {
        return 0;
    }
    public int ballCount() {
        return 0;
    }
}
