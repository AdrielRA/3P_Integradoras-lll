#include <iostream>
#include <string.h>
using namespace std;

int main() {
    char Linha[100000], * result;
    int lado, pos_cont;
    while (cin >> Linha) {
        result = new char[strlen(Linha)];
        int tam = strlen(Linha), ultimo = 0;
        lado = 0; pos_cont = 0;
        for (int i = 0; Linha[i] != '\0'; i++) {
            if (Linha[i] == ']') { lado = 1; pos_cont = 0; }
            else if (Linha[i] == '[') { lado = 0; pos_cont = 0; }
            else if (Linha[i] != '[' && Linha[i] != ']') {
                if(!lado){
                    result--;
                    for(int j = 0; j < pos_cont; j++){ result[j] = result[j+1]; }
                    result[pos_cont] =  Linha[i];
                }
                else{ *(result + ultimo) = Linha[i]; }
                ultimo++;
                pos_cont += 1;
            }
        }
        result[ultimo] = '\0';
        cout << result << '\n';
    }
    return 0;
}
