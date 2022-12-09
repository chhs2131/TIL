package lotto.domain;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.*;

import java.util.List;
import lotto.domain.type.Lotto;
import org.junit.jupiter.api.Test;

class LottoGeneratorTest {

    @Test
    void 로또_n개생성확인_정상() {
        List<Lotto> lottos = LottoGenerator.generateLottos(10000);
        assertThat(lottos.size()).isEqualTo(10000);
    }
}