package baseball.domain;

import java.util.Arrays;

public enum GameCommand {
    RESTART(1),
    STOP(2);

    private int command;
    GameCommand(int command) {
        this.command = command;
    }

    public static GameCommand make(final int command) {
        return Arrays.stream(GameCommand.values())
                .filter(gameCommand -> gameCommand.command == command)
                .findAny()
                .orElseThrow(() -> new IllegalArgumentException("[ERROR] hello"));
    }
}
