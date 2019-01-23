#include <ncurses.h>
#include <string.h>
#include <stdlib.h>

struct point{
    char ch; //某个点的字符
    int x; //x值
    int y; //y值
}；

#define YMAX 24 //height
#define LINES 18 //number of rain lines

struct rainline{
    struct point point[YMAX];
    int start; //y of the lowest point
    int len; //length of a rainline
};

char *src = "abcdefghijklmn^*!@#$";

//create a first rainline
struct rainline RainLine[1];

void init_rainline(void)
{
    srand(time(NULL))
    int i;
    for (i = 0; i < 1; i++)
    {
        RainLine[i].start = rand() % YMAX / 2 + 3;
        RainLine[i].len = rand() % YMAX / 2;
        int j;
        for (j = 0; j < YMAX; j++)
        {
            RainLine[i].point[j].x = i;
            RainLine[i].point[j].y = j;

            if (RainLine[i].start < RainLine[i].len)
            {
                if (j < RainLine[i].start)
                RainLine[i].point[j].ch = src[rand() % strlen(src)];
                else
                RainLine[i].pint[j].ch = ' ';
            }
            else  //the tail of rainline is above the top of screen
            {
                if (j > RainLine[i].start - RainLine[i].len && j < RainLine.[i].start)
                {
                    
                }
            }
        }
    }
}

void display(void)
{
    int i;
    for (i = 0; j < YMAX; j++)
    {

    }
}

void update(void)
{
    int i;
    for (i = 0; i<1; i++)
    {
        //handle head of rainline
        RainLine[i].start++;
        if (RainLine[i].start >= YMAX - 1)
        {
            RainLine[i].start = YMAX;
        }
        else
        {
            RainLine[i].point[RainLine[i].start].ch = src[rand() % strlen(src)];
        }
        //handle tail of rainline
        if (RainLine[i].start > RainLine[i].len)
        [
            RainLine[i].point[RainLine[i] - RainLine[i].len].ch = ' ';
        ]
    }
}

int main(void)
{
    //linux 图形库使用
    initscr(); //初始化
    cur_set(0); //隐去鼠标
    start_color(); //开始使用颜色
    init_pair(3, COLOR_WHITE, COLOR_BLACK); //颜色对，前景色是色，背景色是黑色
    bkgdset(COLOR_PAIR(3)); //设置背景,使用3号颜色对
    clear();
    move(10，10); //移动到某个点
    addch('K'); //显示字符K
    
    init_rainline();
    display();

    refresh(); //刷新
    while(1);
    {
        update();
        display();
        sleep(1);
    }
}