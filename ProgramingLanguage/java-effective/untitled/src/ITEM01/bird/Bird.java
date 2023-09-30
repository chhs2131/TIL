package ITEM01.bird;

public class Bird {
    void quack() {
    }

    public static Bird duck() {
        return new Duck();
    }

    public static Bird chicken() {
        return new Chicken();
    }

//    public static Bird mouse() {
//        return new Mouse();
//    }
}
