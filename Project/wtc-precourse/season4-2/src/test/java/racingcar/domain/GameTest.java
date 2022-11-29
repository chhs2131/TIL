package racingcar.domain;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;


class GameTest {
    List<Car> cars;
    @BeforeEach
    void beforeEach() throws Exception {
        cars = Arrays.asList(
                new Car("test1"),
                new Car("test2"),
                new Car("test3")
        );
        int goalLine = 5;

        Game game = new Game(cars, goalLine);
    }

    @Test
    void moveCars() {
    }

    @Test
    void checkWinning() {
    }

    @Test
    void notificationWinner() {
    }
}