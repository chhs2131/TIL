package lotto.domain;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;
import static org.junit.jupiter.api.Assertions.*;

import java.util.List;
import lotto.domain.type.Lotto;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

class LottoGameTest {
    LottoGame game;

    @BeforeEach
    void beforeEach() throws Exception {
        game = new LottoGame();
    }

    @ValueSource(ints = {1000, 2000, 3000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000})
    @ParameterizedTest
    void buyLotto_구매할금액로또발행_정상(int money) {
        List<Lotto> lottos = game.buyLotto(money);
        assertThat(lottos.size()).isEqualTo(money/1000);
    }

    @ValueSource(ints = {-5000, 0, 1, 10, 100, 999, 1001, 12345, 98765, 99999})
    @ParameterizedTest
    void buyLotto_구매할금액로또발행_예외(int money) {
        assertThatThrownBy(() -> {
            List<Lotto> lottos = game.buyLotto(money);
        }).isInstanceOf(IllegalArgumentException.class);
    }
}