#include <stdio.h>
#include <stdlib.h>

int main ()
{
	int i;		//contador de quebra de linha
	int j;		//contador das bolinhas
	int a;		//contador para o espaçamento
	int tamanho, tronco;
		
	printf("qual o tamanho a arvore vai ter? \n >> ");
	scanf("%d", &tamanho);
	system("cls");
	printf("\n");
	tronco = tamanho / 2;

	for (i = 0; i <= tamanho - 1; i++) {
		for (a = tamanho; a >= i; a--){
			printf(" ");
		}
			
		for (j = 0; j <= i * 2; j++) {
			printf("*");
		}
		printf("\n");
	}
	
	for (a = 0; a <= tamanho-1; a++){
		printf(" ");
	}
	
	for (j = 0; j <= tronco; j++){
		printf("|");
	}

}