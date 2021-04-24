#include <iostream>
#include <string>

using namespace std;

int main()
{
	int qnt_testes;
	cin >> qnt_testes;
	getchar();

	for (int i = 0; i < qnt_testes; i++)
	{
		char str1[50], str2[50];

		gets_s(str1); gets_s(str2);

		char maior[50], menor[50];
		int tam_str1 = strlen(str1), tam_str2 = strlen(str2);

		if(tam_str1 >= tam_str2){
			strcpy_s(maior, str1);
			strcpy_s(menor, str2);
		}
		else {
			strcpy_s(maior, str2);
			strcpy_s(menor, str1);
		}

		tam_str1 = strlen(maior), tam_str2 = strlen(menor);
		string result = "";

		for (int j = 0; j < tam_str2; j++)
		{
			char aux[3];
			aux[0] = str1[j];
			aux[1] = str2[j];
			aux[2] = '\0';
			result = result + aux;
		}
		for (int j = tam_str2; j < tam_str1; j++)
		{
			result = result + maior[j];
		}
		cout << result << '\n';
	}

	return 0;
}