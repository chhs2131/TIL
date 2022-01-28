#include <iostream>
#include <cmath>
using namespace std;

class Solution2 {
public:
	int reverse(int x) {
		int rev = 0;
		while (x != 0) {
			int pop = x % 10;
			x /= 10;
			if (rev > INT_MAX / 10 || (rev == INT_MAX / 10 && pop > 7)) return 0;
			if (rev < INT_MIN / 10 || (rev == INT_MIN / 10 && pop < -8)) return 0;
			rev = rev * 10 + pop;
		}
		return rev;
	}
};

class Solution {
public:
	int reverse(int x) {
		//INT_MIN인 경우 0을 반환.
		if (x == INT_MIN)
			return 0;

		//마이너스인지 확인해서 마이너스면 양수로 전환
		bool minus = false;
		if (x < 0) {
			minus = true;
			x *= -1;
		}

		//자릿수 확인
		int digits = (int)log10(x);

		//숫자 뒤집기 실행.
		int result = 0;
		bool max_check = true;
		int intmax[10] = { 2,1,4,7,4,8,3,6,4,7 };
		for (int i = 0; i <= digits; i++) {
			int new_num = x % 10;

			//x가 10억 단위인 경우, 진행시 문제가 되는지 확인 (int => 32bit)
			if (digits >= 9) {
				if (max_check) {
					if (new_num > intmax[i])
						return 0;
					else if (new_num == intmax[i])
						max_check = true;
					else
						max_check = false;
				}
			}

			result += new_num * (int)pow(10, digits - i);
			x /= 10;
		}

		//마이너스 숫자였던 경우 마이너스 붙여주기
		if (minus)
			result *= -1;

		return result;
	}
};

int main() {
	Solution S;
	cout << S.reverse(123) << endl << endl;
	cout << S.reverse(-123) << endl << endl;
	cout << S.reverse(120) << endl << endl;
	cout << S.reverse(0) << endl << endl;
	cout << S.reverse(5) << endl << endl;
	cout << S.reverse(1534236469) << endl << endl;
	cout << S.reverse(-2147483412) << endl << endl;
	cout << S.reverse(INT_MIN) << endl << endl;
	cout << S.reverse(2147483647) << endl << endl;

	int aaa;
	cin >> aaa;
	return 0;
}
