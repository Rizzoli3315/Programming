#include <cs50.h>
#include <stdio.h>

int coins(int x);

int main(void)
{
    int change;
    do
    {
        change = get_int("Change owed : ");
    }
    while (change < 0);

    printf("%i\n", coins(change));
    
}


int coins(int x)
{
    int penny = 1;
    int nickel = 5;
    int dime = 10;
    int quarter = 25;
    int num = 0;

    while (x > 0)
    {
        if (x >= 25)
        {
            x = x - quarter;
            num++;
        }

        else if (x >= 10)
        {
            x = x - dime;
            num++;
        }

        else if (x >= 5)
        {
            x = x - nickel;
            num++;
        }

        else
        {
            x = x - penny;
            num++;
        }
    }

    return num;
}
