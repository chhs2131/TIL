package lotto.view;

import camp.nextstep.edu.missionutils.Console;

public class InputView {
    public static int readPrice() {
        String input = Console.readLine();
        return Integer.parseInt(input);
    }

    public static void readWinnerNumbers() {
        String input = Console.readLine();
    }

    public static int readBounusNumber() {
        String input = Console.readLine();
        return Integer.parseInt(input);
    }
}
