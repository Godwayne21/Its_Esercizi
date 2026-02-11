# include <stdio.h>

int main () {
    int x = 1;

    do x++;
    while (x<10);

    printf("%d\n",x);
}