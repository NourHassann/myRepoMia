#include <iostream>
#include <string.h>
#include <iomanip>

using namespace std;
void menu();
void addTask();
void viewTask();
void removeTask();
void Exit();
void completedTasks();
struct taskDetails{
string description;
int id;
bool complete;
}s[100];

int countt=0;

int main()
{
    menu();
    return 0;
}

void addTask(){
cout<<"Enter the task description ";
cin.ignore();
getline(cin,s[countt].description);
s[countt].id= countt+1;
cout<<"task added successfully"<<endl;
countt++;
}

void viewTask(){
    cout << "Current Tasks: " << endl;
    cout << setw(10) << "Task ID" << setw(25) << "Description" << setw(30) << "Status" << endl;
    for (int i = 0; i < countt; i++) {
        cout << setw(5) << s[i].id << setw(40) << s[i].description << setw(23) << (s[i].complete ? "  COMPLETED" : "  UNCOMPLETED") << endl;
    }
}


void removeTask(){
    int taskToRemove;
cout<<"Enter task ID to remove: "<<endl;
cin>>taskToRemove;
for(int i = taskToRemove;i<countt;i++){
    s[i-1].description = s[i].description;
    s[i-1].id = i;
    s[i-1].complete = s[i].complete;
}
countt--;
cout<<"Task removed successfully!"<<endl;
}

void completedTasks(){
    int finished;
cout<<"enter the ID of the completed task ";
cin>>finished;
s[finished-1].complete= true;
}
void Exit(){
cout<<"Exiting Minions Task Manager. Have a great day!";
}

void menu(){
int option;
cout<< "Minions Task Manager\n" << "1. Add Task\n"<< "2. View Tasks\n"<<"3. Remove Task\n"<<"4. Mark the completed task\n"<<"5. Exit\n"<<"Select an option ";
cin>>option;
if (option == 1){
        addTask();
   menu();
    }
    else if (option == 2){
    viewTask();
    menu();
    }

   else if (option == 3){
    removeTask();
    menu();
    }
    else if (option == 4){
    completedTasks();
    menu();
    }
   else if(option == 5)
    Exit();
    else {cout<<"PLEASE type valid number\n"; menu();}
}

