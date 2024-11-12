#include <cs50.h>
#include <stdio.h>

int divide(int a, int b);

int main(void)
{
    // ask user for x 
    int x = get_int("What's x? ");

    // ask user for y
    int y = get_int("What's y? ");

    // print the result
    // eg 3/2 = 1.5 but result in 1
    printf("%i\n", divide(x, y));
    return 0;
}

int divide(int a, int b)
{
    return a / b;
}