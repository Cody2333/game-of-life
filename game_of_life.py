# coding: utf-8
from graphics import *
import random
import time
import threading
from button import *
import sys
import pickle
import os
ISOTIMEFORMAT='%Y-%m-%d %X'
os_char='gb18030' 
###################################################################################
TARGET_COUNT=10000     #global variable used for communication between two thread #
ANIMATE_TIMES=10000    #                                                          #
LEFT_COUNT=10000       #                                                          #
CLEARABLE=True         #                                                          #
is_example_show=False  #                                                          #
###################################################################################
TASK_NUM=6
BLOCK_SIZE = 14
BLOCK_OUTLINE_WIDTH = 0
BOARD_WIDTH = 80
BOARD_HEIGHT = 50
BUTTON_WIDTH=200
TEXT_POS_x=BLOCK_SIZE*BOARD_WIDTH+100
TEXT_COLOR='#32CD32'
BLOCK_COLOR='#32CD32'
PAUSE_TIME=0.2
####################################################
#init example list from template.txt
####################################################
if os.path.exists('template'):
    f=open('template','r')
    example=pickle.load(f)
    #print 'a'
    f.close()
else :
    f=open('origin_template','r')
    example=pickle.load(f)
    #print 'b'
    f.close()
    f=open('template','w')
    pickle.dump(example,f,0)
    f.close()
    
#########################################################
#-----example:origin template list stored for show------#
#########################################################
'''heart_shape=[(31, 15), (45, 19), (42, 13), (31, 19), (43, 13), (33, 23), (38, 28), (39, 27), (39, 16), (35, 13), (30, 18), (42, 24), (36, 26), (32, 21), (37, 16), (43, 23), (33, 22), (46, 18), (34, 24), (35, 25), (31, 20), (43, 22), (40, 14), (41, 13), (30, 16), (34, 13), (40, 26), (46, 16), (44, 21), (41, 25), (45, 15), (30, 17), (37, 15), (46, 17), (38, 17), (44, 14), (45, 20), (32, 14), (39, 15), (33, 13), (36, 14), (37, 27)]
example_temp=[]
example_temp.append([(36,18),(37,18),(38,18),(37,20),(37,21),(37,22)])
example_temp.append([(35,24),(38,24),(40,24),(43,24),(37,25),(41,25),(37,26),(41,26),(38,26),(40,26),(35,23),(37,23),(41,23),(43,23),(36,22),(42,22)])
example_temp.append([(36,25),(37,25),(38,25),(37,27),(37,28)])
example_temp.append([(35,27), (36,27), (36,28), (40,28), (41,28), (42,28), (41,26)])
example_temp.append([(32,24), (32,25), (32,26), (34,22), (34,27), (35,22), (35,27),(36,22), (36,27), (37,24), (37,25), (37,26) ])
example_temp.append([(34,24),(35,24),(35,25),(39,25),(40,25),(41,25),(40,23)])
example_temp.append([(39, 16), (40, 17), (38, 20), (34, 19), (40, 18), (38, 19), (34, 17), (35, 18), (32, 17), (37, 20), (32, 18), (38, 17), (34, 20), (35, 20), (37, 18), (33, 16)])
example_temp.append([(36, 20), (36, 19), (37, 23), (38, 21), (36, 22), (37, 21), (38, 24), (38, 19), (39, 20), (39, 23), (39, 22), (37, 18)])
example_temp.append([(41, 21), (42, 27), (44, 26), (45, 24), (43, 22), (42, 28), (40, 27), (38, 25), (39, 23), (44, 24), (41, 22), (39, 25)])
example_temp.append([(41, 21), (36, 25), (40, 23), (41, 20), (36, 20), (37, 25), (36, 21), (37, 22), (40, 25), (39, 21), (38, 24), (41, 25), (37, 20), (40, 20), (41, 24), (36, 24)])
example_temp.append([(34, 26), (39, 24), (36, 25), (38, 23), (37, 25), (39, 26), (37, 22), (35, 24), (40, 26), (36, 23), (38, 25), (35, 26)])
example_temp.append(heart_shape)
example_temp.append([(64, 21), (41, 20), (35, 22), (42, 22), (36, 20), (62, 19), (40, 24), (37, 24), (64, 23), (38, 18), (59, 22), (39, 18), (60, 20), (40, 19), (62, 24), (63, 22), (42, 21), (36, 23), (61, 22), (62, 22), (62, 25), (38, 25), (41, 23), (35, 21), (60, 22), (37, 19), (39, 25), (60, 24), (62, 20)])
example_temp.append([(50, 18), (53, 18), (54, 22), (55, 13), (51, 23), (49, 15), (55, 17), (58, 16),
 (52, 18), (56, 16), (56, 23), (54, 23), (51, 17), (49, 27), (50, 16), (38, 20),
 (47, 18), (39, 19), (48, 16), (57, 18), (49, 26), (57, 27), (52, 21), (59, 17),
 (56, 18), (39, 18), (54, 18), (54, 21), (49, 25), (57, 26), (49, 18), (55, 18),
 (52, 22), (50, 23), (50, 14), (53, 21), (48, 18), (57, 15), (51, 13), (51, 18),
 (49, 24), (57, 25), (52, 23), (53, 20), (57, 23), (57, 24), (37, 19), (55, 23),
 (58, 18), (38, 17), (53, 19), (47, 17), (59, 18), (56, 14), (37, 18), (49, 23)])
example_temp.append([(38, 31), (38, 22), (36, 18), (38, 28), (38, 23), (42, 17), (36, 19), (38, 36),
 (38, 26), (38, 29), (38, 20), (41, 18), (36, 21), (38, 34), (38, 37), (37, 22),
 (40, 18), (43, 15), (38, 27), (38, 18), (38, 21), (39, 18), (38, 35), (43, 16),
 (40, 19), (43, 14), (38, 24), (38, 19), (34, 17), (35, 18), (38, 32), (33, 15),
 (38, 25), (38, 33), (33, 14), (40, 21), (38, 30), (39, 22), (37, 18), (33, 16)])
 
 
example_temp.append([(4, 17), (16, 20), (30, 20), (20, 17), (32, 20), (30, 18), (18, 19), (3, 17), (13, 18), (34, 19), (19, 17), (30, 19), (31, 20), (3, 16), (13, 17), (16, 14), (19, 16), (14, 19), (15, 20), (33, 20), (13, 16), (34, 17), (15, 14), (19, 18), (17, 17), (18, 15), (31, 17), (4, 16), (14, 15)])

f=open('origin_template.txt','w')
pickle.dump(example_temp,f,0)
f.close()
'''



