package racingcar.view;

import racingcar.domain.Car;

import java.util.List;

public class OutputView {
    public static void printInputCarNameGuide() {
        System.out.println("경주할 자동차 이름을 입력하세요.(이름은 쉼표(,) 기준으로 구분)");
    }

    public static void printInputDestinationGuide() {
        System.out.println("시도할 회수는 몇회인가요?");
    }

    public static void printRacingResult(List<Car> cars) {
        System.out.println("실행 결과");
        for (Car car : cars) {
            printCarInformation(car);
        }
    }

    private static void printCarInformation(Car car) {
        System.out.print(car.getName() + " : ");
        for (int i = 0; i < car.getPosition(); i++) {
            System.out.print("-");
        }
        System.out.println("");
    }

    public static void printWinner(List<String> winners) {
        String sentence = String.join(", ", winners);
        System.out.println("최종 우승자 : " + sentence);
    }

    public static void printException(String e) {
        System.out.println("[ERROR] " + e);
    }
}
