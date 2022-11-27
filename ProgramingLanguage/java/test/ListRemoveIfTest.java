import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class ListRemoveIfTest {

    @Test
    void test_even_10() {
        ListRemoveIf lri = new ListRemoveIf(10);
        lri.removeIfEven();

        List<Integer> li = new ArrayList<Integer>() {{
            add(1);
            add(3);
            add(5);
            add(7);
            add(9);
        }};

        assertEquals(li, lri.getLi());
    }

    @Test
    void test_even_20() {
        ListRemoveIf lri = new ListRemoveIf(20);
        lri.removeIfEven();

        List<Integer> li = Stream.of(1, 3, 5, 7, 9, 11, 13, 15, 17, 19).collect(Collectors.toList());

        assertEquals(li, lri.getLi());
    }
    @Test
    void test_odd_20() {
        ListRemoveIf lri = new ListRemoveIf(20);
        lri.removeIfOdd();

        List<Integer> li = Stream.of(0, 2, 4, 6, 8, 10, 12, 14, 16, 18).collect(Collectors.toList());

        assertEquals(li, lri.getLi());
    }
}