###############################################
#----------------任务关卡------------------------#
###############################################
task1=[(36,24),(36,25),(37,26),(38,26)]
task2=[(36,23),(37,23),(36,24),(37,25),(39,27),(41,27),(40,28),(41,28)]
task3=[(36,24),(37,24),(38,24),(37,26),(37,27)]
task4=[(36,24),(37,24),(38,24),(39,24),(40,24),(35,25),(41,25),(35,26),(41,26),(37,26),(39,26),(36,27),(37,27),(39,27),(40,27)]
task5=[(36,24),(37,24),(38,24),(39,24),(40,24),(35,25),(41,25),(35,26),(36,26),(40,26),(41,26)]
task6=[(34,23),(36,23),(34,25),(32,25),(36,25),(38,25),(30,27),(32,27),(38,27),(40,27),(30,29),(32,29),(38,29),(40,29),(34,31),(32,31),(36,31),(38,31),(34,33),(36,33)]
class Block(Rectangle):
    '''
    Block represent a single block in board
    
    '''
    def __init__(self, pos, color,can_change=True):
        self.x = pos.x
        self.y = pos.y
        self.can_change=can_change
        p1 = Point(pos.x*BLOCK_SIZE,pos.y*BLOCK_SIZE)
        p2 = Point(p1.x + BLOCK_SIZE, p1.y + BLOCK_SIZE)
        Rectangle.__init__(self, p1, p2)
        self.setWidth(BLOCK_OUTLINE_WIDTH)
        self.setFill(color)
        self.status = 'dead'
        self.new_status = 'None'
        
    def get_coords(self):
        return (self.x, self.y)

    def set_live(self,win):
        if self.status=='dead' and self.can_change:
            self.status = 'live'
            self.draw(win)

    def set_dead(self):
        if self.status=='live' and self.can_change:
            self.status = 'dead'
            self.undraw()

    def is_live(self):
        if self.status == 'live':
            return True
        return False

    def reset_status(self, win):
        if self.new_status=='dead' and self.status=='live':
            self.set_dead()
        elif self.new_status=='live' and self.status=='dead':
            self.set_live(win)
            
    def change_state(self,win):
        if self.status=='live' and self.can_change:
            self.status='dead'
            self.undraw()
        elif self.status=='dead' and self.can_change:
            self.status='live'
            self.draw(win)
            
    def set_changable(self,flag):
        self.can_change=flag
        return flag
    
