package designPattern.p00_duck;

import designPattern.p00_duck.behavior.FlyNoWay;
import designPattern.p00_duck.behavior.Quack;
import designPattern.p00_duck.behavior.QuackBehavior;

public class ModelDuck extends Duck {
    public void display() {
        System.out.println("저는 모형오리입니다. []-[]");
    }

    public ModelDuck() {
        flyBehavior = new FlyNoWay();
        quackBehavior = new Quack();
    }
}
