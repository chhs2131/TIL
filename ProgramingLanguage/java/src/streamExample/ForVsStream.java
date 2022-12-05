package streamExample;

import streamExample.domain.Manufacturer;
import streamExample.domain.SmartPhone;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class ForVsStream {
    public static void main(String[] args) {
        filterOnlyApple();
    }

    public static void filterOnlyApple() {
        List<SmartPhone> smartPhones = List.of(
                new SmartPhone("갤럭시S2", Manufacturer.SAMSUNG, 1),
                new SmartPhone("갤럭시S10e", Manufacturer.SAMSUNG, 10),
                new SmartPhone("갤럭시S22", Manufacturer.SAMSUNG, 100),
                new SmartPhone("갤럭시FOLD3", Manufacturer.SAMSUNG, 300),
                new SmartPhone("갤럭시Z플립4", Manufacturer.SAMSUNG, 119),
                new SmartPhone("아이폰12", Manufacturer.APPLE, 100),
                new SmartPhone("아이폰13", Manufacturer.APPLE, 150),
                new SmartPhone("아이폰14", Manufacturer.APPLE, 200),
                new SmartPhone("아이폰SE", Manufacturer.APPLE, 10),
                new SmartPhone("LG V50", Manufacturer.LG, 70),
                new SmartPhone("LG 롤러블", Manufacturer.LG, 250),
                new SmartPhone("샤오미 홍미 노트11", Manufacturer.XIAOMI, 27),
                new SmartPhone("샤오미 홍미 노트8", Manufacturer.XIAOMI, 18)
        );

        List<SmartPhone> result;

        // 반복문 기본형
        result = filterOnlyAppleFor1(smartPhones);
        System.out.println(result.toString());

        // 반복문 누적자
        result = filterOnlyAppleFor2(smartPhones);
        System.out.println(result.toString());

        // 스트림
        result = filterOnlyAppleStream(smartPhones);
        System.out.println(result.toString());
    }

    private static List<SmartPhone> filterOnlyAppleFor1(List<SmartPhone> smartPhones) {
        List<SmartPhone> result = new ArrayList<>();
        for (int i = 0; i < smartPhones.size(); i++) {
            SmartPhone smartPhone = smartPhones.get(i);
            if (smartPhone.getManufacturers() == Manufacturer.APPLE) {
                result.add(smartPhone);
            }
        }
        return result;
    }

    private static List<SmartPhone> filterOnlyAppleFor2(List<SmartPhone> smartPhones) {
        List<SmartPhone> result = new ArrayList<>();
        for (SmartPhone smartPhone : smartPhones) {
            if (smartPhone.getManufacturers() == Manufacturer.APPLE) {
                result.add(smartPhone);
            }
        }
        return result;
    }

    private static List<SmartPhone> filterOnlyAppleStream(List<SmartPhone> smartPhones) {
        return smartPhones.stream()
                .filter(smartPhone -> smartPhone.getManufacturers() == Manufacturer.APPLE)
                .collect(Collectors.toList());
    }
}