class Board:
    '''
    Board represet all the block region 
    delay:(float)control the speed of animation
    click_count:(int)count the click times
    clickable:(boolean)whether board is allowed to respond click
    block_list:(dict),contains all the block objects
    '''
    def __init__(self, win, width, height):
        self.width = width
        self.height = height
        self.win = win
        self.delay = 0
        self.click_count=0
        self.clickable=False
        self.win.setBackground('black')

        # initialize grid lines
        for x in range(1,self.width+1):
            self.draw_gridline(Point(x, 0), Point(x, self.height))

        for y in range(1,self.height+1):
            self.draw_gridline(Point(0, y), Point(self.width, y))

        ################################################################
        #define a block dict
        #get (x,y) block by using self.block_list[(x,y)]
        ################################################################
        self.block_list = {}
        #self.block_list_cache={}

        #init blocks
        for x in range(0,self.width):
            for y in range(0,self.height):
                self.block_list[(x,y)]=Block(Point(x,y),BLOCK_COLOR)

    def set_speed(self,state):
        if state=='fast':
            if abs(self.delay)>pow(10,-3):
                self.delay-=0.05
                #if self.delay<0:
                #    self.delay=0
                #print 'x'+str(self.delay)
            #self.delay=0
        if state=='slow':
            if self.delay<1.0:
                self.delay+=0.05
                #print 'y'+str(self.delay)
    #reset all block dead
    def reset(self):
        for block in self.block_list.values():
            block.set_changable(True)
            block.set_dead()
    
    #called once in a stimulation
    def reset_state(self):
        for block in self.block_list.values():
            block.set_changable(True)
            block.reset_status(self.win)
            
    def draw_gridline(self, startp, endp):

        line = Line(Point(startp.x*BLOCK_SIZE, startp.y*BLOCK_SIZE), \
                    Point(endp.x*BLOCK_SIZE, endp.y*BLOCK_SIZE))
        line.setOutline('#32cd32')
        line.draw(self.win)
        
        line = Line(Point(startp.x*BLOCK_SIZE-1, startp.y*BLOCK_SIZE-1), \
                    Point(endp.x*BLOCK_SIZE-1, endp.y*BLOCK_SIZE-1))
        line.setOutline('#32cd32')
        line.draw(self.win)

    #generate random seed 
    def random_seed(self, percentage):
        for block in self.block_list.values():
            if random.random() < percentage:
                
                block.set_live(self.win)
                #block.set_changable(False)
                #block.set_changable(False)
                
    #set seed
    def seed(self, block_coords):
        for block in self.block_list.values():
            if block.get_coords() in block_coords:
                
                block.set_live(self.win)
                block.set_changable(False)
                #block.set_changable(False)
    ##############################################################################
    #generate a list that contains the live block;list=[(x1,y1),(x2,y2)......]   #
    #-----------------------used for creating examples---------------------------#
    ##############################################################################
    def generate_list(self):
        global example
        l=[]
        for block in self.block_list.values():
            if block.is_live():
                l.append(block.get_coords())
        print l
        example.append(l)
        f=open('template','w')
        pickle.dump(example,f,0)
        f.close()
        return l
    
    def delete_list(self,count):
        global example
        example.remove(example[count])
        self.reset()
        f=open('template','w')
        pickle.dump(example,f,0)
        f.close()
        
    def respond_click(self,x,y):
        if self.clickable:
            self.block_list[(x,y)].change_state(self.win)
            
    def set_clickable(self,flag):
        self.clickable=flag
        
    def is_clickable(self):
        return self.clickable
    
    #get the num of live blocks
    def get_live_count(self):
        count=0
        for block in self.block_list.values():
            if block.is_live():
                count+=1
        return count
    
    def get_block_neighbors(self, block):
        coord=block.get_coords()
        if coord==(0,0):
            return [self.block_list[(0,1)],self.block_list[(1,0)],self.block_list[(1,1)]]
        elif coord==(BOARD_WIDTH-1,BOARD_HEIGHT-1):
            return [self.block_list[(BOARD_WIDTH-2,BOARD_HEIGHT-1)],self.block_list[(BOARD_WIDTH-2,BOARD_HEIGHT-2)],self.block_list[(BOARD_WIDTH-1,BOARD_HEIGHT-2)]]    
        elif coord==(0,BOARD_HEIGHT-1):
            return [self.block_list[(0,BOARD_HEIGHT-2)],self.block_list[(1,BOARD_HEIGHT-2)],self.block_list[(1,BOARD_HEIGHT-1)]]
        elif coord==(BOARD_WIDTH-1,0):
            return [self.block_list[(BOARD_WIDTH-2,0)],self.block_list[(BOARD_WIDTH-2,1)],self.block_list[(BOARD_WIDTH-1,1)]]
        elif coord[0]==0:
            return [self.block_list[(0,coord[1]+1)],self.block_list[(0,coord[1]-1)],self.block_list[(1,coord[1]+1)],self.block_list[(1,coord[1])],self.block_list[(1,coord[1]-1)]]
        elif coord[0]==BOARD_WIDTH-1:
            return [self.block_list[(BOARD_WIDTH-1,coord[1]-1)],self.block_list[(BOARD_WIDTH-1,coord[1]+1)],self.block_list[(BOARD_WIDTH-2,coord[1]-1)],self.block_list[(BOARD_WIDTH-2,coord[1])],self.block_list[(BOARD_WIDTH-2,coord[1]+1)]]
        elif coord[1]==0:
            return [self.block_list[(coord[0]+1,0)],self.block_list[(coord[0]-1,0)],self.block_list[(coord[0]+1,1)],self.block_list[(coord[0],1)],self.block_list[(coord[0]-1,1)]]
        elif coord[1]==BOARD_HEIGHT-1:
            return [self.block_list[(coord[0]+1,BOARD_HEIGHT-1)],self.block_list[(coord[0]-1,BOARD_HEIGHT-1)],self.block_list[(coord[0]+1,BOARD_HEIGHT-2)],self.block_list[(coord[0],BOARD_HEIGHT-2)],self.block_list[(coord[0]-1,BOARD_HEIGHT-2)]]
        else: 
            return [self.block_list[(coord[0]+1,coord[1]+1)],self.block_list[(coord[0]+1,coord[1])],self.block_list[(coord[0]+1,coord[1]-1)],self.block_list[(coord[0],coord[1]+1)],self.block_list[(coord[0],coord[1]-1)],self.block_list[(coord[0]-1,coord[1]+1)],self.block_list[(coord[0]-1,coord[1])],self.block_list[(coord[0]-1,coord[1]-1)]]
        
    #generate once
    def simulate(self):    
        #print "ANIMATE_TIMES:",time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )
        for block in self.block_list.values():
            live_num=0
            neighbors = self.get_block_neighbors(block)
            #print "ANIMATE_TIMES:",time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )
            for neighbor in neighbors:
                #print neighbor.get_coords()
                if neighbor.is_live():
                    live_num+=1    
                    #print "live:",neighbor.get_coords(),            
            if live_num==3:
                block.new_status='live'
            elif live_num==2 and block.is_live() :
                block.new_status='live'
            else:
                block.new_status='dead'
        #    for block in self.block_list.values():        
        #        block.reset_status(self.win)
            #print "B:",time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )
        #print "ANIMATE_TIMES:",time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )
        self.reset_state()

    def animate(self):
            self.simulate()
            time.sleep(self.delay)
    


