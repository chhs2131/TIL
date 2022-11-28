package baseball.domain;

public enum GameProgress {
    PLAYING, WINNING;

    public static boolean isWinning(final GameProgress progress) {
        if (progress == WINNING) {
            return true;
        }
        return false;
    }
}
