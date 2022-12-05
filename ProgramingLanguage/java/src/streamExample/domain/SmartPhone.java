package streamExample.domain;

public class SmartPhone {
    private final String name;
    private final Os os;
    private final Manufacturer manufacturer;
    private final int price;  // 단위 만원

    public SmartPhone(String name, Manufacturer manufacturer, int price) {
        this.name = name;
        this.manufacturer = manufacturer;
        this.price = price;
        this.os = Os.of(manufacturer);
    }

    @Override
    public String toString() {
        return name + "(" + os +") " + manufacturer + " - " + price + "만원";
    }

    public Manufacturer getManufacturers() {
        return manufacturer;
    }

    public int getPrice() {
        return price;
    }

    public boolean isSameDevice(String deviceName) {
        return name.equals(deviceName);
    }
}