class Task():
    '''
    respond_click(self,q):used for listening on task btn click
    mainly operating on task related events
    '''
    def __init__(self,win,task_list,board,boardThread):
        self.win=win
        self.board=board
        self.board_thread=boardThread
        self.task_list=task_list
        self.button_width=BUTTON_WIDTH
        self.text=Text(Point(BOARD_WIDTH * BLOCK_SIZE+40,10),"Task:")
        self.text.setFill(TEXT_COLOR)
        self.text.draw(self.win)
        self.task_btn_list=[]
        # self.can_clear=True
        self.show_text_drawn=False
        self.target_live_count=10000
        self.animate_times=10000
        self.left_num=10000
        for i in range(TASK_NUM):
            taskBtn=Button(win,Point(BOARD_WIDTH * BLOCK_SIZE+40*(1+i%4),40*(i/4+1)),40,40,str(i+1))
            taskBtn.activate()
            self.task_btn_list.append(taskBtn)
    def respond_click(self,q):
        #self.can_clear=True
        for i in range(TASK_NUM):
            btn=self.task_btn_list[i]
            if btn.clicked(q):
                self.board_thread.stop()
                time.sleep(0.1)
                global CLEARABLE
                CLEARABLE=False
                self.undraw_show_free_mode_test()
                self.target_live_count=self.task_list.get_live(i)
                self.animate_times=self.task_list.get_times(i)
                self.left_num=self.task_list.get_left_num(i)
                global TARGET_COUNT,ANIMATE_TIMES,LEFT_COUNT
                TARGET_COUNT=self.target_live_count
                #print "target_live_count:",TARGET_COUNT
                ANIMATE_TIMES=self.animate_times
                LEFT_COUNT=self.left_num
                #set the time the animation need to loop
                self.board_thread.set_count(self.animate_times)
                                
                self.task_list.draw_task(i,self.board)
                
                
                self.board.set_clickable(True)
    
    def show_free_mode_test(self):
        if self.show_text_drawn==False:
            self.show_text_drawn=True
            self.show_text=Text(Point(TEXT_POS_x,250),"Free Edit Mode")
            self.show_text.setFill(TEXT_COLOR)
            self.show_text.draw(self.win) 
            
    def undraw_show_free_mode_test(self):
        if self.show_text_drawn:
            self.show_text_drawn=False
            self.show_text.undraw()
            
    def undraw_task_text(self):
        self.task_list.undraw_task()
                      

