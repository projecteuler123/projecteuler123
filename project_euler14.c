#include<stdio.h>
int c=0;
int collatzsequence(int n){
    while(n!=0){
        if(n%2 == 0)
            n = n/2;
        else
            n=(3*n)+1;
        c=c+1;
       }
    return c;
}
int main(){
int i,v;
for(i=1;i<=13;i++){
   v = collatzsequence(i);
}
printf("%d",v);
}
