package baseball.domain;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.*;

class BaseballNumbersTest {
    @Test
    void makeNumbers() {
        List<Integer> l = List.of(1, 2, 3);
        BaseballNumbers numbers = new BaseballNumbers(l);
        assertThat(numbers.toString()).isEqualTo("123");
    }

    @Test
    void 잘못된입력_중복된숫자() {
        List<Integer> l = List.of(1, 2, 1);
        assertThrows(IllegalArgumentException.class, () -> {
            BaseballNumbers numbers = new BaseballNumbers(l);
        });
    }

    @ValueSource(ints = {-3, -2, -1, 0, 10, 11, 100})
    @ParameterizedTest
    void 잘못된입력_범위벗어남ㅓ(int n) {
        List<Integer> l = List.of(n, 2, 1);
        assertThrows(IllegalArgumentException.class, () -> {
            BaseballNumbers numbers = new BaseballNumbers(l);
        });
    }

    @Test
    void 잘못된입력_사이즈부족함() {
        List<Integer> l = List.of(1, 2);
        assertThrows(IllegalArgumentException.class, () -> {
            BaseballNumbers numbers = new BaseballNumbers(l);
        });
    }

    @Test
    void 잘못된입력_사이즈너무큼() {
        List<Integer> l = List.of(1, 2, 3, 4);
        assertThrows(IllegalArgumentException.class, () -> {
            BaseballNumbers numbers = new BaseballNumbers(l);
        });
    }

    @Test
    void compare() {
    }

    @Test
    void strikeCount() {
    }

    @Test
    void ballCount() {
    }
}