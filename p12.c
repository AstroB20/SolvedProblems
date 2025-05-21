char *intToRoman(int num)
{
    char *result = (char *)malloc(16);
    int i = 0;
    int values[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    char *symbols[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

    for (int j = 0; j < sizeof(values) / sizeof(values[0]); j++)
    {
        while (num >= values[j])
        {
            num -= values[j];
            i += sprintf(result + i, "%s", symbols[j]);
        }
    }
    return result;
}