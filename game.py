import sys
# initalising pygame in to the app
pygame.init()
black = 0,0,0

print(black)
size = width, height = 500, 340
# generating a tuple of (width, height) for the window
speed = [2, 2]
red = 256, 0, 0
# game window name
pygame.display.set_caption(' Yemi\'s game ')
# displaying the screen
screen = pygame.display.set_mode(size)

# getting the file from a directory
imp = pygame.image.load("C:\\Users\\OTI\Downloads\\ball-removebg-preview.png").convert()


imp = pygame.transform.scale(imp, (50, 50))
screen.blit(imp, (0, 0))
# can you see the window i made ? with the ball? no not yet , so??? check twitter
# run it in the terminal, with py game.py, share the terminal (its shared)
# no need for python3
# defining the dimensions for the window

ball_rect = imp.get_rect()

pygame.display.flip()
status = True


while (status):

  # iterate over the l
  # ist of Event objects
  # that was returned by pygame.event.get() method.
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False

    ball_rect = ball_rect.move(speed)
    if ball_rect.left < 0 or ball_rect.right > width:
        speed[0] = -speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > height:
        speed[1] = -speed[1]


    screen.fill(black)
    screen.blit(imp, ball_rect)

# deactivates the pygame library
pygame.quit()

