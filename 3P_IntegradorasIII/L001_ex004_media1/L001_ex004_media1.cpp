#include <iostream>

using namespace std;

int main() {

	double A, B;
	cin >> A;
	cin >> B;

	double result = ((A * 3.5) + (B * 7.5)) / 11;

	printf("MEDIA = %0.5lf\n", result);

	return 0;
}