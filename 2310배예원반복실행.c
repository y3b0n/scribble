#include<stdio.h>
int main()
{
	int n,i,j;
	scanf("%d", &n);
	for(i=1; ; i++)
	{
		int j=i;
		while(1)
		{
			printf("%d", i);
			j--;
			if(j==0)
				break;
				
		}
		if(i<+n)
		{
			printf("\n");
			continue;
			
		}
		else
			break;
	}
}
