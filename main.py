
import pygame
import sys
from pygame.locals import *
import cmath
import pygame.freetype

GOLD = 255, 215, 0
def drawText(xpos,ypos,path,sizex,sizey):
    img = pygame.image.load(path)
    img = pygame.transform.scale(img,(sizex,sizey))
    return img

def judge(temp1,left,right,bottom,top):
    if temp1.left<right and temp1.left>left and temp1.bottom<bottom and temp1.bottom>top:
        #print('get')
        return True
    elif temp1.left<right and temp1.left>left and temp1.top<bottom and temp1.top>top:
        #print('get')
        return True 
    elif temp1.right<right and temp1.right>left and temp1.top<bottom and temp1.top>top:
        #print('get')
        return True 
    elif temp1.right<right and temp1.right>left and temp1.bottom<bottom and temp1.bottom>top:
        #print('get')
        return True 
    else:
        return False

#初始化Pygame
pygame.init()
 
size = width,hight = 800,600
speed = [3,1]
speed1 = [7,3]
speed2 = [6,4]
speed3 = [4,6]
bg = (255,255,255) #RGB颜色
 
#clock = pygame.time.Clock()
#创建指定大写的窗口
screen = pygame.display.set_mode(size)
#设置窗口标题
pygame.display.set_caption('Rust me !')
 
#加载图片
turtle = pygame.image.load('zyr.png')
turtle1 = pygame.image.load('wash.png')
turtle2 = pygame.image.load('wash.png')
# hand = pygame.image.load('hand.png')
# temp1=pygame.image.load("temp1.png")
# temp2=pygame.image.load("temp2.png")
turtle = pygame.transform.scale(turtle,(60,60))
turtle1 = pygame.transform.scale(turtle1,(80,60))
turtle2 = pygame.transform.scale(turtle2,(80,60))
# hand = pygame.transform.scale(hand,(60,40))
# temp1 = pygame.transform.scale(temp1,(200,100))
# temp2 = pygame.transform.scale(temp2,(300,150))
#screen.blit(turtle1,) 
#获得图像的位置矩形
position = turtle.get_rect()
position1 = turtle1.get_rect()
position2 = turtle2.get_rect()
position3=position2
l_head = pygame.transform.rotate(turtle,340)
u_head = pygame.transform.rotate(turtle,270)
d_head = pygame.transform.rotate(turtle,90)
r_head = pygame.transform.rotate(turtle,20)
ll_head = turtle1
rr_head = pygame.transform.flip(turtle1,True,True)
num = 0
# test=drawText(120,100,'1.png',100,100)
# test1=drawText(120,200,'2.png',100,100)
# test2=drawText(120,300,'3.png',100,100)
# test3=drawText(300,150,'4.png',100,100)
words="SQL"
num_wash=0
num_piao=0
while True:
    #print(num)
    if num >=8:
        dir=-1
        turtle = l_head
    elif num<=0:
        dir=1
        turtle = r_head
    num=num+dir
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_LEFT]:
        position = position.move(-20,0)
    if key_pressed[pygame.K_RIGHT]:
        position = position.move(20,0)
    if key_pressed[pygame.K_UP]:
        position = position.move(0,-20)
    if key_pressed[pygame.K_DOWN]:
        position = position.move(0,20)
        # if event.type == KEYDOWN:
        #     if event.key == K_LEFT:
        #         #turtle = l_head
        #         position = position.move(-20,0)
        #     if event.key == K_RIGHT:
        #         #turtle = r_head
        #         position = position.move(20,0)
        #     if event.key == K_UP:
        #         #turtle = d_head
        #         position = position.move(0,-20)
        #     if event.key == K_DOWN:
        #         #turtle = u_head
        #         position = position.move(0,20)
				
    position1 = position1.move(speed1)
    position2 = position2.move(speed2)
    position3 = position3.move(speed3)
    if position.left < 0 or position.right > width:        
        #翻转图像
        turtle = pygame.transform.flip(turtle,True,False)
        #反向移动
        speed[0] = -speed[0]
    if position1.left < 0 or position1.right > width:
        #翻转图像
        turtle1 = pygame.transform.flip(turtle1,True,False)
        #反向移动
        speed1[0] = -speed1[0]
    if position2.left < 0 or position2.right > width:
        #翻转图像
        turtle2 = pygame.transform.flip(turtle2,True,False)
        #反向移动
        speed2[0] = -speed2[0]
    if position2.left < 0 or position2.right > width:
        #翻转图像
        #turtle2 = pygame.transform.flip(turtle2,True,False)
        #反向移动
        speed3[0] = -speed3[0]

    if position.top < 0 or position.bottom > hight:
        speed[1] = -speed[1]
    if position1.top < 0 or position1.bottom > hight:        
        speed1[1] = -speed1[1]
    if position2.top < 0 or position2.bottom > hight:        
        speed2[1] = -speed2[1]
    if position3.top < 0 or position3.bottom > hight:        
        speed3[1] = -speed3[1]
    #填充背景
    screen.fill(bg)
    #双缓冲
    #更新图像
    screen.blit(turtle2,position2)#bilt方法将一个图像覆盖到另一个图象上    
    screen.blit(turtle,position)#bilt方法将一个图像覆盖到另一个图象上
    screen.blit(turtle1,position1)#bilt方法将一个图像覆盖到另一个图象上 
    # screen.blit(test,(120,40))
    # screen.blit(test1,(120,300))
    # screen.blit(test2,(600,40))
    # screen.blit(test3,(600,300))
    f1 = pygame.freetype.Font("C://Windows//Fonts//msyh.ttc", 36)
    # f1rect = f1.render_to(screen, (position.left,position.bottom+60), words, fgcolor=GOLD, size=25)
    f2rect = f1.render_to(screen, position3, "白嫖", fgcolor=GOLD, size=25)
    f2rect = f1.render_to(screen, (600,500), str(num_piao-num_wash), fgcolor=GOLD, size=25)
    #f2rect = f1.render_to(screen, (120,400), "", fgcolor=GOLD, size=25)
    #screen.blit(hand,(position.left,position.bottom+20))
    out1=judge(position1,position.left,position.right,position.bottom,position.top)
    out2=judge(position2,position.left,position.right,position.bottom,position.top)
    out3=judge(position3,position.left,position.right,position.bottom,position.top)
    if out1 or out2 ==True:
        num_wash=num_wash+1
        print("你被逮捕！ 快去洗澡！   ",num_wash)
    if out3== True:
        num_piao=num_piao+1
        print("白嫖成功！    ",num_piao)
    
    """
    out=judge(120,40,position.left,position.right,position.bottom,position.top)
    out1=judge(120,300,position.left,position.right,position.bottom,position.top)
    out2=judge(600,40,position.left,position.right,position.bottom,position.top)
    out3=judge(600,300,position.left,position.right,position.bottom,position.top)
    out4=judge(120,500,position.left,position.right,position.bottom,position.top)
    out5=judge(600,500,position.left,position.right,position.bottom,position.top)
    if out == True:
        #screen.blit(turtle1,(position.left-60,position.bottom))
        words="语法查询树"
    #reset=judge(position1.left,position1.bottom,position.left,position.right,position.bottom,position.top)
    #if reset == True:
        #words="SQL"
    if out1 == True:
        words="视图被换为基表"
    if out3 == True:
        words="查询执行计划"
    if out2 ==True:
        words="得到SQL结果"
    if out4 == True:
        screen.blit(temp1,(120,600))
    if out5 == True:
        screen.blit(temp2,(600,600))
    """
        

    #更新界面
    pygame.display.flip()
    #延迟10毫秒
    pygame.time.delay(20)