#include <iostream>

using namespace std;

int main()
{
	char mensagem[100], crib[100];

	gets_s(mensagem);
	gets_s(crib);
	int tam_msg = strlen(mensagem), tam_crib = strlen(crib);;
	int cont = 0;
	for (int i = 0; i < tam_msg - tam_crib + 1; i++) {
		char contar = 1;
		for (int j = 0; j < strlen(crib); j++) { if (crib[j] == mensagem[i + j]) { contar = 0; break; } }
		if (contar) { cont++; }
	}

	cout << cont << '\n';

	return 0;
}