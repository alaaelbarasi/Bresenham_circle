from graphics import *
import time
def bresenhamCircle(xc,yc,r):
    winX = 1500
    winY = 800
    win = GraphWin('Bresenham\'s circle', winX, winY)
    x=0
    y=r
    p=3-(2*r)
    pixels(win,xc,yc,x,y)
    while(x<y):
        if(p<0):
            p+=(4*x)+6
        else:
            y-=1
            p+=(4*(x-y))+10
        x+=1
        pixels(win,xc,yc,x,y)
        time.sleep(0.01)
    win.getMouse() 
    win.close()


def pixels(win,xc,yc,x,y):
    putPixel(win,xc+x,yc-y)
    putPixel(win,xc-x,yc-y)
    putPixel(win,xc+x,yc+y)
    putPixel(win,xc-x,yc+y)
    putPixel(win,xc+y,yc-x)
    putPixel(win,xc+y,yc+x)
    putPixel(win,xc-y,yc-x)
    putPixel(win,xc-y,yc+x) 

def putPixel(win,x,y):
    pt= Point(x,y)
    pt.draw(win)

def main():
    xc,yc= [int(x) for x in input("Enter center point :  ").split()]
    r= int(input("Enter radius : "))
    bresenhamCircle(xc,yc,r)

if __name__=='__main__':
    main()