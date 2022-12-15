package bridge.domain.type;

public enum GameProgress {
    PLAYING("진행중"), COMPLETED("성공"), FAILED("실패");

    private String name;

    GameProgress(String name) {
        this.name = name;
    }

    public boolean isFailed() {
        return this == FAILED;
    }

    public String getName() {
        return name;
    }
}
