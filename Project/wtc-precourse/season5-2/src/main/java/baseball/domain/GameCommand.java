package baseball.domain;

import java.util.Arrays;

public enum GameCommand {
    KEEP_PLAYING(1),
    STOP(2);

    private int command;
    GameCommand(int command) {
        this.command = command;
    }

    public boolean isKeepPlaying() {
        return this == KEEP_PLAYING;
    }

    public static GameCommand make(final int command) {
        return Arrays.stream(GameCommand.values())
                .filter(gameCommand -> gameCommand.command == command)
                .findAny()
                .orElseThrow(() -> new IllegalArgumentException("[ERROR] 존재하지 않는 값이 입력되었습니다. 입력:" + command));
    }
}
