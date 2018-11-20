import pygame, sys
import random
from pygame.locals import *
from settings import settings
#Game Display
display_width = 600
display_height = 600

#Background Image
bg = pygame.image.load("snake.jpg")
bg = pygame.transform.scale(bg, (display_height, display_width))

#import settings
settings = settings()

#initializign the game
pygame.init()
#background music
crash_sound = pygame.mixer.Sound("crash.wav")
pygame.mixer.music.load("jazz.wav")
bite_sound = pygame.mixer.Sound("bite.wav")

#Display Settings
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

font = pygame.font.SysFont('Arial', 20)

#Color
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
bg_green = (172, 221, 57)

#Apple Position
appleimage = pygame.Surface((10, 10))
appleimage.fill((255, 0, 0))

#snake color info
probably=random.randint(0,255)
probably1=random.randint(0,255)
probably2=random.randint(0,255)
img = pygame.Surface((20, 20))
img.fill((probably, probably1, probably2))

#Game Display
xs = [290, 290, 290, 290, 290]
ys = [290, 270, 250, 230, 210]

pause = True


def end_game():
	intro = True

	while intro:
		for event in pygame.event.get():
			print(event)
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		gameDisplay.blit(bg, [0,0])
		largeText = pygame.font.Font('freesansbold.ttf', 115)
		TextSurf, TextRect = text_objects("Snakey", largeText)
		TextRect.center = ((display_width / 2), (display_height / 2))
		gameDisplay.blit(TextSurf, TextRect)
		del xs[5::]
		del ys[5::]
		xs[0]=xs[1]=xs[2]=xs[3]=xs[4]=290
		ys[0]= 290
		ys[1]= 270
		ys[2]= 250
		ys[3]= 230
		ys[4]= 210
		button("Play Again", 100, 450, 150, 50, settings.bright_green, settings.green, game_intro2)
		button("Quit", 400, 450, 100, 50, settings.bright_red, settings.red, quitgame)

		pygame.display.update()





def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def collide(x1, x2, y1, y2, w1, w2, h1, h2):
	if x1+w1>x2 and x1<x2+w2 and y1+h1>y2 and y1<y2+h2:
		return True
	else:
		return False

def die(screen, score):
	pygame.mixer.music.stop()
	pygame.mixer.Sound.play(crash_sound)
	font=pygame.font.SysFont('Arial', 30)
	t=font.render('Your score was: '+str(score), True, (0, 0, 0))
	screen.blit(t, (10, 270))
	pygame.display.update()
	pygame.time.wait(2000)
	end_game()

