package lotto.domain.type;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

class PrizeTest {
//    FIRST(6, false, 2000000000),
//    SECOND(5, true, 30000000),
//    THIRD(5, false, 1500000),
//    FOURTH(4, false, 50000),
//    FIFTH(3, false, 5000);

    @CsvSource(value = {"1:false:null", "1:true:null",
            "2:false:null", "2:true:null",
            "3:false:FIFTH", "3:true:FIFTH",
            "4:false:FOURTH", "4:true:FOURTH",
            "5:false:THIRD", "5:true:SECOND",
            "6:false:FIRST", "6:true:FIRST"},
            delimiter = ':', nullValues = {
            "null"})
    @ParameterizedTest
    void from(int count, boolean bonus, Prize prize) {
        Prize test = Prize.from(count, bonus);
        assertThat(test).isEqualTo(prize);
    }

    @Test
    void getMoney() {
        assertThat(Prize.FOURTH.getMoney()).isEqualTo(50000);
    }

    @Test
    void makeSentence() {
        String sentence = Prize.makeSentence(Prize.FOURTH);
        assertThat(sentence).isEqualTo("4개 일치 (50,000원)");
    }
}