#include <iostream>

using namespace std;

int main() {

	int N, result;
	cin >> N;
	char ** strs = new char*[N];

	for (int i = 0; i < N; i++) {
		strs[i] = new char[3];
		cin >> strs[i];
	}

	for (int i = 0; i < N; i++) {

		char * str = strs[i];

		if (str[2] != str[0]) {
			if (str[1] >= 65 && str[1] <= 90) {
				result = (str[2] - 48) - (str[0] - 48);
			}
			else if (str[1] >= 97 && str[1] <= 122) {
				result = (str[2] - 48) + (str[0] - 48);
			}
		}
		else {
			result = (str[2] - 48) * (str[0] - 48);
		}

		cout << result << '\n';
	}

	return 0;
}