class TaskText():
    '''
    represent the task discription text
    '''
    def __init__(self,win,level,target,left_life_num,animate_time,target_count=0):
        self.win=win
        self.target_count=target_count
        self.animate_time=animate_time
        self.left_num=left_life_num
        self.is_drawn=False
        self.level=Text(Point(TEXT_POS_x,200),"-----任务"+str(level)+"-----")
        self.title=Text(Point(TEXT_POS_x,230),"-----任务目标------")
        self.target=Text(Point(TEXT_POS_x,260),target)
        self.left_life_num=Text(Point(TEXT_POS_x,300),"可用生命："+str(left_life_num))
        self.level.setTextColor(TEXT_COLOR)
        self.title.setTextColor(TEXT_COLOR)
        self.target.setTextColor(TEXT_COLOR)
        self.left_life_num.setTextColor(TEXT_COLOR)

    def get_left(self):
        return self.left_num
        
    def get_animate_time(self):
        return self.animate_time
        
    def get_target_count(self):
        return self.target_count
        
    def draw_text(self):
        if self.is_drawn==False:
            self.is_drawn=True
            self.left_life_num.draw(self.win)
            self.level.draw(self.win)
            self.target.draw(self.win)
            self.title.draw(self.win)
            
    def undraw_text(self):
        if self.is_drawn==True:
            self.is_drawn=False
            self.left_life_num.undraw()
            self.level.undraw()
            self.target.undraw()
            self.title.undraw()
            
    def is_drawn(self):
        return self.is_drawn
        
