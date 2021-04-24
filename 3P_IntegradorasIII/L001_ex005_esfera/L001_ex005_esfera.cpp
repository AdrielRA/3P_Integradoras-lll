#include <iostream>
#include <math.h>

using namespace std;

int main()
{
	double raio;

	cin >> raio;

	printf("VOLUME = %.3f\n", (4 / 3.0) * 3.14159 * pow(raio, 3));

	return 0;
}