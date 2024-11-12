#include <cs50.h>
#include <stdio.h>

void meow(int n);

int main(void)
{
    meow(3);
    return 0;
}

// meow some number of times
void meow(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("meow\n");
    }
    
}