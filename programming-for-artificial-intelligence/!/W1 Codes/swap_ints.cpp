#include <iostream>

using namespace std;

int main ()
{
    int x = 72;
    int y = 3;
    int t = x;
    x = y;
    y = t;
    cout<<"x = "<<x<<"\t"<<"y = "<<y<<endl;
}