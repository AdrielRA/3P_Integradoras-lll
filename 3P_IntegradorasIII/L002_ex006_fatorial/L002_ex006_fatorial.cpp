#include <iostream>

using namespace std;

int Fatorial(int n) {
	if (n > 1) return n * Fatorial(n - 1);
	else return 1;
}

int main()
{
	int num, cont = 0;

	cin >> num;

	while (num > 0) {
		int fator = 1, fatorado = Fatorial(fator);
		while (Fatorial(fator + 1) <= num) {
			fator++;
			fatorado = Fatorial(fator);
		}
		cont++;
		num -= fatorado;
	}

	cout << cont << '\n';

	return 0;
}