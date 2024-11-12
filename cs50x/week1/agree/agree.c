#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // ask the user for y for yes and n for no
    char c = get_char("Do you agreee? ");

    if (c == 'Y' || c == 'y')
    {
        printf("Agreed.\n");
    }
    else if (c == 'N' || c == 'n')
    {
        printf("Not Agreed.\n");
    }

    return 0;
}