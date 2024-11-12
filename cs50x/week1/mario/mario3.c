#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // prompt the user for positive integer
    int n = 0;
    do
    {
        n = get_int("Size: ");
    } 
    while (n < 1);
    
    // print n by n grid of bricks
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("#");
        }
        printf("\n");
    } 
    return 0;
}