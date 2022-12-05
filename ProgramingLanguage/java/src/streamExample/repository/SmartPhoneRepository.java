package streamExample.repository;

import streamExample.domain.Manufacturer;
import streamExample.domain.SmartPhone;

import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public class SmartPhoneRepository {
    private List<SmartPhone> smartPhones;
    //new SmartPhone("갤럭시S2",Manufacturer.SAMSUNG, 1),
    //new SmartPhone("갤럭시S10e", Manufacturer.SAMSUNG, 10),
    //new SmartPhone("갤럭시S22", Manufacturer.SAMSUNG, 100),
    //new SmartPhone("갤럭시FOLD3", Manufacturer.SAMSUNG, 300),
    //new SmartPhone("갤럭시Z플립4", Manufacturer.SAMSUNG, 119),
    //new SmartPhone("아이폰12", Manufacturer.APPLE, 100),
    //new SmartPhone("아이폰13", Manufacturer.APPLE, 150),
    //new SmartPhone("아이폰14", Manufacturer.APPLE, 200),
    //new SmartPhone("아이폰SE", Manufacturer.APPLE, 10),
    //new SmartPhone("LG V50", Manufacturer.LG, 70),
    //new SmartPhone("LG 롤러블", Manufacturer.LG, 250),
    //new SmartPhone("샤오미 홍미 노트11", Manufacturer.XIAOMI, 27),
    //new SmartPhone("샤오미 홍미 노트8", Manufacturer.XIAOMI, 18)

    public SmartPhoneRepository(List<SmartPhone> smartPhones) {
        this.smartPhones = smartPhones;
    }

// 애플이 제조한 핸드폰들을 알려주세요.
public List<SmartPhone> findByManufacturerName(String name) {
    Manufacturer manufacturer = Manufacturer.of(name);
    return smartPhones.stream()
            .filter(phone -> phone.getManufacturers() == manufacturer)
            .collect(Collectors.toList());
}

// 예산 범위안에서 어떤 핸드폰을 살 수 있는지 알고싶어요.
public List<SmartPhone> findByPriceRange(int low, int high) {
    return smartPhones.stream()
            .filter(phone -> low <= phone.getPrice() && phone.getPrice() <= high)
            .sorted(Comparator.comparing(SmartPhone::getPrice))
            .collect(Collectors.toList());
}

// 가장 비싼 핸드폰은 뭔가요?
public SmartPhone findMostExpansiveSmartPhone() {
    return smartPhones.stream()
            .max(Comparator.comparingInt(SmartPhone::getPrice))
            .orElse(null);
}

// 가장 저렴한 핸드폰은 뭔가요?
public SmartPhone findMostCheapSmartPhone() {
    return smartPhones.stream()
            .max(Comparator.comparingInt(phone -> -phone.getPrice()))
            //.max(Comparator.comparingInt(SmartPhone::getPrice))
            .orElse(null);
}

// LG 롤러블은 얼마에요?
public int findPriceByDeviceName(String deviceName) {
    return smartPhones.stream()
            .filter(phone -> phone.isSameDevice(deviceName))
            .map(SmartPhone::getPrice)
            .findFirst()
            .orElseThrow(() -> new IllegalArgumentException(""));
}

// 이 매장에 있는 스마트폰에 가격을 합치면 얼마인가요?
public int findTotalPrice() {
    return smartPhones.stream()
            .map(SmartPhone::getPrice)
            .reduce(0, Integer::sum);
}

// 스마트폰 제조사들이 뭐잇는지 알려주세요.
public List<String> findAllManufacturerName() {
    return smartPhones.stream()
            .map(SmartPhone::getManufacturers)
            .map(Manufacturer::toString)
            .distinct()
            .collect(Collectors.toList());
}

// 이 매장에는 10만원도 안하는 스마트폰이 있을까?
public boolean findAnyLowerPrice(int price) {
    return smartPhones.stream()
            .anyMatch(phone -> phone.getPrice() <= price);
}
}
