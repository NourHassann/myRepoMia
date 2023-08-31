#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
int count;
printf("enter the number of counting ");
scanf("%d", &count);
for(int i=count; i >0; i--){
    printf("%d\n", i);
    sleep(1);
}
printf("Blast off to the moon!");
    return 0;
}
