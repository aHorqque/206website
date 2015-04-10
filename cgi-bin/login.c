#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define DATAFILE "../data/members.csv"

const char *getfield(char *line, int i){
	const char *tok;
	for (tok = strtok(line, ",");
		tok && *tok;
		tok = strtok(NULL, ",\n"))
	{
		if (!--i)
			return tok;
	}
	return NULL;
}

int main(void){
	FILE *f = fopen(DATAFILE, "r");
	//If there's no csv file
	if (f == NULL){
		printf("%s%c%c\n","Content-Type:text/html\n");
		printf("<head><title> Error </title></head>");
		printf("<body><p> Unable to open members.csv </p></body>");
		return(1);
	} //If you can open the csv file 
	else { 
		char str[2000];
		if(fgets(str,2000,f)!=NULL){
			char *tmp = strup(line);
			if getfield(tmp,2) == //USERNAME {then redirect to loginsuccess}
			// else {}
		}
		return(0);
	}
}
