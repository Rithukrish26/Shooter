

import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Basics")

background_color = (224,191,184)

running = True

bgimg = pygame.image.load('Assets-shooter/Stall/bg_wood.png')
bgimg = pygame.transform.scale(bgimg, (800,600))
curtain = pygame.image.load('Assets-shooter/Stall/curtain.png')
curtain = pygame.transform.scale(curtain, (75,600))
topcurtain = pygame.image.load('Assets-shooter/Stall/curtain_top.png')
topcurtain = pygame.transform.scale(topcurtain, (800,75))
curtain2 = pygame.transform.flip(curtain, True, False)
grass = pygame.image.load('Assets-shooter/Stall/grass2.png')
water = pygame.image.load('Assets-shooter/Stall/water2.png')
water2 = pygame.image.load('Assets-shooter/Stall/water1.png')
whiteduck = pygame.image.load('Assets-shooter/Objects/duck_white.png')
duck = pygame.image.load('Assets-shooter/Objects/duck_yellow.png')
rifle = pygame.image.load('Assets-shooter/Objects/rifle.png')
rifle = pygame.transform.scale(rifle, (70,70))
bullets = 3
bulletsleft = bullets

font = pygame.font.SysFont("Impact", 30)

targetrect = duck.get_rect()
targetrect.topleft = (100,100)
targetspeed = 5

targetrect2 = whiteduck.get_rect()
targetrect2.topleft = (300,200)
targetspeed2 = 3

riflerect = rifle.get_rect()
riflerect.midbottom = (430,530)

clock = pygame.time.Clock()

points = 0

bullet = []
bulletspeed = 6

scoreimglist = ["text_0.png","text_1.png","text_2.png","text_3.png","text_4.png","text_5.png","text_6.png","text_7.png","text_8.png","text_9.png"]

shot = pygame.image.load("Assets-shooter/Objects/shot_yellow_large.png")
shot = pygame.transform.scale(shot, (10,20))

ammo = pygame.image.load("Assets-shooter/HUD/icon_bullet_gold_long.png")
ammogone = pygame.image.load("Assets-shooter/HUD/icon_bullet_empty_long.png")
ammo = pygame.transform.scale(ammo, (10, 22))
ammogone = pygame.transform.scale(ammogone, (10, 22))
scoreimg = pygame.image.load("Assets-shooter/HUD/text_score_small.png")
scoreimg = pygame.transform.scale(scoreimg, (70, 32))
gameover = pygame.image.load("Assets-shooter/HUD/text_gameover.png")

while running:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False

       if event.type == pygame.KEYDOWN:
           if bulletsleft > 0:
               if event.key == pygame.K_SPACE and bullets > 0:
                   bullet_rect = shot.get_rect()
                   bullet_rect.midbottom = riflerect.midtop
                   bullet.append(bullet_rect)
                   bulletsleft -= 1

   targetrect.x = targetrect.x + targetspeed
   screen.fill(background_color)

   targetrect.x = targetrect.x + targetspeed
   screen.fill(background_color)

   targetrect2.x = targetrect2.x - targetspeed2
   screen.fill(background_color)

   screen.blit(bgimg, (0,0))

   x = 0

   if targetrect.right > screen_width or targetrect.left <= 0:
       targetspeed *= -1

   if targetrect2.right > screen_width or targetrect2.left <= 0:
       targetspeed2 *= -1

   for i in range(7):
       screen.blit(grass, (x, 400))
       screen.blit(water, (x, 450))
       screen.blit(water2, (x, 500))
       x = x+132

   for i in bullet[:]:
       i.y -= bulletspeed
       if i.bottom < 0:
           bullet.remove(i)
       elif i.colliderect(targetrect):
           bullet.remove(i)
           print ("Hit")
           points += 3
           bulletsleft += 1
       elif i.colliderect(targetrect2):
           bullet.remove(i)
           print ("Hit")
           points += 1

   screen.blit(curtain, (0,0))
   screen.blit(curtain2, (725, 0))
   screen.blit(topcurtain, (0, 0))
   #screen.blit(rifle, (400, 520))
   screen.blit(whiteduck, targetrect2)
   screen.blit(duck, targetrect)
   screen.blit(rifle, riflerect)
   #print(bullet)
   for i in bullet:
       screen.blit(shot, i)

   positions = [(640,60),(650,60), (660,60)]
   for j in range(bullets):
       x,y = positions[j]

       if j < bulletsleft:
            screen.blit(ammo, (x,y))
       else:
           screen.blit(ammogone, (x,y))


   copy_points = points
   copy_points = str(copy_points)

   list_num = []  # empty list

   for i in copy_points:
       val = int(i)
       list_num.append(val)

   #print(list_num)
   num = 120

   for j in list_num:
       path = f"Assets-shooter/HUD/{scoreimglist[j]}"
       img = pygame.image.load(path)
       img = pygame.transform.scale(img, (30,32))
       screen.blit(img, (num,50))
       num = num + 24

   textscore = font.render(f" : {points}" , True, "white")
   screen.blit(scoreimg, (50,50))
   if bulletsleft == 0:
       screen.blit(gameover, (200,300))
       pygame.display.update()
       pygame.time.wait(3000)
       pygame.quit()
       sys.exit()
   #screen.blit(textscore, (120,50))




   pygame.display.flip()