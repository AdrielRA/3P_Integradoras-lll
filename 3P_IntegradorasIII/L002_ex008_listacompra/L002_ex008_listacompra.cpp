#include <iostream>

using namespace std;

int main()
{
	int N;
	char produtos[1000][20];

	cin >> N;
	getchar();

	for (int i = 0; i < N; i++)
	{
		char produto[20000];
		gets_s(produto);

		int cont = 0, j = 0, k = 0, max = strlen(produto);
		while (cont < max)
		{
			if (produto[cont] != ' ') { produtos[k][j] = produto[cont]; j++; }
			else { produtos[k][j] = '\0'; k++; j = 0; }
			cont++;
		}
		produtos[k][j] = '\0';

		for (int l = 0; l <= k; l++)
		{
			for (int m = l + 1; m <= k; m++)
			{
				if (strcmp(produtos[l], produtos[m]) == 0) {
					for (int n = m; n < k; n++)
					{
						strcpy_s(produtos[n], produtos[n + 1]);
					}
					k--;
					l--;
				}
			}
		}

		for (int l = 0; l < k; l++)
		{
			for (int m = l + 1; m <= k; m++)
			{
				if(strcmp(produtos[l], produtos[m]) > 0){
					char aux[20];
					strcpy_s(aux, produtos[m]);
					for (int n = m; n > l; n--)
					{
						strcpy_s(produtos[n], produtos[n - 1]);
					}
					strcpy_s(produtos[l], aux);
				}
			}
		}

		for (int l = 0; l <= k; l++)
		{
			cout << produtos[l] << '\n';
		}

	}

	system("pause");

	return 0;
}