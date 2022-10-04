package designPattern.p00_duck;

import designPattern.p00_duck.behavior.FlyWithWings;
import designPattern.p00_duck.behavior.Quack;

public class MallardDuck extends Duck {
    public void display() {
        System.out.println("저는 물오리입니다. ^^");
    }

    // interface로 선언된 객체에 실제 구현체를 넣어준다.
    public MallardDuck() {
        quackBehavior = new Quack();
        flyBehavior = new FlyWithWings();
    }
}
