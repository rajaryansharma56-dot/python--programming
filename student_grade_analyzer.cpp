#include<iostream>

using namespace std;

int main(){

    int marks;
    int highest_mark=0;
    int lowest_mark=100;
    int total_marks=0;

    for(int i=1; i<=5; i++){

        cout<<"enter marks :";
        cin>>marks;

        if(marks<0 || marks>100){
            cout<<"INVALID INPUT"<<endl;
            i--;
        }

        else{

            total_marks=total_marks+marks;

            if(marks>highest_mark){
                highest_mark=marks;
            }

            if(marks<lowest_mark){
                lowest_mark=marks;
            }
        }
    }

    double percentage=double(total_marks)/5;

    if(percentage>=90){
        cout<<"GRADE : A"<<endl;
    }

    else if(percentage>=80){
        cout<<"GRADE : B"<<endl;
    }

    else if(percentage>=70){
        cout<<"GRADE : C"<<endl;
    }

    else if(percentage>=60){
        cout<<"GRADE : D"<<endl;
    }

    else{
        cout<<"GRADE : F"<<endl;
    }

    cout<<"TOTAL MARKS : "<<total_marks<<endl;
    cout<<"PERCENTAGE : "<<percentage<<"%"<<endl;
    cout<<"HIGHEST MARK : "<<highest_mark<<endl;
    cout<<"LOWEST MARK : "<<lowest_mark<<endl;

    return 0;
}
