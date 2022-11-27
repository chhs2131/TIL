import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class HelloWorldTest {
    @Test
    void printHello() {
        String a = "hello";
        assertEquals("hello", a);
    }

    @Test
    void printHelloWrong() {
        String a = "hello";
        assertEquals("hello", a + "zzz");
    }
}
