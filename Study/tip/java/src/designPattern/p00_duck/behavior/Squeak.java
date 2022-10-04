package designPattern.p00_duck.behavior;

public class Squeak implements QuackBehavior{
    public void quack() {
        System.out.println("삑삑(장난감 오리소리)");
    }
}
