#include <iostream>
using namespace std;

int main()
{
	int inicio, fim, horas;

	cin >> inicio;
	cin >> fim;

	if (fim <= inicio) { horas += 24 - inicio + fim; }
	else { horas = fim - inicio; }

	cout << "O JOGO DUROU " << horas << " HORA(S)\n";
	return 0;
}