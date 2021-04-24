#include <iostream>

using namespace std;

int main()
{
	int J, R, * total;

	cin >> J; cin >> R;
	total = new int[J];
	for (int i = 0; i < J; i++) { total[i] = 0; }

	for (int r = 0; r < R; r++)
	{
		for (int j = 0; j < J; j++)
		{
			int pts;
			cin >> pts;
			total[j] += pts;
		}
	}
	int vencedor = 0;
	for (int i = 0; i < J; i++) {
		if (total[i] >= total[vencedor]) {
			vencedor = i;
		}
	}

	cout << vencedor + 1 << '\n';

	return 0;
}