class TaskList():
    '''
    contains all the task information
    list:contains TaskText Objects
    seed_list:contains (x,y) coords to draw the pattern
    '''
    def __init__(self,win):
        self.list=[]
        self.seed_list=[]
        self.win=win
        self.list.append(TaskText(self.win,1,"生命繁衍3代后等于7个生命",1,3,7))
        self.list.append(TaskText(self.win,2,"生命繁衍30代后等于9个生命",1,30,9))
        self.list.append(TaskText(self.win,3,"生命繁衍25代后等于18个生命",1,25,18))
        self.list.append(TaskText(self.win,4,"生命繁衍30代后等于19个生命",1,30,19))
        self.list.append(TaskText(self.win,5,"生命繁衍6代后等于10个生命",1,6,10))
        self.list.append(TaskText(self.win,6,"生命繁衍20代后等于36个生命",4,20,36))
        self.seed_list.append(task1)
        self.seed_list.append(task2)
        self.seed_list.append(task3)
        self.seed_list.append(task4)
        self.seed_list.append(task5)
        self.seed_list.append(task6)
        
    def draw_task(self,pos,board):
        #draw the task text
        self.undraw_task()
        self.list[pos].draw_text()
        #draw the task pattern
        board.reset()
        board.seed(self.seed_list[pos])
        board.set_clickable(True)
    
    def get_times(self,pos):
        return self.list[pos].get_animate_time()
    
    def get_live(self,pos):
        return self.list[pos].get_target_count()
    
    def get_left_num(self,pos):
        return self.list[pos].get_left()
    
    def undraw_task(self):
        for i in self.list:
            i.undraw_text()
        
class BoardThread(threading.Thread):
    '''
    BoardThread is used to show animatino in a new thread
    this thread lives as long as the main thread
    times:(Text)to show the gengerate times on canvas
    numbers:(Text)to show the present live life count on canvas
    '''
    def __init__(self,win,board,start_btn):
        threading.Thread.__init__(self)
        self.thread_stop=False
        self.start_btn=start_btn
        self.board=board
        self.count=100000
        self.win=win
        self.live=0
        self.loop_time=0
        
        self.is_success_show=False
        self.is_fail_show=False
        self.times=Text(Point(TEXT_POS_x,120),"生命代数："+str(0))
        self.numbers=Text(Point(TEXT_POS_x,170),"生命个数："+str(0))
        self.times.setTextColor(TEXT_COLOR)
        self.numbers.setTextColor(TEXT_COLOR)
        self.times.draw(self.win)
        self.numbers.draw(self.win)
        
    def run(self):
        while True:
            while not self.thread_stop and self.count>0:
                self.board.animate()
                self.count-=1
                self.loop_time+=1
                self.show_info()
            if self.count==0:
                self.stop()
                self.check_success()
                time.sleep(2)
                self.undraw_msg()
                
    def is_running(self):
        if not self.thread_stop and self.count>0:
            return True
        return False
    def stop(self):
        
        
        self.thread_stop=True
        #time.sleep(0.05)
        self.start_btn.activate()
        self.count=100000
        self.loop_time=0
    
    def pause(self,second):
        flag=self.is_running()
        self.thread_stop=True
        #time.sleep(second)
        if flag:
            self.thread_stop=False
        
    def continue_thread(self):
        
        self.thread_stop=False
        #time.sleep(0.05)
        self.start_btn.deactivate()
        self.times.setText("生命代数:1")
        self.numbers.setText("生命个数:"+str(self.board.get_live_count()))
    
    #used for setting the loop time required for task mode    
    def set_count(self,count):
        self.thread_stop=True
        time.sleep(0.05)
        self.start_btn.activate()
        self.count=count
        self.loop_time=0

    #show the generate times and live num real-time on screen
    def show_info(self):
        self.times.setText("生命代数:"+str(self.loop_time))
        self.numbers.setText("生命个数:"+str(self.board.get_live_count()))
        self.times.setTextColor(TEXT_COLOR)
        self.numbers.setTextColor(TEXT_COLOR)
        
    #called when the task animation finished
    #show the result when called
    def check_success(self):
        self.live=self.board.get_live_count()
        global TARGET_COUNT
        print "check success live count:",TARGET_COUNT
        if self.live==TARGET_COUNT:
            self.success_msg=Text(Point(600,350),"success")
            self.success_msg.setSize(36)
            self.success_msg.setFill(TEXT_COLOR)
            self.success_msg.draw(self.win)
            self.is_success_show=True
        else:
            self.fail_msg= Text(Point(600,350),"failed")
            self.fail_msg.setSize(36)
            self.fail_msg.setFill(TEXT_COLOR)
            self.fail_msg.draw(self.win)
            self.is_fail_show=True  
    
    #undraw the result(success or fail)
    def undraw_msg(self):
        if self.is_fail_show:
            self.fail_msg.undraw()
        if self.is_success_show:
            self.success_msg.undraw()
          

    
