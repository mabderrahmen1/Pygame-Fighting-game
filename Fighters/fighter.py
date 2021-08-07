import pygame,os,sys

from pygame.constants import K_SPACE, K_a, K_d, K_q, K_w, MOUSEBUTTONDOWN

pygame.init()
clock = pygame.time.Clock()
widht,height=1000,600
screen=pygame.display.set_mode((widht,height))
pygame.display.set_caption("fighters")
FPS=45
BLACK=(0,0,0)
GREEN=(0,255,0)
RED=(255,0,0)


#--------------------loading cities--------------------
forest1=pygame.image.load("Fighters\\assets\\forest\\forest1.png")
forest1=pygame.transform.scale(forest1,(widht,height))
forest2=pygame.image.load("Fighters\\assets\\forest\\forest2.png")
forest2=pygame.transform.scale(forest2,(widht,height))
forest3=pygame.image.load("Fighters\\assets\\forest\\forest3.png")
forest3=pygame.transform.scale(forest3,(widht,height))
forest4=pygame.image.load("Fighters\\assets\\forest\\forest4.png")
forest4=pygame.transform.scale(forest4,(widht,height))
#------------------loading annimations----------------
knightImage=pygame.image.load("Fighters\\assets\\fighters\\silver_knight\\1_IDLE_000.png")
knightImage=pygame.transform.scale(knightImage,(100,150))
warriorImage=pygame.image.load("Fighters\\assets\\fighters\\bronze_knight\\1_IDLE_000.png")
warriorImage=pygame.transform.scale(warriorImage,(100,150))
#------------walking-----------
walk1=pygame.image.load("Fighters\\assets\\fighters\\silver_knight\\2_WALK_000.png")
walk1=pygame.transform.scale(walk1,(100,150))
walk2=pygame.image.load("Fighters\\assets\\fighters\\silver_knight\\2_WALK_001.png")
walk2=pygame.transform.scale(walk2,(100,150))
walk3=pygame.image.load("Fighters\\assets\\fighters\\silver_knight\\2_WALK_002.png")
walk3=pygame.transform.scale(walk3,(100,150))
walk4=pygame.image.load("Fighters\\assets\\fighters\\silver_knight\\2_WALK_003.png")
walk4=pygame.transform.scale(walk4,(100,150))
walk5=pygame.image.load("Fighters\\assets\\fighters\\silver_knight\\2_WALK_004.png")
walk5=pygame.transform.scale(walk5,(100,150))
knightWalk=[walk1,walk2,walk3,walk4,walk5]
#------------runinging-----------
run1=pygame.image.load("Fighters\\assets\\fighters\\silver_knight\\3_RUN_000.png")
run1=pygame.transform.scale(run1,(100,150))
run2=pygame.image.load("Fighters\\assets\\fighters\\silver_knight\\3_RUN_001.png")
run2=pygame.transform.scale(run2,(100,150))
run3=pygame.image.load("Fighters\\assets\\fighters\\silver_knight\\3_RUN_002.png")
run3=pygame.transform.scale(run3,(100,150))
run4=pygame.image.load("Fighters\\assets\\fighters\\silver_knight\\3_RUN_003.png")
run4=pygame.transform.scale(run4,(100,150))
run5=pygame.image.load("Fighters\\assets\\fighters\\silver_knight\\3_RUN_004.png")
run5=pygame.transform.scale(run5,(100,150))
knightRun=[run1,run2,run3,run4,run5]
#------------jumping-----------
jump1=pygame.image.load("Fighters\\assets\\fighters\\silver_knight\\4_JUMP_000.png")
jump1=pygame.transform.scale(jump1,(100,150))
jump2=pygame.image.load("Fighters\\assets\\fighters\\silver_knight\\4_JUMP_001.png")
jump2=pygame.transform.scale(jump2,(100,150))
jump3=pygame.image.load("Fighters\\assets\\fighters\\silver_knight\\4_JUMP_002.png")
jump3=pygame.transform.scale(jump3,(100,150))
jump4=pygame.image.load("Fighters\\assets\\fighters\\silver_knight\\4_JUMP_003.png")
jump4=pygame.transform.scale(jump4,(100,150))
jump5=pygame.image.load("Fighters\\assets\\fighters\\silver_knight\\4_JUMP_004.png")
jump5=pygame.transform.scale(jump5,(100,150))
knightJump=[jump1,jump2,jump3,jump4,jump5]
#------------attacking-----------
attack1=pygame.image.load("Fighters\\assets\\fighters\\silver_knight\\5_ATTACK_000.png")
attack1=pygame.transform.scale(attack1,(125,175))
attack2=pygame.image.load("Fighters\\assets\\fighters\\silver_knight\\5_ATTACK_001.png")
attack2=pygame.transform.scale(attack2,(125,175))
attack3=pygame.image.load("Fighters\\assets\\fighters\\silver_knight\\5_ATTACK_002.png")
attack3=pygame.transform.scale(attack3,(125,175))
attack4=pygame.image.load("Fighters\\assets\\fighters\\silver_knight\\5_ATTACK_003.png")
attack4=pygame.transform.scale(attack4,(125,175))
attack5=pygame.image.load("Fighters\\assets\\fighters\\silver_knight\\5_ATTACK_004.png")
attack5=pygame.transform.scale(attack5,(125,175))
knightAttack=[attack1,attack2,attack3,attack4,attack4]
#------------death-----------
die1=pygame.image.load("Fighters\\assets\\fighters\\silver_knight\\6_DIE_000.png")
die1=pygame.transform.scale(die1,(100,150))
die2=pygame.image.load("Fighters\\assets\\fighters\\silver_knight\\6_DIE_001.png")
die2=pygame.transform.scale(die2,(100,150))
die3=pygame.image.load("Fighters\\assets\\fighters\\silver_knight\\6_DIE_002.png")
die3=pygame.transform.scale(die3,(100,150))
die4=pygame.image.load("Fighters\\assets\\fighters\\silver_knight\\6_DIE_003.png")
die4=pygame.transform.scale(die4,(100,150))
die5=pygame.image.load("Fighters\\assets\\fighters\\silver_knight\\6_DIE_004.png")
die5=pygame.transform.scale(die5,(100,150))
knightDie=[die1,die2,die3,die4,die5]
#===================================warrior annimation==================================
wariorWalk1=pygame.image.load("Fighters\\assets\\fighters\\bronze_knight\\2_WALK_000.png")
wariorWalk1=pygame.transform.scale(wariorWalk1,(150,200))
wariorwalk2=pygame.image.load("Fighters\\assets\\fighters\\bronze_knight\\2_WALK_001.png")
wariorWalk2=pygame.transform.scale(wariorwalk2,(150,200))
wariorWalk3=pygame.image.load("Fighters\\assets\\fighters\\bronze_knight\\2_WALK_002.png")
wariorWalk3=pygame.transform.scale(wariorWalk3,(150,200))
wariorWalk4=pygame.image.load("Fighters\\assets\\fighters\\bronze_knight\\2_WALK_003.png")
wariorWalk4=pygame.transform.scale(wariorWalk4,(150,200))
wariorWalk5=pygame.image.load("Fighters\\assets\\fighters\\bronze_knight\\2_WALK_004.png")
wariorWalk5=pygame.transform.scale(wariorWalk5,(150,200))
warriorWalk=[wariorWalk1,wariorWalk2,wariorWalk3,wariorWalk4,wariorWalk5]
#------------runinging-----------
wariorRun1=pygame.image.load("Fighters\\assets\\fighters\\bronze_knight\\3_RUN_000.png")
wariorRun1=pygame.transform.scale(wariorRun1,(150,200))
wariorRun1=pygame.transform.flip(wariorRun1,True, False)
wariorRun2=pygame.image.load("Fighters\\assets\\fighters\\bronze_knight\\3_RUN_001.png")
wariorRun2=pygame.transform.scale(wariorRun2,(150,200))
wariorRun2=pygame.transform.flip(wariorRun2,True, False)
wariorRun3=pygame.image.load("Fighters\\assets\\fighters\\bronze_knight\\3_RUN_002.png")
wariorRun3=pygame.transform.scale(wariorRun3,(150,200))
wariorRun3=pygame.transform.flip(wariorRun3,True, False)
wariorRun4=pygame.image.load("Fighters\\assets\\fighters\\bronze_knight\\3_RUN_003.png")
wariorRun4=pygame.transform.scale(wariorRun4,(150,200))
wariorRun4=pygame.transform.flip(wariorRun4,True, False)
wariorRun5=pygame.image.load("Fighters\\assets\\fighters\\bronze_knight\\3_RUN_004.png")
wariorRun5=pygame.transform.scale(wariorRun5,(150,200))
wariorRun5=pygame.transform.flip(wariorRun5,True, False)
warriorRun=[wariorRun1,wariorRun2,wariorRun3,wariorRun4,wariorRun5]
#------------jumping-----------
wariorJump1=pygame.image.load("Fighters\\assets\\fighters\\bronze_knight\\4_JUMP_000.png")
wariorJump1=pygame.transform.scale(wariorJump1,(150,200))
wariorJump2=pygame.image.load("Fighters\\assets\\fighters\\bronze_knight\\4_JUMP_001.png")
wariorJump2=pygame.transform.scale(wariorJump2,(150,200))
wariorJump3=pygame.image.load("Fighters\\assets\\fighters\\bronze_knight\\4_JUMP_002.png")
wariorJump3=pygame.transform.scale(wariorJump3,(150,200))
wariorJump4=pygame.image.load("Fighters\\assets\\fighters\\bronze_knight\\4_JUMP_003.png")
wariorJump4=pygame.transform.scale(wariorJump4,(150,200))
wariorJump5=pygame.image.load("Fighters\\assets\\fighters\\bronze_knight\\4_JUMP_004.png")
wariorJump5=pygame.transform.scale(wariorJump5,(150,200))
warriorJump=[wariorJump1,wariorJump2,wariorJump3,wariorJump4,wariorJump5]
#------------attacking-----------
wariorAttack1=pygame.image.load("Fighters\\assets\\fighters\\bronze_knight\\5_ATTACK_000.png")
wariorAttack1=pygame.transform.scale(wariorAttack1,(150,200))
wariorAttack2=pygame.image.load("Fighters\\assets\\fighters\\bronze_knight\\5_ATTACK_001.png")
wariorAttack2=pygame.transform.scale(wariorAttack2,(150,200))
wariorAttack3=pygame.image.load("Fighters\\assets\\fighters\\bronze_knight\\5_ATTACK_002.png")
wariorAttack3=pygame.transform.scale(wariorAttack3,(150,200))
wariorAttack4=pygame.image.load("Fighters\\assets\\fighters\\bronze_knight\\5_ATTACK_003.png")
wariorAttack4=pygame.transform.scale(wariorAttack4,(150,200))
wariorAttack5=pygame.image.load("Fighters\\assets\\fighters\\bronze_knight\\5_ATTACK_004.png")
wariorAttack5=pygame.transform.scale(wariorAttack5,(150,200))
warriorAttack=[wariorAttack1,wariorAttack2,wariorAttack3,wariorAttack4,wariorAttack5]






