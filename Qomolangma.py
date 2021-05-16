import pygame,sys
ORIGIN_ALTITUDE, SCALE_ALTITUDE = 5700, 0.15
DATA_X_MAX, DATA_Y_MAX = 1401, 1401
SCREEN_WIDTH, SCREEN_HEIGHT = 1400, 600 #窗口大小
#得到绘图y值
def RT_get_drawy(alt):
    return SCREEN_HEIGHT - (alt -ORIGIN_ALTITUDE) * SCALE_ALTITUDE
#----------主程序 pygame初始化---------
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('3D珠穆朗玛峰')
screen.fill((0, 0, 155))
#----------读取三维数据----------------
datafile = open('Qomolangma.asc', 'r')
strList = datafile.readlines()
datafile.close()
maxList, minList = [0] * DATA_X_MAX, [9000] * DATA_X_MAX #上下遮挡线初始化
for dataStr in strList:    	       #逐行遍历数据文件
    line, lastSpace = [], 0
    for x in range(len(dataStr)):  	#逐字符处理每行数据字符串
        c = dataStr[x]
        if c == ' ' or c == '\n':       #遇到空格或回车
            num = eval(dataStr [lastSpace:x])   #截取字符串转为海拔高度
            line.append(num)    	    	#将海拔高度加入剖面线
            lastSpace = x + 1
    x0, y0 = 0, RT_get_drawy(line[DATA_X_MAX - 1])  #逐行正投影绘图
    for x in range (DATA_X_MAX):
        y, flag = line[DATA_X_MAX - 1 - x], 0  	   	#取数据从东向西取
        if y < minList[x]: 	   	   	   	#下遮挡线处理
            minList[x], flag, clr = y, 1, (120,120,120)
        if y > maxList[x]:  	                  	#上遮挡线处理
            maxList[x], flag, clr = y, 1, (240, 240, 240)
        if flag == 1:
            y = RT_get_drawy(y)        	   	       	#绘制未被遮挡的点
            if abs(y - y0) < 100:
                pygame.draw.line(screen, clr, (x0, y0), (x, y), 1)
        x0, y0 = x,y
    pygame.display.update()
while True:
    for event in pygame.event.get():
        pass
    
pygame.display.update()
    
            
        



