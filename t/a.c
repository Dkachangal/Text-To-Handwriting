#include<stdio.h>
#include<stdlib.h>
int main() {
	
    char grid[20][20];
    int N, M;
    char inputRowString[20];
    int C_over_R=0, R_over_C = 0;
    int row, cols;
    row = -1;
    cols = -1;
    int rCount = 0;
    int x=-1;
    int x1=-1;
    int y=-1;
    int y1=-1;
    int ans =0;
    int over = 0;
    
    scanf("%d %d", &N, &M);
    
    // taking input in grid
    for (int i=0; i<N; i++) {
        scanf("%s", inputRowString);
        for (int j=0; j<M; j++) {
            grid[i][j] = inputRowString[j];
        }
    }

    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            if (grid[i][j] == 'R') {
                rCount++;
            }
        }
    }
    // FINDING HORIZONTAL OR VERTICAL
    
    if (rCount == 1) {
        return 1;
    }
    else if (rCount > 1){
        int count=0;
        for (int p=0; p<N; p++) {
            for (int q=0; q<M; q++) {

                if (count == 0) {
                    if (grid[p][q] == 'R') {
                        x = p;
                        y = q;
                        count++;
                    }
                }
                else if (count == 1) {
                    if (grid[p][q] == 'R') {
                        if (count <2) {
                            x1 = p;
                            y1 = q;
                            count++;
                        }
                    }
                }
            }
        }

    }
    //inserting row or cols
    if (x == x1) {
        row = x;
        for (int i=0; i<M; i++) {
            if (grid[row][i] != '.') {
                if (grid[row+1][i] != '.') {
                    if (grid[row][i] == 'C' && over==0) {
                        C_over_R++;
                        over++;
                    }
                    else {
                        over = 0;
                        R_over_C++;
                    }
                }
            }
        }
    }
    if (y == y1) {
        cols = y;
        //vertical
        for (int i=0; i<N; i++) {
            if (grid[i][cols] != 'c') {
                if (grid[i][cols+1] != '.') {
                    if (grid[i][cols] == 'C') {
                        C_over_R++;
                        over++;
                        if (over == 2) {
                            C_over_R = C_over_R -2;
                        }
                    }
                    else {
                        over=0;
                        R_over_C++;
                        
                    }
                }
            }
        }
    }
    if (C_over_R > R_over_C) {
        ans = R_over_C;
    } else {
        ans = C_over_R;
    }
    printf("%d", ans);
    return 0;

}