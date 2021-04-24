#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int T[10000], N, tot, busca;
    while(cin >> N){
        tot = 0;
        for(int i = 0; i < N; i++){
            int a, b;
            cin >> a >> b;
            for(int j = a; j <= b; j++){ T[tot++] = j; }
        }
        sort(T, T+tot);
        cin >> busca;
        int encontrou = 0, inicio = 0, fim = 0;
        while(inicio < tot){ if(T[inicio++] == busca){ encontrou = 1; inicio--; break; } }
        if(encontrou){
            fim = inicio;
            while(fim < tot && T[++fim] == busca);
            cout << busca << " found from " << inicio << " to " << fim-1 << '\n';
        }
        else{ cout << busca << " not found" << '\n'; }
    }
	return 0;
}
