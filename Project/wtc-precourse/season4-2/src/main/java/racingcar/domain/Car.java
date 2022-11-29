package racingcar.domain;

public class Car {
    private final String name;
    private int position = 0;

    public Car(String name) {
        this.name = name;
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
