package racingcar.domain;

public class Car {
    private static final int MAXIMUM_NAME_LENGTH = 5;
    private static final int MOVE_RANGE_MIN = 0;
    private static final int MOVE_RANGE_MAX = 9;
    private final String name;
    private int position = 0;

    public Car(String name) {
        validateNameLength(name);
        this.name = name;
    }

    private static void validateNameLength(String name) {
        if (name.length() > MAXIMUM_NAME_LENGTH) {
            throw new IllegalArgumentException("이름은 5글자까지만 사용할 수 있습니다. (" + name + ", " + name.length() + "글자)");
        }
    }

    public void move(int number) {
        validateMoveRange(number);
    }

    private void isGood() {
    }

    private void goStraight() {
        position++;
    }

    private static void validateMoveRange(int position) {
        if (position < MOVE_RANGE_MIN || MOVE_RANGE_MAX < position) {
            throw new IllegalArgumentException("잘못된 이동 값이 전달되었습니다. (" + position + ")");
        }
    }

    @Override
    public String toString() {
        return "이름:" + name + " 현위치:" + position;
    }
}
