package baseball.domain;

public class GameResult {
    private static final int NUMBERS_SIZE = 3;

    private int strike = 0;
    private int ball = 0;
    private GameProgress progress = GameProgress.PLAYING;

    public void addStrike() {
        strike++;
        checkWinning();
    }

    private void checkWinning() {
        if (strike == NUMBERS_SIZE) {
            progress = GameProgress.WINNING;
        }
    }

    public void addBall() {
        ball++;
    }

    public int getStrike() {
        return strike;
    }

    public int getBall() {
        return ball;
    }
    public GameProgress getProgress() {
        return progress;
    }

    @Override
    public String toString() {
        String result = "";
        result += strike;
        result += ball;
        result += progress.toString();
        return result;
    }
}
