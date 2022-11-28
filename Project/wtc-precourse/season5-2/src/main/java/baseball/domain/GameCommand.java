package baseball.domain;

public enum GameCommand {
    RESTART(1),
    STOP(2);

    private int command;
    GameCommand(int command) {
        this.command = command;
    }
}
