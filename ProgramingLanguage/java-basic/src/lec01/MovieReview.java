package lec01;

public class MovieReview {
    private String title;
    private String review;

    public MovieReview(String title, String review) {
        this.title = title;
        this.review = review;
    }

    public String getTitle() {
        return title;
    }

    public String getReview() {
        return review;
    }
}
