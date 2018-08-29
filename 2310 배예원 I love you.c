#include<stdio.h>
void f()
{
	printf("I love you!\n");
	return;
}
int g()
{	
	return 999;
	return 123;
}
int main()
{
f();
printf("%d\n", g());
return 0;
}


