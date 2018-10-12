import math
import time

class HanoiBoard:

    def  __init__(self,numOfCircles):
        self.towers=[list(),list(),list(),list()]


        for i in range(numOfCircles,0,-1):
            self.towers[0].append(Circle(i))


			# init all towers 
        self.towers[0].insert(0,Circle(numOfCircles+1)) 
        self.towers[1].insert(0,Circle(numOfCircles+1))
        self.towers[2].insert(0,Circle(numOfCircles+1))
        self.towers[3].insert(0,Circle(numOfCircles+1)) 
         




class Circle:

    def  __init__(self,level):
        self.level=level

    def __str__(self):
        return "level %s"%self.level

    






def sloveHanoiForThreeTowers(source,middle,end,divider):

    power= len(source)-1
    n=2**(math.ceil(power/divider))-1
   
    if (math.ceil(power/divider))%2==0: #even

 
        while n>0:

            if source[len(source)-1].level<middle[len(middle)-1].level:
                middle.append(source.pop())
                
                n=n-1
                if n==0:
                    break
 
            elif  source[len(source)-1].level>middle[len(middle)-1].level:
                source.append(middle.pop())
              
                n=n-1
                if n==0:
                    break

         
            if source[len(source)-1].level<end[len(end)-1].level:
                end.append(source.pop())
                n=n-1
                if n==0:
                    break

            elif  source[len(source)-1].level>end[len(end)-1].level:
                source.append(end.pop())
                n=n-1
                if n==0:
                    break

            

            if middle[len(middle)-1].level<end[len(end)-1].level:
                end.append(middle.pop())
                n=n-1
                if n==0:
                    break 



            elif  middle[len(middle)-1].level>end[len(end)-1].level:
                middle.append(end.pop())
                n=n-1
                if n==0:
                    break  
              
           

    else:
        while n>0:

            if source[len(source)-1].level<end[len(end)-1].level:
                end.append(source.pop())
               
                n=n-1
                if n==0:
                    break
            elif  source[len(source)-1].level>end[len(end)-1].level:
                source.append(end.pop())
                n=n-1
                if n==0:
                    break


         
            if source[len(source)-1].level<middle[len(middle)-1].level:
                middle.append(source.pop())
                n=n-1
                if n==0:
                    break

            elif  source[len(source)-1].level>middle[len(middle)-1].level:
                source.append(middle.pop())
                n=n-1
                if n==0:
                    break

            

            if middle[len(middle)-1].level<end[len(end)-1].level:
                end.append(middle.pop())
                n=n-1
                if n==0:
                    break
                

            elif  middle[len(middle)-1].level>end[len(end)-1].level:
                middle.append(end.pop())
                n=n-1
                if n==0:
                    break






        
    


def HanoiSlovingForFourTowers(board):
    before = int(round(time.time() ))
    sloveHanoiForThreeTowers(board.towers[0],board.towers[1],board.towers[2],2)
    sloveHanoiForThreeTowers(board.towers[0],board.towers[1],board.towers[3],1)
    sloveHanoiForThreeTowers(board.towers[2],board.towers[1],board.towers[3],1)
    after = int(round(time.time() ))
    print(after-before)


if __name__ == "__main__":

    board = HanoiBoard(45)
    HanoiSlovingForFourTowers(board)




