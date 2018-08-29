#include<stdio.h> 
int main()
{
	int a,b,c,d;
	scanf("%d", &a);
	b=a/100;
	c=(a-100*b)/10;
	d=a-(100*b+10*c);
	printf("%d%d%d", d,c,b);
	
}
