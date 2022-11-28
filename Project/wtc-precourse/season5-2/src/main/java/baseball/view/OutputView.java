package baseball.view;

import baseball.domain.GameResult;

public class OutputView {
    private static final int NUMBERS_SIZE = 3;
    public void printWelcome() {
        System.out.println("숫자 야구 게임을 시작합니다.");
    }
    public void printNumbersInputGuide() {
        System.out.print("숫자를 입력해주세요 : ");
    }
    public void printGameResult(GameResult gameResult) {
        String sentence = gameResultSentence(gameResult);
        System.out.println(sentence);
    }
    private String gameResultSentence(GameResult gameResult) {
        if (gameResult.getStrike() == 3) {
            return "3스트라이크\n3개의 숫자를 모두 맞히셨습니다! 게임 종료";
        }
        if (gameResult.getStrike() != 0 && gameResult.getBall() != 0) {
            return gameResult.getBall() + "볼 " + gameResult.getStrike() + "스트라이크";
        }
        if (gameResult.getStrike() != 0) {
            return gameResult.getStrike() + "스트라이크";
        }
        if (gameResult.getBall() != 0) {
            return gameResult.getBall() + "볼";
        }
        return "낫싱";
    }
    public void printContinueGuide() {
        System.out.println("게임을 새로 시작하려면 1, 종료하려면 2를 입력하세요.");
    }
}
