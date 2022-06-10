###
### Author: Sherali Ozodov
### Course: CSc 110
### Description: this program builds a program that displays 
### a landscape in a graphics canvas and allows the user
### to control the distance at which the landscape is viewed from. 

from graphics import graphics
import random 

def grass(gui):
    '''This function draws green lines 
    and the height of these lines is determined 
    by user that controls distance 
    '''
    x=-20
    y=gui.mouse_y
    while x<700:
        gui.line(x,320,x,-0.097*y + 325,'green',2)
        x+=5
def mountain(gui):
        '''This function draws a brown tringle, and 
        represents x and y cordinates'''
        x=gui.mouse_y
        gui.triangle(350,-0.6*x+250,100,400,600,400,'brown')
        gui.text(0, 0, "x=" + str(gui.mouse_x), 'black', 20)
        gui.text(0, 30, "y=" + str(gui.mouse_y), 'black', 20)
def lake_ellipse(gui):
        '''This function draws a blue lake'''
        x=gui.mouse_y
        gui.ellipse(350,0.22*x+320,0.57*x+15,1/35*x+6,'blue')     
def tree_ellipse(gui):
        '''This function draws a green ellipse of the tree'''
        x=gui.mouse_y
        gui.ellipse(-0.867*x+320, -0.13*x+320, 0.6*x + 1, 0.8*x + 1,'green')
        gui.ellipse(0.867*x+380,-0.13*x+320,0.6*x+1,0.8*x + 1,'green')
def tree_foot_rec(gui):
        '''This function draws a brown body of the tree'''
        x=gui.mouse_y        
        gui.rectangle(-0.96*x+320,-0.19*x+321,0.19*x+1,0.86*x+1,'brown')
        gui.rectangle(0.78*x + 379,-0.19*x+321,0.19*x+1,0.86*x+1,'brown')        
def shapes(gui): 
        '''This function includes some ready shapes and print them out'''
        mountain(gui)
        grass(gui)
        gui.rectangle(0,320,700,500,'Pale green') 
        tree_foot_rec(gui)
        tree_ellipse(gui)
        lake_ellipse(gui)
        
def main():
    cloud_x_1=random.randint(55,645)
    cloud_y_1=random.randint(80,200)
    cloud_x_2=random.randint(55,645)
    cloud_y_2=random.randint(80,200)
    cloud_x_3=random.randint(55,645)
    cloud_y_3=random.randint(80,200)
    cloud_x_4=random.randint(55,645)
    cloud_y_4=random.randint(80,200) 
    b=0
    gui = graphics(700,500,'Vanishing Point')   
    while True:
        gui.clear()
        gui.rectangle(0,0,700,500,'Sky Blue') 
        ## it prints random position clouds
        gui.ellipse(cloud_x_1,cloud_y_1,110,80,'white')
        gui.ellipse(cloud_x_2,cloud_y_2,100,60,'white')
        gui.ellipse(cloud_x_3,cloud_y_3,110,80,'white')
        gui.ellipse(cloud_x_4,cloud_y_4,110,80,'white') 
        ## it prints sun
        gui.ellipse(b,1/1400*(b-350)**2+35,70,70,'yellow')  
        shapes(gui)
        b+=2
        if b>700:
           b=-20
        gui.update_frame(20) 
    gui.primary.mainloop()
main()   