#include<stdio.h>
int main()
{
	int a,b,c,d;
	scanf("%d %d %d %d", &a, &b, &c,&d);
	printf("%d", ((a-c)*(a-c))+((b-d)*(b-d)));
	return 0;
}
