package streamExample.domain;

import java.util.Arrays;

public enum Manufacturer {
    SAMSUNG("삼성"),
    APPLE("애플"),
    LG("LG"),
    XIAOMI("샤오미");

    private String name;

    Manufacturer(String name) {
        this.name = name;
    }

    public static Manufacturer of(String name) {
        return Arrays.stream(Manufacturer.values())
                .filter(m -> m.getName() == name)
                .findAny()
                .orElse(null);
    }

    private String getName() {
        return name;
    }

    @Override
    public String toString() {
        return name;
    }
}
