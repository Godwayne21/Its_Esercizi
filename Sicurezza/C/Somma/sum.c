# include <stdio.h>

int main () {
    int primo_num;
    int secondo_num;

    printf ("Dammi un numero: \n");
    scanf("%d", &primo_num);

    printf ("Dammi un altro numero: \n");
    scanf ("%d", &secondo_num);

    int somma = primo_num + secondo_num;

    printf("La somma di %d e %d = %d\n",primo_num,secondo_num, somma);

    return 0;
}