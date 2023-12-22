package lec01;

import java.util.List;

public class MovieReviewMain {
    public static void main(String[] args) {
        // 영화 리뷰 정보 선언
//        MovieReview[] movies = {
//            new MovieReview("인셉션", "인생은 무한 루프"),
//            new MovieReview("어바웃 타임", "인생 시간 영화!")
//        };

        List<MovieReview> movies = List.of(
            new MovieReview("인셉션", "인생은 무한 루프"),
            new MovieReview("어바웃 타임", "인생 시간 영화!")
        );

        // 영화 리뷰 정보 출력
        for (MovieReview movie : movies) {
            System.out.printf("영화 제목: \"%s\", 리뷰: \"%s\"%n", movie.getTitle(), movie.getReview());
        }
    }
}

// [출력 예시]
// 영화 제목: "인셉션", 리뷰: "인생은 무한 루프"
// 영화 제목: "어바웃 타임", 리뷰: "인생 시간 영화!"
