#include <iostream>

using namespace std;

int main()
{
	int qnt_vagoes;

	do
	{
		cin >> qnt_vagoes;

		if (qnt_vagoes) {
			int * trem = new int[qnt_vagoes];
			do
			{
				for (int i = 0; i < qnt_vagoes; i++) {
					cin >> trem[i];
					if (i == 0 && !trem[i]) { break; }
				}
				if (trem[0] != 0) {
					if (trem[0] == 1 || trem[qnt_vagoes - 1] == 1) { cout << "Yes\n"; }
					else { cout << "No\n"; }
				}
				else { cout << " \n"; }

			} while (trem[0]);
		}

	} while (qnt_vagoes != 0);

	return 0;
}