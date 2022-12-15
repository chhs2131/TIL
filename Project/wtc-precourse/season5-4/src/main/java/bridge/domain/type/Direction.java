package bridge.domain.type;

import java.util.Arrays;
import java.util.Objects;

public enum Direction {
    DOWN(0, "D"),
    UP(1, "U");

    private int number;
    private String word;

    Direction(int number, String word) {
        this.number = number;
        this.word = word;
    }

    public static Direction from(String word) {
        return Arrays.stream(Direction.values())
                .filter(direct -> Objects.equals(direct.getWord(), word))
                .findAny()
                .orElseThrow(() -> new IllegalArgumentException("해당하는게 없습니다. " + word));
    }

    public static String numberToWord(int number) {
        return Arrays.stream(Direction.values())
                .filter(direct -> direct.getNumber() == number)
                .map(Direction::getWord)
                .findAny()
                .orElseThrow(() -> new IllegalArgumentException("해당하는게 없습니다. " + number));
    }

    public static boolean compare(Direction direction1, Direction direction2) {
        return direction1 == direction2;
    }

    private String getWord() {
        return word;
    }

    private int getNumber() {
        return number;
    }
}
