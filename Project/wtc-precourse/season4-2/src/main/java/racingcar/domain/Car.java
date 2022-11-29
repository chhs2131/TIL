package racingcar.domain;

public class Car {
    private static final int MAXIMUM_NAME_LENGTH = 5;
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

    public void move() {
    }

    private void isGood() {
    }

    private void validateMoveRange() {
    }

    @Override
    public String toString() {
        return "이름:" + name + " 현위치:" + position;
    }
}