def testBoard():
    win = GraphWin("Game of Life",BOARD_WIDTH * BLOCK_SIZE+BUTTON_WIDTH,BOARD_HEIGHT * BLOCK_SIZE)    
    board = Board(win, BOARD_WIDTH, BOARD_HEIGHT)
    board.seed(random.choice(example))
    #board,random_seed(0.15)
    while True:
        board.animate()
    
    win.close()
    
def main():    
    global example
    global CLEARABLE
    win = GraphWin("Cody's Game of Life",BOARD_WIDTH * BLOCK_SIZE+BUTTON_WIDTH,BOARD_HEIGHT * BLOCK_SIZE)
    #############################################################
    #init function button
    ##############################################################
    exampleSeedBtn=Button(win,Point(BOARD_WIDTH * BLOCK_SIZE+60,BOARD_HEIGHT * BLOCK_SIZE-260),90,30,"ExampSeed")
    randomBtn=Button(win,Point(BOARD_WIDTH * BLOCK_SIZE+60,BOARD_HEIGHT * BLOCK_SIZE-220),90,30,"RandSeed")
    startBtn=Button(win,Point(BOARD_WIDTH * BLOCK_SIZE+50,BOARD_HEIGHT * BLOCK_SIZE-350),80,35,"start")
    stopBtn=Button(win,Point(BOARD_WIDTH * BLOCK_SIZE+140,BOARD_HEIGHT * BLOCK_SIZE-350),80,35,"stop")
    exitBtn=Button(win,Point(BOARD_WIDTH * BLOCK_SIZE+100,BOARD_HEIGHT * BLOCK_SIZE-30),110,40,"Exit")
    clearBtn=Button(win,Point(BOARD_WIDTH * BLOCK_SIZE+100,BOARD_HEIGHT * BLOCK_SIZE-80),110,40,"clear")
    freeBtn=Button(win,Point(BOARD_WIDTH * BLOCK_SIZE+100,BOARD_HEIGHT * BLOCK_SIZE-130),110,40,"FreeEditMode")
    fastBtn=Button(win,Point(BOARD_WIDTH * BLOCK_SIZE+50,BOARD_HEIGHT * BLOCK_SIZE-310),80,35,"Fast")
    slowBtn=Button(win,Point(BOARD_WIDTH * BLOCK_SIZE+140,BOARD_HEIGHT * BLOCK_SIZE-310),80,35,"Slow")
    storeSeedBtn=Button(win,Point(BOARD_WIDTH * BLOCK_SIZE+60,BOARD_HEIGHT * BLOCK_SIZE-180),90,30,"StoreSeed")
    resetSeedBtn=Button(win,Point(BOARD_WIDTH * BLOCK_SIZE+160,BOARD_HEIGHT * BLOCK_SIZE-180),90,30,"ResetSeed")
    lastBtn=Button(win,Point(BOARD_WIDTH * BLOCK_SIZE+160,BOARD_HEIGHT * BLOCK_SIZE-260),50,30,"Last")
    
    deletBtn=Button(win,Point(BOARD_WIDTH * BLOCK_SIZE+160,BOARD_HEIGHT * BLOCK_SIZE-220),80,30,"deleteSeed")
    
    #lastBtn.activate()
    storeSeedBtn.activate()
    slowBtn.activate()
    #fastBtn.activate()
    freeBtn.activate()
    exampleSeedBtn.activate()
    randomBtn.activate()
    startBtn.activate()
    stopBtn.activate()
    exitBtn.activate()
    clearBtn.activate()
    resetSeedBtn.activate()

    
    task_list=TaskList(win)
    
    board = Board(win, BOARD_WIDTH, BOARD_HEIGHT)
    
    boardThread=BoardThread(win,board,startBtn)
    
    boardThread.setDaemon(True)
    boardThread.start()
    boardThread.stop()
    
    board.set_clickable(True)
    
    task = Task(win,task_list,board,boardThread)
    
    task.show_free_mode_test()
    
    example_count=10
    global is_example_show
    
    while True:
        if is_example_show:
                deletBtn.activate()
        else:
            deletBtn.deactivate()
            
        q=win.getMouse()
        x=int(q.getX()/BLOCK_SIZE)
        y=int(q.getY()/BLOCK_SIZE)
        #print "(%d,%d)"%(x,y)
        
        #listen on task btn click
        task.respond_click(q)
        
        #listen on board click
        if board.clickable and x>0 and x<BOARD_WIDTH and y>0 and y<BOARD_HEIGHT:
            board.respond_click(x,y)
        
        #init clear button state        
        if CLEARABLE==False :
            clearBtn.deactivate()
        else:
            clearBtn.activate()
            
        
        #used for generate the list for present patterns    
        if storeSeedBtn.clicked(q):
            board.generate_list()
            
        if deletBtn.clicked(q):
            board.delete_list(example_count)
            #example_count-=1
        if resetSeedBtn.clicked(q):
            is_example_show=True
            f=open('origin_template','r')
            example=pickle.load(f)
            f.close()
            f=open('template','w')
            pickle.dump(example,f,0)
        #set the generate speed    
        if fastBtn.clicked(q):
            fastBtn.deactivate()
            slowBtn.activate()
            boardThread.pause(0.1)
            board.set_speed('fast')
        if slowBtn.clicked(q):
            slowBtn.deactivate()
            fastBtn.activate()
            boardThread.pause(0.1)
            board.set_speed('slow')
            
        #show example seed randomly
        if exampleSeedBtn.clicked(q):
            is_example_show=True
            
            boardThread.stop()
            ################################################################################
            #不延迟一下的话会有bug，有时候点击一下无法达到效果                             #
            #主要原因是boreadThread线程被暂停的时候时间是不精确的，需要主动延迟保证线程逻辑#
            time.sleep(0.1)                                                                #
            ################################################################################
            
            f=open('template','r')
            example=pickle.load(f)
            f.close()
            #EXAMPLE_NUM=len(example)
            
            CLEARABLE=True
            clearBtn.activate()
            lastBtn.activate()
            task.show_free_mode_test()
            #print boardThread.isAlive()
            task.undraw_task_text()         
            board.reset()
            #############################################
            #board.seed(random.choice(example))
            example_count+=1
            if example_count>=len(example):
                example_count=0
            board.seed(example[example_count])
            #############################################
            board.set_clickable(True)
        if lastBtn.clicked(q):
            is_example_show=True
            boardThread.stop()
            time.sleep(0.1)
            
            CLEARABLE=True
            clearBtn.activate()
            task.show_free_mode_test()
            #print boardThread.isAlive()
            task.undraw_task_text()         
            board.reset()
                
            example_count-=1
            
            board.seed(example[example_count])
        #enable free edit mode
        if freeBtn.clicked(q):
            is_example_show=False
            boardThread.stop()
            time.sleep(0.1)
            board.reset()
            CLEARABLE=True
            clearBtn.activate()
            task.show_free_mode_test()
            task.undraw_task_text()
            board.set_clickable(True)
        
        #using random seed
        if randomBtn.clicked(q):
            is_example_show=False
            boardThread.stop()
            time.sleep(0.1)
            #board.reset()
            CLEARABLE=True
            clearBtn.activate()
            task.show_free_mode_test()
            task.undraw_task_text()
            board.random_seed(0.05)
            
        #clear the board
        if clearBtn.clicked(q):
            is_example_show=False
            boardThread.stop()
            time.sleep(0.1)
            board.reset()
            
        #exit the program
        if exitBtn.clicked(q):
            break
                    
        #start to animate
        if startBtn.clicked(q):
            #disable board click
            board.set_clickable(False)
            #print boardThread.isAlive()
            boardThread.continue_thread()  
                
        #stop animating         
        if stopBtn.clicked(q):
            #enable board click
            board.set_clickable(True)
            boardThread.stop()
             
    
    win.close()
    
main()                

