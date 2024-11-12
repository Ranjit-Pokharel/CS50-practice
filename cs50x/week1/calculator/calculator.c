#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // ask user for x 
    int x = get_int("What's x? ");

    // ask user for y
    int y = get_int("What's y? ");

    // print the result
    printf("%i\n", x + y);
    return 0;
}