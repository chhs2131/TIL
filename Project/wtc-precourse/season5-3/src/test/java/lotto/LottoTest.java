package lotto;

import lotto.domain.type.Lotto;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.util.List;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import org.junit.jupiter.params.provider.ValueSource;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

class LottoTest {
    @DisplayName("로또 번호의 개수가 6개가 넘어가면 예외가 발생한다.")
    @Test
    void createLottoByOverSize() {
        assertThatThrownBy(() -> new Lotto(List.of(1, 2, 3, 4, 5, 6, 7)))
                .isInstanceOf(IllegalArgumentException.class);
    }

    @DisplayName("로또 번호에 중복된 숫자가 있으면 예외가 발생한다.")
    @Test
    void createLottoByDuplicatedNumber() {
        // TODO: 이 테스트가 통과할 수 있게 구현 코드 작성
        assertThatThrownBy(() -> new Lotto(List.of(1, 2, 3, 4, 5, 5)))
                .isInstanceOf(IllegalArgumentException.class);
    }

    @ValueSource(ints = {6, 7, 8, 9, 10, 11, 12, 13, 22, 23, 24, 25, 26, 37, 38, 39, 40, 41, 42, 43, 44, 45})
    @ParameterizedTest
    void 로또생성_범위내숫자_정상(int n) {
        List<Integer> numbers = List.of(1, 2, 3, 4, 5, n);
        Lotto l = new Lotto(numbers);
        assertThat(l.getNumbers()).isEqualTo(numbers);
    }

    @ValueSource(ints = {-100, -1, 0, 46, 100, 1000})
    @ParameterizedTest
    void 로또생성_범위밖숫자_정상(int n) {
        assertThatThrownBy(() -> {
            List<Integer> numbers = List.of(1, 2, 3, 4, 5, n);
            Lotto l = new Lotto(numbers);
        }).isInstanceOf(IllegalArgumentException.class);
    }
}
