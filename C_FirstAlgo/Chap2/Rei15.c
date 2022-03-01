/*
 * ---------------------------------------------------
 *      連立方程式の解法（ガウス・ジョルダン法）     *
 * ---------------------------------------------------
 */

#include <stdio.h>

#define N 3     // 元の数

void main(void)
{                                   // 係数行列
    double a[N][N+1]={{2.0  ,3.0  ,1.0  ,4.0  },
                      {4.0  ,1.0  ,-3.0 ,-2.0 },
                      {-1.0 ,2.0  ,2.0  ,2.0  }};
    double p,d;
    int i,j,k;

    for (k=0;k<N;k++){
        p=a[k][k];                // ピボット係数
        for (j=k;j<N+1;j++)       // ピボット行をｐで割る
            a[k][j]=a[k][j]/p;
        for (i=0;i<N;i++){        // ピボット列の掃き出し
            if (i!=k){
                d=a[i][k];
                for (j=k;j<N+1;j++)
                    a[i][j]=a[i][j]-d*a[k][j];
            }
        }
    }

    for (k=0;k<N;k++)
        printf("x%d=%f\n",k+1,a[k][N]);
}
