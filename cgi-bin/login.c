#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stddef.h>
#define MAXPASS 15
#define MAXUSR 10
#define NAME_SIZE 20
#define LINE_SIZE NAME_SIZE+MAXUSR+MAXPASS+2 //since there are two commas
#define LINE_NUMBER 36

void   getInput(char *str, int *password, int max);
int  searchUser(char *username,char *password,char *line);

int main(int argc, char *argv[]){
	printf("Content-type: text/html\n\n");
	printf("<html>\n\n");
	int data_size = atoi(getenv("CONTENT_LENGTH"));
	char *username = (char *)malloc(MAXUSR+1),
		*password = (char *)malloc(MAXPASS+1);
	int count = 0;
	getInput(username, &count, data_size);
	getInput(password, &count, data_size);
	if(strcmp(username, "") == 0 || strcmp(password, "")==0){
		printf("<div align = \"center\">");
		printf("<body>");
		printf("<h1> COMPSCI FUNNIES </h1>");
		printf("<br>");
		printf("Please fill in every field! We need all your info!");
		printf("<br>");
		printf("<a href=\"../welcome.html\"> back to the welcome page! </a>");
		printf("<br>");
		printf("<br>");
		//printf(<img src="http://40.media.tumblr.com/tumblr_lkdkryTFbR1qiinzao1_400.png">);
		printf("</body>");
		printf("</div>");
		return EXIT_FAILURE;}
	
	//check if user exists...
	FILE *file_ptr = fopen("../data/members.csv", "rt");
	char *line = (char *)malloc(LINE_SIZE+1); //again allocating for the \0
	int check; 
	
	fgets(line, LINE_SIZE, file_ptr);
		for(fgets(line, LINE_SIZE, file_ptr);!feof(file_ptr); fgets(line, LINE_SIZE, file_ptr)){
	if((check = searchUser(username,password,line))>=0)
		break;
	}
	fclose(file_ptr);
	
    if (check == -1){
	 	printf("<div align = <\"center\">");
                printf("<body>");
                printf("<h1> COMPSCI FUNNIES </h1>");
                printf("<br>");
                printf("We did not find that username!\"%s\"", username);         
		printf("<br>");
		printf("<a href=\"../newmembers.html\"> Register! </a>");         
                printf("<br>");
		printf("<a href=\"../welcome.html\"> back to the welcome page! </a>");
                printf("<br>");
                printf("<br>");
                //printf(<img src="http://40.media.tumblr.com/tumblr_lkdkryTFbR1qiinzao1_400.png">);
                printf("</body>");
                printf("</div>");
                return EXIT_FAILURE;}

    if (check == 0){
		printf("<div align = <\"center\">");
                printf("<body>");
                printf("<h1> COMPSCI FUNNIES </h1>");
                printf("<br>");
                printf("Oops! You seem to have entered the wrong password\"%f\"", check);
                printf("<br>");       
                printf("<a href=\"../welcome.html\"> back to the welcome page! </a>");         
                printf("<br>");
                printf("<br>");
                //printf(<img src="http://40.media.tumblr.com/tumblr_lkdkryTFbR1qiinzao1_400.png">);
                printf("</body>");
                printf("</div>");
                return EXIT_FAILURE;}
	
	free(password);
	
	file_ptr = fopen("../loginsuccess.html", "rt");
	char *page_line = (char*)malloc(256);
	*(page_line+255) = '\0';
	int counter;
	
	for(counter=0;counter<LINE_NUMBER-1;counter++)
		printf("%s",fgets(page_line,255,file_ptr));
	printf("\t\t <input type=\"hidden\" name=\"user\" value=\"%s\">\n", username);
	fgets(page_line,255,file_ptr);
	while(!feof(file_ptr))
		printf("%s",fgets(page_line,255,file_ptr));
	fclose(file_ptr);

	free(page_line);	
	free(username);
	return EXIT_SUCCESS;
}


void getInput(char *str, int *count, int max){
	int c, index=0;
	char *escChar = (char *)malloc(3);	
	escChar[2]='\0';
	
	for(;(c=getchar())!='='; (*count)++);
	while((c=getchar())!='&' && c!=EOF && *count<=max){
		if(c=='%'){
			escChar[0]=getchar();
			escChar[1]=getchar();
			str[index]=(char)strtol(escChar,NULL,16);
		}
		else if(c=='+') str[index]=' ';
		else str[index]=c;
		(*count)++;
		index++;
	}
	str[index+1]='\0';
	free(escChar);

}

int  searchUser(char *username,char *password,char *line){
    char *token;

    token = strtok(line,",");
    //error on the line, possibly empty
    if (token == NULL) return -2;

    token = strtok(NULL,",");
    //error on the line, missing field
    if (token == NULL) return -2;
    //user not found
    if (strcmp(token,username)!=0) return -1;

    token = strtok(NULL,"\n");
    //error on the line, missing field
    if (token == NULL) return -2;
    //user found but wrong password
    if (strcmp(token,password)!=0) return 0;

    //username passes all tests
    else return 1;
}


	



