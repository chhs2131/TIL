package designPattern.p00_duck;

import designPattern.p00_duck.behavior.FlyBehavior;
import designPattern.p00_duck.behavior.QuackBehavior;

public abstract class Duck {
    // interface 받기
    FlyBehavior flyBehavior;
    QuackBehavior quackBehavior;

    public Duck() {}

    // 인터페이스안에 메소드를 실행한다.
    public abstract void display();
    public void performFly() {
        flyBehavior.fly();
    }
    public void performQuack() {
        quackBehavior.quack();
    }

    // setter를 통해 동적으로 행동을 지정하기
    public void setFlyBehavior(FlyBehavior flyBehavior) {
        this.flyBehavior = flyBehavior;
    }
    public void setQuackBehavior(QuackBehavior quackBehavior) {
        this.quackBehavior = quackBehavior;
    }
}
