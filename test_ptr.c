#include<stdio.h>
#include <stdlib.h>

void append(int** a, int* b, int i){
  if(i>0){
    a = realloc(a,(i+1)*sizeof(int*));
    a[i] = malloc(4*sizeof(int));
  }
  for(int j=0; j<4; j++){
    a[i][j]=b[j];
    printf("%d ",b[j]);
  }
  printf("\n");
  printf("a[0]=%p\n",a[0]);
}

void stuff_int(int** a, int* b){
  int i;
  for(i=0;i<20;i++){
    b[i-4*(i/4)]=i+1;
    if(i%4==3){
      
      printf("..a  a[0]=%p, a[0][0]=%d\n",a[0],a[0][0]);
      
      append(a,b,i/4);
      printf("a..  a[0]=%p\n",a[0]);
    }
  }
}

int main(){

int** a=malloc(1*sizeof(int*));
a[0]=malloc(4*sizeof(int));

int* b=malloc(4*sizeof(int));

stuff_int( a, b);

//print the content in a
for(int i=0; i<5; i++){
  for(int j=0; j<4; j++){
    printf("%d ",a[i][j]);
  }
  printf("\n");
}

for(int i=0;i<5;i++){
  free(a[i]);
}

free(a);
free(b);

return 0;
}