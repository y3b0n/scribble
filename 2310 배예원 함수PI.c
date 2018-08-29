
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>

#define PI 3.14159265

int main()
{
	printf("%If\n", sin(30*PI/180));
	printf("\n");
	
	for(int i=1; i<=5; i++)
		printf("%d\n", rand());
		
	printf("\n");
	
	srand((int)time(NULL));
	for(int i=1; i<=5; i++)
	printf("%d\n", rand());
}


