int funky(x)
{
    if (x > 0)
    {
        x -= 1;
        funky(x);
    }
    printf("%d", x);
}

int main()
{
    funky(x passed as in 5);
    return 0;
}