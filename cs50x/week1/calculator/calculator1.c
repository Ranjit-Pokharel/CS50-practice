#include <cs50.h>
#include <stdio.h>

int add(int a, int b);

int main(void)
{
    // ask user for x 
    int x = get_int("What's x? ");

    // ask user for y
    int y = get_int("What's y? ");

    // print the result
    printf("%i\n", add(x, y));
    return 0;
}

int add(int a, int b)
{
    return a + b;
}