#include<stdio.h>

void f(int a,int b)
{
	printf("%d\n", a>b? a-b: b-a);
	
}

void g(int c,int d,int e)
{
	printf("%f\n", (c+d+e)/3.0);
}
int main()
{
	int a,b,c,d,e;
	scanf("%d %d %d %d %d", &a, &b, &c, &d, &e);
	f(a,b);
	g(c,d,e);
	
return 0;	
}

