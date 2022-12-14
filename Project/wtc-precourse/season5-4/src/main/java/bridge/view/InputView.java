package bridge.view;

import bridge.domain.type.Command;
import bridge.domain.type.Direction;
import camp.nextstep.edu.missionutils.Console;

/**
 * 사용자로부터 입력을 받는 역할을 한다.
 */
public class InputView {
    /**
     * 다리의 길이를 입력받는다.
     */
    public static int readBridgeSize() {
        String input = Console.readLine();
        try {
            return Integer.parseInt(input);
        } catch (NumberFormatException e) {
            throw new IllegalArgumentException("숫자가 아닌 형식이 들어왔습니다.");
        }
    }

    /**
     * 사용자가 이동할 칸을 입력받는다.
     */
    public static Direction readMoving() {
        String input = Console.readLine();
        return Direction.from(input);
    }

    /**
     * 사용자가 게임을 다시 시도할지 종료할지 여부를 입력받는다.
     */
    public static Command readGameCommand() {
        String input = Console.readLine();
        return Command.from(input);
    }
}
