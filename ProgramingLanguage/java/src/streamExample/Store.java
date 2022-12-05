package streamExample;

import streamExample.domain.Manufacturer;
import streamExample.domain.SmartPhone;
import streamExample.repository.SmartPhoneRepository;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Store {
    private final SmartPhoneRepository smartPhoneRepository;

    public Store() {
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
        smartPhoneRepository = new SmartPhoneRepository(smartPhones);
    }

    public void printAll() {
        System.out.println(smartPhoneRepository.findByManufacturerName("애플").toString());
        System.out.println(smartPhoneRepository.findByPriceRange(50,150).toString());
        System.out.println(smartPhoneRepository.findPriceByDeviceName("LG 롤러블"));
        System.out.println(smartPhoneRepository.findMostExpansiveSmartPhone());
        System.out.println(smartPhoneRepository.findMostCheapSmartPhone());
        System.out.println(smartPhoneRepository.findTotalPrice());
        System.out.println(smartPhoneRepository.findAllManufacturerName());
        System.out.println(smartPhoneRepository.findAnyLowerPrice(10));
    }
}
