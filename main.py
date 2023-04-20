import pygame

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


#game loop####################################
while not doExit:
    
    clock.tick(60)
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
   
   Cactusheights= [80,40,20,80,30]
   
   CactusxXpos=[]
   
   for x in range(1,5):
       CactusXpos.append(random.randrange(200, 300))
    #timer section//////////////
   
            
    clock.tick(60)
    
    #input section////////////////////
    
    #render section//////////////////
    screen.fill((0,0,0))
    
    pygame.draw.rect(screen, (255, 255, 255), (p1x, p1y, 20, 100), 1)
    
   
    
    pygame.display.flip()
#end game loop############################
    
pygame.quit()