#----------------creating the fighter class-------------------
class Fighter:
    def __init__(self,x,y,widht,height):
        self.x=x
        self.y=y
        self.widht=widht
        self.height=height
        self.fighterVel=10
        self.jumpCount=10
        self.jump=False
        self.walk=False
        self.walkCount=0
        self.attack=False
        self.attackCount=0
        self.hp=5000
        self.damage=30
        self.dead=False
        self.deathCount=0

    def draw(self,screen):
        if self.walkCount+1>=15 or self.attackCount+1>=15 or self.deathCount+1>=15:
            self.walkCount=0
            self.attackCount=0
            self.deathCount=0
        if self.walk:
            screen.blit(knightRun[self.walkCount//3],(self.x,self.y))
            self.walkCount+=1
        elif self.attack :
            screen.blit(knightAttack[self.attackCount//3],(self.x,self.y))
            self.attackCount+=1
            
        elif self.dead:
            screen.blit(knightDie[self.deathCount//3],(self.x,self.y))
            self.deathCount+=1

        else:
            screen.blit(knightImage,(self.x,self.y))


    def mouvement(self,keys):
        if keys[K_a] and self.x>=0:
            self.x-=self.fighterVel
            self.walk=True
            self.attack=False
            self.dead=False
        elif keys[K_d] and self.x<=widht-100:
            self.x+=self.fighterVel
            self.walk=True
            self.attack=False
            self.dead=False
        elif keys[K_q]:    
            self.attack=True
            self.walk=False
            self.dead=False
        else:
            self.walk=False
            self.dead=False
            self.walkCount=0
            self.attack=False
            self.attackCount=0
        if self.hp<=0:
            self.dead=True
            self.walk=False
            self.attack=False
            self.jump=False
            


        if not self.jump:
            if keys[K_w]:
                self.jump=True  
                self.walk=False
                self.dead=False
                self.attack=False
                self.walkCount=0
                self.attackCount=0

        else:
            if self.jumpCount>=-10:
                neg=1
                if self.jumpCount<0:
                    neg=-1
                self.y-=(self.jumpCount**2)*0.5*neg
                self.jumpCount-=1
            else:
                self.jump=False
                self.jumpCount=10
        
    
        


class Enemy():
    def __init__(self,x,y,widht,height):
        self.x=x
        self.y=y
        self.widht=widht
        self.height=height
        self.enemyVel=3
        self.walk=True
        self.walkCount=0
        self.attack=False
        self.attackCount=0
        self.hp=1500
        self.damage=20


    #other knight
    def draw(self,screen):
        if self.walkCount+1>=15 or self.attackCount+1>=15:
            self.walkCount=0
            self.attackCount=0
        if self.walk:
            screen.blit(warriorRun[self.walkCount//3],(self.x,self.y))
            self.walkCount+=1
        elif self.attack :
            screen.blit(warriorAttack[self.attackCount//3],(self.x,self.y))
            self.attackCount+=1
        

    def mouvements(self):
        if self.x>=0:
            self.x-=self.enemyVel
        if self.x>=widht-150 :
            self.enemyVel=3      
        if self.x==50:
            self.enemyVel=-3
        



#----------------menu fonction------------
def mainMenu():
    running=True
    while running:
        clock.tick(FPS)
        screen.blit(forest2,(0,0))
        mx,my=pygame.mouse.get_pos()
        start1P=pygame.Rect(400,200,200,50)
        start2P=pygame.Rect(400,300,200,50)
        credits=pygame.Rect(400,400,200,50)
        leave=pygame.Rect(400,500,200,50)
        pygame.draw.rect(screen,BLACK,start1P)
        pygame.draw.rect(screen,BLACK,start2P)
        pygame.draw.rect(screen,BLACK,leave)
        pygame.draw.rect(screen,BLACK,credits)
        if start1P.collidepoint(mx,my):
            if click:
                main()
        if start2P.collidepoint(mx,my):
            if click:
                main()
        if credits.collidepoint(mx,my):
            if click:
                pass
        if leave.collidepoint(mx,my):
            if click:
                sys.exit()
        click=False
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            if event.type==MOUSEBUTTONDOWN:
                if event.button==1:
                    click=True
        pygame.display.update()
    sys.exit()

#--------------main Loop ------------------
def main():
    run =True
    knight=Fighter(100,400,100,150)
    warrior=Enemy(500,350,100,150)
    knifeW,knifeH=45,120
    while run:
        screen.blit(forest1,(0,0))
        clock.tick(FPS)
        #-----------drawing and animating the knight-------------
        knighthp=pygame.Rect(0,0,knight.hp//10,20)
        warriorhp=pygame.Rect(widht-150,0,warrior.hp//10,20)
        knightRect=pygame.Rect(knight.x,knight.y,100,150)
        warriorRect=pygame.Rect(warrior.x+20,warrior.y+20,100,170)
        knifeRect=pygame.Rect(knight.x+75,knight.y+20,knifeW,knifeH)


        knight.draw(screen)
        warrior.draw(screen)
        pygame.draw.rect(screen,GREEN,knighthp)
        pygame.draw.rect(screen,RED,warriorhp)
        #---------------mouvement of the knight--------------
        keys_pressed=pygame.key.get_pressed()
        knight.mouvement(keys_pressed)
        warrior.mouvements()
       
       #----------------enemy collision-----------------
        if warriorRect.colliderect(knightRect):
            knight.hp-=warrior.damage
         #------------------knife collision-----------------
        if warriorRect.colliderect(knifeRect):
            if keys_pressed[K_q]:
                warrior.hp-=knight.damage
        

        print("warrior hp :" , warrior.hp)
        print("knight hp :" , knight.hp)
        #--------------------window control-------------------
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            

        pygame.display.update()
    sys.exit()

#-----------starting the game---------
mainMenu()