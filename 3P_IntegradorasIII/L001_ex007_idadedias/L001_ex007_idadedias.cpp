#include <iostream>
using namespace std;

int main()
{
	int anos = 0, meses = 0, dias;

	cin >> dias;

	while (dias >= 365) {
		anos++;
		dias -= 365;
	}
	while (dias >= 30) {
		meses++;
		dias -= 30;
	}

	cout << anos << " ano(s)\n";
	cout << meses << " mes(es)\n";
	cout << dias << " dia(s)\n";

	return 0;
}