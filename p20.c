bool isValidParantheses(char *s)
{
    int stack[10000];
    int top = -1;
    for (int i = 0; s[i] != '\0'; i++)
    {
        if (s[i] == '(' || s[i] == '{' || s[i] == '[')
        {
            stack[++top] = s[i];
        }
        else
        {
            if (top == -1)
                return false;
            char open = stack[top--];
            if ((open == '(' && s[i] != ')') ||
                (open == '{' && s[i] != '}') ||
                (open == '[' && s[i] != ']'))
            {
                return false;
            }
        }
    }
    return top == -1;
}