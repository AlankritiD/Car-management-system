#include <windows.h>
#include<stdio.h>
#include<conio.h>
#include <stdlib.h>
#include<string.h>
#include<ctype.h>
#include<direct.h>
#include<time.h>
void mainmenu();
void addcars();
void removecars();
void editlist();
void searchcars();
void carlist();
int getdata();
int checkplate(int t);
struct car
 {
int plate;
char company[20];
char make_model[20];
char chasis[20];
char engine[20];
4

        char avail[20];
struct car a;
COORD coord = { 0, 0 };
COORD max_res, cursor_size;
void gotoxy(int x, int y)
{
       coord.X = x; coord.Y = y;
       SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),
coord);
}
void delay(unsigned int mseconds)
};
{
clock_t goal = mseconds + clock();
while (goal > clock());
}
FILE *fp, *ft, *fs;
int main()
{
       system(" title Car Management System");
       system(" color 1A");
       char array[50] = { "CAR MANAGEMENT SYSTEM" };
       gotoxy(35, 10);
       for (int x = 0; x < 21; x++)
       {
               printf("%c", array[x]);
               delay(200);
       }
       gotoxy(38, 15);
       printf("Loading......");
       delay(4000);
       mainmenu();
void mainmenu()
       system(" color 5F ");
       system("cls");
       int choice;
       gotoxy(20, 3);
printf("\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB
2\xB2 MAIN MENU
\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2");
       gotoxy(20, 5);
       printf("\xDB\xDB\xDB\xDB\xB2 1- Add cars");
       gotoxy(20, 7);
       printf("\xDB\xDB\xDB\xDB\xB2 2- Remove cars");
       gotoxy(20, 9);
       printf("\xDB\xDB\xDB\xDB\xB2 3- Search cars");
       gotoxy(20, 11);
       printf("\xDB\xDB\xDB\xDB\xB2 4- View car list");
       gotoxy(20, 13);
       printf("\xDB\xDB\xDB\xDB\xB2 5- Edit availability info");
       gotoxy(20, 15);
       printf("\xDB\xDB\xDB\xDB\xB2 6- Close application");
} {
5

 { option");
}
} }
void addcars()
gotoxy(10, 23);
printf("\aWrong Entry!!Please re-entered correct
if (getch())
       mainmenu();
{
char choice = ' ';
system("cls");
system(" color 2F ");
gotoxy(20, 3);
printf("Press any key to enter data.");
gotoxy(20, 4);
printf("Press backspace to go back to main menu.");
if (getch() == 8)
       mainmenu();
else
printf("\n\n\n\t\t\tEnter choice: ");
switch (getch())
{
case '1':
addcars();
       break;
case '2':
       removecars();
       break;
case '3':
       searchcars();
       break;
case '4':
carlist();
       break;
case '5':
editlist();
       break;
case '6':
{
system("cls");
gotoxy(16, 3);
printf("Thanks for using the Program..");
gotoxy(10, 7);
printf("Exiting in 5 second...........>");
//flushall();
delay(5000);
exit(0);
} default:
