#include <stdio.h>

int main() {
	
	char string[50] = "AMO FAZER EXERCICIO NO URI";

	printf("<%s>\n", string);
	printf("<%30s>\n", string); // padding left
	printf("<%.20s>\n", string); // truncates to 20 characters
	printf("<%-20s>\n", string); // padding right
	printf("<%-30s>\n", string); // padding right
	printf("<%.30s>\n", string); // truncates to 30 characters
	printf("<%30.20s>\n", string); // padding left and truncates to 20 characters
	printf("<%-30.20s>\n", string); // padding right and truncates to 20 characters

	return 0;
}