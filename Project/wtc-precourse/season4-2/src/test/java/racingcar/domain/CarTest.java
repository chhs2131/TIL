package racingcar.domain;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.*;

class CarTest {
    @ValueSource(strings = {"aaa", "bbb", "ccc", "abc", "123", "hi", "a", "0", "abcde", "a12c"})
    @ParameterizedTest
    void move(String name) {
        Car c = new Car(name);
        assertThat(c.getName()).isEqualTo(name);
    }

    @ValueSource(ints = {0, 1, 2, 3})
    @ParameterizedTest
    void move_부족한힘(int power) {
        Car c = new Car("test");
        c.move(power);
        assertThat(c.getPosition()).isEqualTo(0);
    }

    @ValueSource(ints = {4, 5, 6, 7, 8, 9})
    @ParameterizedTest
    void move_충분한힘(int power) {
        Car c = new Car("test");
        c.move(power);
        assertThat(c.getPosition()).isEqualTo(1);
    }

    @ValueSource(ints = {-100, -9, 10, 100, 1000})
    @ParameterizedTest
    void move_예외_잘못된힘(int power) {
        Car c = new Car("test");
        assertThrows(IllegalArgumentException.class, () -> {
            c.move(power);
        });
    }
}