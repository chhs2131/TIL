package lec01;

import java.util.ArrayList;
import java.util.List;

public class ProductOrderMain {
    private static final String PRINT_FORMAT = "상품명: %s, 가격: %s, 수량: %s";

    public static void main(String[] args) {
        // 여러 상품의 주문 정보를 담는 배열 생성
        List<ProductOrder> productOrders = new ArrayList<>();

        // 상품 주문 정보를 ProductOrder 타입의 변수로 받아 저장
        productOrders.add(new ProductOrder("두부", 2000, 2));
        productOrders.add(new ProductOrder("김치", 5000, 1));
        productOrders.add(new ProductOrder("콜라", 1500, 2));

        // 상품 주문 정보와 최종 금액 출력
        int result = 0;
        for (ProductOrder order : productOrders) {
            result += order.getPrice() * order.getQuantity();
            System.out.println(String.format(PRINT_FORMAT, order.getProductName(), order.getPrice(), order.getQuantity()));
        }

        System.out.println(String.format("총 결제 금액: %s", result));
    }
}
