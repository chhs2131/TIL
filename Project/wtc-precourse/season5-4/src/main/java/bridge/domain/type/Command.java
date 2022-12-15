package bridge.domain.type;

import java.util.Arrays;
import java.util.Objects;

public enum Command {
    RESTART("R", true),
    QUIT("Q", false);

    private final String command;
    private final boolean isRestart;

    Command(String command, boolean isRestart) {
        this.command = command;
        this.isRestart = isRestart;
    }

    public boolean isRestart() {
        return this == RESTART;
    }

    public static Command from(String command) {
        return Arrays.stream(Command.values())
                .filter(c -> Objects.equals(c.getCommand(), command))
                .findAny()
                .orElseThrow(() -> new IllegalArgumentException("해당하는게 없습니다. " + command));
    }

    private String getCommand() {
        return command;
    }
}
