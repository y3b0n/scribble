#include<stdio.h>
int main()
{
	char n;
	scanf("%c", &n);

	
	switch(n)
	{
		case 'A':
			printf("best!!!\n"); break;
		case 'B':
			printf("good!!\n"); break;
		case 'C':
			printf("run\n"); break;
		case 'D':
			printf("slowly~\n"); break;	
			
		default :
		printf("What?\n"); break;	
	}
}
