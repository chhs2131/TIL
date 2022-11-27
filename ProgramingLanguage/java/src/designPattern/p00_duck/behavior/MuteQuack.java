package designPattern.p00_duck.behavior;

public class MuteQuack implements QuackBehavior{
    public void quack() {
        System.out.println("(...)");
    }
}
