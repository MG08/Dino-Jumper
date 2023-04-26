import pygame
import random


print("Hello world")
pygame.init()
screen = pygame.display.set_mode((640,550))
pygame.display.set_caption("Dino Jumper")
doExit=False
clock = pygame.time.Clock()
#game variables go here, above the game loop
p1x = 20
p1y = 450
yVel = 0
touchGround = False

CactusHeights= [20,20,20,20,20]

CactusXpos=[]
   
for x in range(1 ,5):
       CactusXpos.append(random.randrange(200, 3000))

CactusImg = pygame.image.load('cactus.png')
CactusImg.set_colorkey((255, 255, 255))
#game loop####################################
while not doExit:
    
    clock.tick(100000000000000000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True;

    p1y += yVel
    
    if (p1y+30) == 480:
        touchGround = True
    else:
        touchGround = False

    if touchGround == False:
        yVel += 1
    else:
        yVel = 0
    #game logic
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and touchGround == True:
        yVel=-20
   
   
    #timer section//////////////
   
            
    clock.tick(100)
    
    CactusXpos = [x - 5 for x in CactusXpos]
    
    for x in range(len(CactusXpos)):
        if CactusXpos[x]<0:
            CactusXpos[x]=random.randrange(640,5000)
            print("reset to", CactusXpos[x])
            
    for x, y in zip(CactusXpos, CactusHeights):
        a = pygame.Rect((x,480-y), (30,80))
        b = pygame.Rect((p1x, p1y), (30, 30))
        if a.colliderect(b) == True:
            print("COLLISION")
    #input section////////////////////
    
    #render section//////////////////
    screen.fill((0,0,0))
    
    pygame.draw.rect(screen, (255, 255, 255), (p1x, p1y, 20, 100), 1)
    
    for x, y in zip(CactusXpos, CactusHeights):
       screen.blit(CactusImg, (x-15,480-y))
    
    pygame.display.flip()
#end game loop############################
    
pygame.quit()
