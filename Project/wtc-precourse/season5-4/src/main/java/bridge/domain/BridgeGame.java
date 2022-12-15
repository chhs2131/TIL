package bridge.domain;

import bridge.BridgeMaker;
import bridge.BridgeNumberGenerator;
import bridge.BridgeRandomNumberGenerator;
import bridge.domain.type.Bridge;
import bridge.domain.type.Command;
import bridge.domain.type.Direction;
import bridge.domain.type.GameResult;
import java.util.List;

/**
 * 다리 건너기 게임을 관리하는 클래스
 */
public class BridgeGame {
    private final BridgeNumberGenerator bridgeNumberGenerator = new BridgeRandomNumberGenerator();
    private final BridgeMaker bridgeMaker = new BridgeMaker(bridgeNumberGenerator);
    private Bridge bridge;
    private Bridge userPick = new Bridge();
    private GameResult gameResult = new GameResult();

    // 다리를 만듭니다.
    public void makeBridge(int size) {
        List<String> bridgeInform = bridgeMaker.makeBridge(size);
        bridge = new Bridge(bridgeInform);
        System.out.println(bridge.toString());
    }

    /**
     * 사용자가 칸을 이동할 때 사용하는 메서드
     * <p>
     * 이동을 위해 필요한 메서드의 반환 타입(return type), 인자(parameter)는 자유롭게 추가하거나 변경할 수 있다.
     */
    public GameResult move(Direction direction) {
        userPick.add(direction);
        // 이동 결과 비교 및 상태 업데이트
        gameResult.updateProgress(userPick, bridge);
        return gameResult;
    }

    /**
     * 사용자가 게임을 다시 시도할 때 사용하는 메서드
     * <p>
     * 재시작을 위해 필요한 메서드의 반환 타입(return type), 인자(parameter)는 자유롭게 추가하거나 변경할 수 있다.
     */
    public void retry(Command command) {
        if (command.isRestart()) {
            userPick.clear();
            gameResult.retry();
        }
    }
}
