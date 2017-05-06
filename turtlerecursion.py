import turtle

myturtle  = turtle.Turtle()

def spiral_helper(sideLen, num):
    if num==0:
       return
    else:
                    
       myturtle.forward(sideLen)
       myturtle.left(90)
       spiral_helper(1.1*sideLen, num -1)

def spiral(sideLen, num):
    spiral_helper(sideLen,2*num)


if __name__=='__main__':
    spiral(20,20)
    turtle.done()



    
 
