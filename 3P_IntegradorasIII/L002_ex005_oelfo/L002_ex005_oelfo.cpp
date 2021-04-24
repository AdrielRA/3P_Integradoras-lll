#include <iostream>

using namespace std;

typedef struct {
	char S[100];
	int P, I;
	float A;
}Rena;

void Ordenar(Rena * renas, Rena rena, int pos) {

	while (pos > 0 && rena.P > renas[pos - 1].P)
	{
		renas[pos] = renas[pos - 1];
		pos--;
	}

	while (pos > 0 && rena.P == renas[pos - 1].P)
	{
		if (rena.I < renas[pos-1].I) {
			renas[pos] = renas[pos - 1];
			pos--;
		}
		else break;
	}

	while (pos > 0 && rena.I == renas[pos - 1].I)
	{
		if (rena.A < renas[pos - 1].A) {
			renas[pos] = renas[pos - 1];
			pos--;
		}
		else break;
	}

	while (pos > 0 && rena.A == renas[pos - 1].A)
	{
		if (strcmp(rena.S, renas[pos - 1].S) < 0) {
			renas[pos] = renas[pos - 1];
			pos--;
		}
		else break;
	}

	renas[pos] = rena;
}

int main()
{
	int T, N, M;

	cin >> T;

	for (int i = 0; i < T; i++)
	{
		cin >> N;
		cin >> M;

		Rena * Renas = new Rena[N];

		for (int j = 0; j < N; j++)
		{
			Rena Rena_Lida;
			cin >> Rena_Lida.S;
			cin >> Rena_Lida.P;
			cin >> Rena_Lida.I;
			cin >> Rena_Lida.A;

			Ordenar(Renas, Rena_Lida, j);
		}
		
		cout << "CENARIO {" << i + 1 << "}\n";
		for (int j = 0; j < M; j++) { cout << j + 1 << Renas[j].S << '\n'; }
	}

	return 0;
}