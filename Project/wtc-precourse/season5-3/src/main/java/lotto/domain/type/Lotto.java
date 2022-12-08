package lotto.domain.type;

import java.util.List;
import java.util.Set;

public class Lotto {
    private static final int NUMBER_MIN = 1;
    private static final int NUMBER_MAX = 45;
    private static final int NUMBER_SIZE = 6;

    private final List<Integer> numbers;

    public Lotto(List<Integer> numbers) {
        validate(numbers);
        this.numbers = numbers;
    }

    private void validate(List<Integer> numbers) {
        validateSize(numbers);
        validateRange(numbers);
        validateDuplicate(numbers);
    }

    private static void validateSize(List<Integer> numbers) {
        if (numbers.size() != NUMBER_SIZE) {
            throw new IllegalArgumentException("사이즈가 맞지않습니다.");
        }
    }

    private static void validateRange(List<Integer> numbers) {
        numbers.stream()
                .filter(number -> number < NUMBER_MIN || NUMBER_MAX < number)
                .findAny()
                .ifPresent(e -> {throw new IllegalArgumentException("범위 밖의 숫자가 있습니다. " + e);});
    }

    private static void validateDuplicate(List<Integer> numbers) {
        if (Set.copyOf(numbers).size() != NUMBER_SIZE) {
            throw new IllegalArgumentException("중복되는 숫자가 있습니다.");
        }
    }

    public int countSameNumbers(Lotto lotto) {
        return (int) lotto.getNumbers().stream()
                .filter(number -> numbers.contains(number))
                .count();
    }

    public boolean isContainNumber(int number) {
        return numbers.contains(number);
    }

    public List<Integer> getNumbers() {
        return numbers;
    }

    @Override
    public String toString() {
        return numbers.toString();
    }
}
