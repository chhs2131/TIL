package racingcar.domain;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import org.junit.jupiter.params.provider.ValueSource;

import java.util.Arrays;
import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;


class GameTest {
    Game game;
    List<Car> cars;
    @BeforeEach
    void beforeEach() throws Exception {
        cars = Arrays.asList(
                new Car("test1"),
                new Car("test2"),
                new Car("test3")
        );
        int goalLine = 5;

        game = new Game(cars, goalLine);
    }

    @DisplayName("차가 앞으로 잘 나아가나요?")
    @CsvSource(value = {"0:0", "1:0", "2:0", "3:0", "4:1", "5:1", "6:1", "7:1", "8:1", "9:1"}, delimiter = ':')
    @ParameterizedTest
    void moveCar(int power, int result) {
        Car nowCar = cars.get(0);
        game.moveCar(nowCar, power);
        assertThat(nowCar.getPosition()).isEqualTo(result);
    }

    @Test
    void moveCars() {
        game.moveCar(cars.get(0), 0);
        game.moveCar(cars.get(1), 3);
        game.moveCar(cars.get(2), 9);

        assertThat(cars.get(0).getPosition()).isEqualTo(0);
        assertThat(cars.get(1).getPosition()).isEqualTo(0);
        assertThat(cars.get(2).getPosition()).isEqualTo(1);
    }

    @Test
    void checkWinning() {
        List<String> winners = game.checkWinning(cars);
        while (winners.isEmpty()) {
            game.moveCar(cars.get(0), 0);
            game.moveCar(cars.get(1), 3);
            game.moveCar(cars.get(2), 9);
            winners = game.checkWinning(cars);
        }

        assertFalse(winners.contains("test1"));
        assertFalse(winners.contains("test2"));
        assertTrue(winners.contains("test3"));
    }
}