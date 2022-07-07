import java.util.ArrayList;
import java.util.List;

public class ListRemoveIf {
    private List<Integer> li = new ArrayList<>();

    ListRemoveIf(int limit) {
        for(int i = 0; i < limit; i++) {
            li.add(i);
        }
    }

    void printLi() {
        System.out.println(li);
    }
    List<Integer> getLi() {
        return li;
    }
    void removeIfEven() {
        li.removeIf(num -> num % 2 == 0);
    }
    void removeIfOdd() {
        li.removeIf(num -> num % 2 == 1);
    }
}
