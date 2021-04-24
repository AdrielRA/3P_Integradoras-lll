#include <iostream>

using namespace std;

int main() {

	int Hora, Velocidade;

	cin >> Hora;
	cin >> Velocidade;

	printf("%.3f\n", (float)Hora * Velocidade / 12);

	return 0;
}