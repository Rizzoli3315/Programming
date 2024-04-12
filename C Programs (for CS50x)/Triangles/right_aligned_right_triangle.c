#include <cs50.h>
#include <stdio.h>

void row(int space, int length);

int main(void)
{
    int height;
    do
    {
        height = get_int("Height : ");
    }
    while (height < 1);

    for (int k = 0; k < height; k++)
    {
        row(height - (k + 1), k + 1);
    }

}

void row(int space, int length)
{
    for (int j = 0; j < space; j++)
    {
        printf(" ");
    }

    for (int i = 0; i < length; i++)
    {
        printf("#");
    }

    printf("\n");
}
