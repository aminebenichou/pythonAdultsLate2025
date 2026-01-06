# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True

pygame.font.init()
my_font = pygame.font.SysFont(None, 350)

cells=[
    {'start_pos':(0,0), 'end_pos': (190, 190), 'x_checked':False, 'o_checked': False},
    {'start_pos':(200, 0), 'end_pos': (390, 190), 'x_checked':False, 'o_checked': False},
    {'start_pos':(400, 0), 'end_pos': (600, 190), 'x_checked':False, 'o_checked': False},
   
    {'start_pos':(0,200), 'end_pos': (190, 200), 'x_checked':False, 'o_checked': False},
    {'start_pos':(200, 200), 'end_pos': (390, 200), 'x_checked':False, 'o_checked': False},
    {'start_pos':(400, 200), 'end_pos': (600, 200), 'x_checked':False, 'o_checked': False},
   
    {'start_pos':(0,400), 'end_pos': (190, 600), 'x_checked':False, 'o_checked': False},
    {'start_pos':(200, 400), 'end_pos': (390, 600), 'x_checked':False, 'o_checked': False},
    {'start_pos':(400, 400), 'end_pos': (600, 600), 'x_checked':False, 'o_checked': False},
   
]
mouse=(0,0)
turn = 0
while running:
    print(cells)
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse=pygame.mouse.get_pos()
            turn += 1
            

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    for cell in cells:
        pygame.draw.rect(screen, 'white', (cell['start_pos'][0], cell['start_pos'][1], 190, 190))
        if cell['start_pos'][0]<mouse[0]<cell['end_pos'][0] and cell['start_pos'][1]<mouse[1]<cell['end_pos'][1]:
            if turn%2==0:
                cell['x_checked']=True 
            else:
                cell['o_checked']=True
        
        if cell['x_checked']:
            text_surface = my_font.render('X', False, 'black')
            screen.blit(text_surface, (cell['start_pos'][0]+10, cell['start_pos'][1]))
        if cell['o_checked']:
            text_surface = my_font.render('O', False, 'black')
            screen.blit(text_surface, (cell['start_pos'][0]+10, cell['start_pos'][1]))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()