def button(msg,x,y,w,h,ac,ic,action = None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	smallText = pygame.font.Font("freesansbold.ttf", 20)

	if x + w > mouse[0] > x and y + h > mouse[1] > y:
		pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
		if click[0] == 1 and action != None:
			action()

#			if action == "play":
#				game_loop()
#			elif action == "quit":
#				pygame.quit()
#				quit()

	else:
		pygame.draw.rect(gameDisplay, ic, (x,y,w,h))

	textSurf, textRect = text_objects(msg, smallText)
	textRect.center = ((x + (w / 2)), (y + (h / 2)))
	gameDisplay.blit(textSurf, textRect)

def unpause():
	global pause
	pause = False



def paused():


	while pause:
		for event in pygame.event.get():
			print(event)
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		gameDisplay.blit(bg, [0,0])
		largeText = pygame.font.Font('freesansbold.ttf', 115)
		TextSurf, TextRect = text_objects("Paused", largeText)
		TextRect.center = ((display_width / 2), (display_height / 2))
		gameDisplay.blit(TextSurf, TextRect)


		button("Resume", 100, 450, 100, 50, bright_green, green,unpause)
		button("Quit", 400, 450, 100, 50, bright_red, red,quitgame)


		pygame.display.update()



def game_intro():
	print ('!')
	intro = True

	while intro:
		for event in pygame.event.get():
			print(event)
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		gameDisplay.blit(bg, [0,0])
		largeText = pygame.font.Font('freesansbold.ttf', 115)
		TextSurf, TextRect = text_objects("Snakey", largeText)
		TextRect.center = ((display_width / 2), 200)
		gameDisplay.blit(TextSurf, TextRect)


		button("Play", 100, 450, 100, 50, settings.bright_green, settings.green,game_intro2)
		button("Quit", 400, 450, 100, 50, settings.bright_red, settings.red,quitgame)


		pygame.display.update()


def game_intro2():
	print ("@")
	intro = True

	while intro:
		for event in pygame.event.get():
			print(event)
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		gameDisplay.blit(bg, [0,0])
		largeText = pygame.font.Font('freesansbold.ttf', 115)
		TextSurf, TextRect = text_objects("levels", largeText)
		TextRect.center = ((display_width / 2), (display_height / 2))
		gameDisplay.blit(TextSurf, TextRect)

		button("Easy", 50, 400, 100, 50, bright_green, green,game_loop)
		button("Normal", 200, 400, 100, 50, bright_green, green,game_loop2)
		button("Hard", 350,400,100,50,bright_green,green,game_loop3)

		pygame.display.update()

def quitgame():
	pygame.quit()
	quit()


def game_loop():

	global pause
	settings.music()
	applepos = (random.randint(0, 590), random.randint(0, 590))
	dirs = 0
	score = 0

	while True:
		clock.tick(10)
		for event in pygame.event.get():

			if event.type == QUIT:
				sys.exit(0)
			elif event.type == KEYDOWN:
				if event.key == K_UP and dirs != 0:
					dirs = 2
				elif event.key == K_DOWN and dirs != 2:
					dirs = 0
				elif event.key == K_LEFT and dirs != 1:
					dirs = 3
				elif event.key == K_RIGHT and dirs != 3:
					dirs = 1
				elif event.key == pygame.K_p:
					pause = True
					paused()

		i = len(xs)-1
		while i >= 2:
			if collide(xs[0], xs[i], ys[0], ys[i], 20, 20, 20, 20):
				die(gameDisplay, score)
			i-= 1
		if collide(xs[0], applepos[0], ys[0], applepos[1], 20, 10, 20, 10):
			settings.eat_sound()
			score+=1
			xs.append(700)
			ys.append(700)
			applepos=(random.randint(0,590),random.randint(0,590))
		if xs[0] < 0 or xs[0] > 580 or ys[0] < 0 or ys[0] > 580:
			die(gameDisplay, score)
		i = len(xs)-1
		while i >= 1:
			xs[i] = xs[i-1]
			ys[i] = ys[i-1]
			i -= 1
		if dirs==0:
			ys[0] += 20
		elif dirs==1:
			xs[0] += 20
		elif dirs==2:
			ys[0] -= 20
		elif dirs==3:
			xs[0] -= 20
		gameDisplay.fill(bg_green)

		for i in range(0, len(xs)):


			gameDisplay.blit(img, (xs[i], ys[i]))
		gameDisplay.blit(appleimage, applepos)
		t=font.render(str(score), True, (0, 0, 0))
		gameDisplay.blit(t, (10, 10))


		pygame.display.update()


def game_loop2():
	global pause
	pygame.mixer.music.play(-1)
	applepos = (random.randint(0, 590), random.randint(0, 590))
	dirs = 0
	score = 0
	while True:
		clock.tick(20)
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit(0)
			elif event.type == KEYDOWN:
				if event.key == K_UP and dirs != 0:
					dirs = 2
				elif event.key == K_DOWN and dirs != 2:
					dirs = 0
				elif event.key == K_LEFT and dirs != 1:
					dirs = 3
				elif event.key == K_RIGHT and dirs != 3:
					dirs = 1
				elif event.key == pygame.K_p:
					pause = True
					paused()

		i = len(xs)-1
		while i >= 2:
			if collide(xs[0], xs[i], ys[0], ys[i], 20, 20, 20, 20):
				die(gameDisplay, score)
			i-= 1
		if collide(xs[0], applepos[0], ys[0], applepos[1], 20, 10, 20, 10):
			pygame.mixer.Sound.play(bite_sound)
			score+=1
			xs.append(700)
			ys.append(700)
			applepos=(random.randint(0,590),random.randint(0,590))
		if xs[0] < 0 or xs[0] > 580 or ys[0] < 0 or ys[0] > 580:
			die(gameDisplay, score)
		i = len(xs)-1
		while i >= 1:
			xs[i] = xs[i-1]
			ys[i] = ys[i-1]
			i -= 1
		if dirs==0:
			ys[0] += 20
		elif dirs==1:
			xs[0] += 20
		elif dirs==2:
			ys[0] -= 20
		elif dirs==3:
			xs[0] -= 20
		gameDisplay.fill(bg_green)
		for i in range(0, len(xs)):
			gameDisplay.blit(img, (xs[i], ys[i]))
		gameDisplay.blit(appleimage, applepos)
		t=font.render(str(score), True, (0, 0, 0))
		gameDisplay.blit(t, (10, 10))
		pygame.display.update()

def game_loop3():
	global pause
	pygame.mixer.music.play(-1)
	applepos = (random.randint(0, 590), random.randint(0, 590))
	dirs = 0
	score = 0
	while True:
		clock.tick(30)
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit(0)
			elif event.type == KEYDOWN:
				if event.key == K_UP and dirs != 0:
					dirs = 2
				elif event.key == K_DOWN and dirs != 2:
					dirs = 0
				elif event.key == K_LEFT and dirs != 1:
					dirs = 3
				elif event.key == K_RIGHT and dirs != 3:
					dirs = 1
				elif event.key == pygame.K_p:
					pause = True
					paused()
		i = len(xs) - 1
		while i >= 2:
			if collide(xs[0], xs[i], ys[0], ys[i], 20, 20, 20, 20):
				die(gameDisplay, score)
			i -= 1
		if collide(xs[0], applepos[0], ys[0], applepos[1], 20, 10, 20, 10):
			pygame.mixer.Sound.play(bite_sound)
			score += 1
			xs.append(700)
			ys.append(700)
			applepos = (random.randint(0, 590), random.randint(0, 590))
		if xs[0] < 0 or xs[0] > 580 or ys[0] < 0 or ys[0] > 580:
			die(gameDisplay, score)
		i = len(xs) - 1
		while i >= 1:
			xs[i] = xs[i - 1]
			ys[i] = ys[i - 1]
			i -= 1
		if dirs == 0:
			ys[0] += 20
		elif dirs == 1:
			xs[0] += 20
		elif dirs == 2:
			ys[0] -= 20
		elif dirs == 3:
			xs[0] -= 20
		gameDisplay.fill(bg_green)
		for i in range(0, len(xs)):
			gameDisplay.blit(img, (xs[i], ys[i]))
		gameDisplay.blit(appleimage, applepos)
		t = font.render(str(score), True, (0, 0, 0))
		gameDisplay.blit(t, (10, 10))

		pygame.display.update()


game_intro()



