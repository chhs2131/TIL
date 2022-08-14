// 자바 숏코딩은 어떻게 하는걸까요?
import java.util.*;
import java.io.IOException;

interface Main {
    static void main(String[] q) throws IOException {
        Scanner i = new Scanner(System.in);
        int n = i.nextInt();
        for (int l = 0; l < n; l++) {
            byte[] a = new byte[99];
            int b = System.in.read(a);
            a[0] &= ~32;
            System.out.print(new String(a, 0, b));
        }
    }
}
