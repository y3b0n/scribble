#include<stdio.h>
void f(int x)
{
	if(x%2==1) printf("Hello?\n");
	else printf("goodbye!\n");
	
}
int main()
{	int a=1, b=214783646;
	f(1);
	f(214783646);
	return 0;
}
