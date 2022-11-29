package racingcar.domain;

public class Car {
    private static final int MAXIMUM_NAME_LENGTH = 5;
    private static final int POWER_RANGE_MIN = 0;
    private static final int POWER_RANGE_MAX = 9;
    private static final int MINIMUM_POWER = 4;

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

    public void move(int power) {
        validateMoveRange(power);
        if (isPowerEnough(power)) {
            goStraight();
        }
    }

    private static void validateMoveRange(int power) {
        if (power < POWER_RANGE_MIN || POWER_RANGE_MAX < power) {
            throw new IllegalArgumentException("잘못된 이동 값이 전달되었습니다. (" + power + ")");
        }
    }

    private static boolean isPowerEnough(int power) {
        return MINIMUM_POWER <= power;
    }

    private void goStraight() {
        position++;
    }

    private static void validatePosition(int position) {
        if (position < 0) {
            throw new IllegalArgumentException("위치는 마이너스가 될 수 없습니다.");
        }
    }

    @Override
    public String toString() {
        return "이름:" + name + " 현위치:" + position;
    }
}
