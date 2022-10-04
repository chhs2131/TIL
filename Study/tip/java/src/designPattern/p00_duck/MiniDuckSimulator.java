package designPattern.p00_duck;

import designPattern.p00_duck.behavior.FlyRocketPowered;

public class MiniDuckSimulator {
    public static void main(String[] args) {
        Duck mallard = new MallardDuck();
        mallard.display();
        mallard.performQuack();
        mallard.performFly();

        Duck model = new ModelDuck();
        model.performFly();
        model.setFlyBehavior(new FlyRocketPowered());
        model.performFly();
    }
}

//저는 물오리입니다. ^^
//꽥꽥
//fly!!!!!!!!!!!
