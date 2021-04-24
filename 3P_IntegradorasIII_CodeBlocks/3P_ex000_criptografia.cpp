#include <iostream>
#include <string.h>
#include <cstdio>

using namespace std;

int main()
{
	int N;
	cin >> N;
	getchar();
	char * strs;
	for (int i = 0; i < N; i++) {
		strs = new char[1000];
		gets(strs);
		char * result = new char[strlen(strs)];
		result = strs;
		for (int j = 0; j < strlen(result); j++) {
			if ((result[j] >= 'A' && result[j] <= 'Z') || (result[j] >= 'a' && result[j] <= 'z')) { result[j] += 3; }
		}
		char * aux = new char[strlen(result)];

		for (int j = 0; j < strlen(result); j++) { aux[j] = result[strlen(result) - (j + 1)]; }
		aux[strlen(result)] = '\0';
		result = aux;

		for (int j = strlen(result) / 2; j < strlen(result); j++) { result[j] -= 1; }

		cout << result << '\n';
	}
	return 0;
}
