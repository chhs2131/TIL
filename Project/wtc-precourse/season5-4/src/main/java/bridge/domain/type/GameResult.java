package bridge.domain.type;

public class GameResult {
    private int tryCount = 1;
    private GameProgress progress = GameProgress.PLAYING;
    private Bridge userPick;

    public void updateProgress(Bridge userPick, Bridge bridge) {
        boolean rightWay = userPick.isRightWay(bridge);
        if (!rightWay) {
            setProgress(GameProgress.FAILED);
        }
        if (userPick.equals(bridge)) {
            setProgress(GameProgress.COMPLETED);
        }
        this.userPick = userPick;
    }

    public boolean isPlaying() {
        return this.getProgress() == GameProgress.PLAYING;
    }

    public boolean isFailed() {
        return this.getProgress() == GameProgress.FAILED;
    }

    public GameProgress getProgress() {
        return progress;
    }

    public Bridge getUserPick() {
        return userPick;
    }

    public int getTryCount() {
        return tryCount;
    }

    public void retry() {
        setProgress(GameProgress.PLAYING);
        addTryCount();
    }
    private void addTryCount() {
        tryCount++;
    }

    private void setProgress(GameProgress progress) {
        this.progress = progress;
    }
}
