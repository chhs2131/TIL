package bridge.view;

import bridge.domain.type.Command;
import bridge.domain.type.Direction;
import camp.nextstep.edu.missionutils.Console;

/**
 * 사용자로부터 입력을 받는 역할을 한다.
 */
public class InputView {
    private static final int MINIMUM_BRIDGE_SIZE = 3;
    private static final int MAXIMUM_BRIDGE_SIZE = 20;

    /**
     * 다리의 길이를 입력받는다.
     */
    public static int readBridgeSize() {
        String input = Console.readLine();
        try {
            int bridgeSize = Integer.parseInt(input);
            validateBridgeSize(bridgeSize);
            return bridgeSize;
        } catch (NumberFormatException e) {
            throw new IllegalArgumentException("숫자가 아닌 형식이 들어왔습니다.");
        }
    }

    private static void validateBridgeSize(int bridgeSize) {
        if (bridgeSize < MINIMUM_BRIDGE_SIZE) {
            throw new IllegalArgumentException(String.format(
                    "The bridge size must be at least %d", MINIMUM_BRIDGE_SIZE));
        }
        if (bridgeSize > MAXIMUM_BRIDGE_SIZE) {
            throw new IllegalArgumentException(String.format(
                    "The bridge size must be at most %d", MAXIMUM_BRIDGE_SIZE));
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
