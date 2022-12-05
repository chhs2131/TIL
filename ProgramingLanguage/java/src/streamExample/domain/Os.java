package streamExample.domain;

import java.util.Arrays;
import java.util.List;

public enum Os {
    ANDROID("안드로이드", List.of(Manufacturer.SAMSUNG, Manufacturer.LG, Manufacturer.XIAOMI)),
    IOS("IOS", List.of(Manufacturer.APPLE));

    private final String name;
    private final List<Manufacturer> manufacturers;

    Os(String name, List<Manufacturer> manufacturers) {
        this.name = name;
        this.manufacturers = manufacturers;
    }

    public static Os of(Manufacturer manufacturer) {
        return Arrays.stream(Os.values())
                .filter(os -> os.getManufacturers().contains(manufacturer))
                .findAny()
                .orElse(null);
    }

    private List<Manufacturer> getManufacturers() {
        return manufacturers;
    }
}
