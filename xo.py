# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True

pygame.font.init()
my_font = pygame.font.SysFont(None, 350)
small_font = pygame.font.SysFont(None, 50)

class Player:

    sign="x"
    def alternate(self, is_valid_x, is_valid_o, turn):
        if turn%2==0 and not is_valid_o:
                self.sign="x"
                cell['x_checked']=True 
        elif turn%2!=0 and not is_valid_x:
                self.sign="o"
                cell['o_checked']=True


    def draw(self):
        return f"{self.sign}_checked"

cells=[
    {'start_pos':(0,0), 'end_pos': (190, 190), 'x_checked':False, 'o_checked': False},
    {'start_pos':(200, 0), 'end_pos': (390, 190), 'x_checked':False, 'o_checked': False},
    {'start_pos':(400, 0), 'end_pos': (600, 190), 'x_checked':False, 'o_checked': False},
   
    {'start_pos':(0,200), 'end_pos': (190, 400), 'x_checked':False, 'o_checked': False},
    {'start_pos':(200, 200), 'end_pos': (390, 400), 'x_checked':False, 'o_checked': False},
    {'start_pos':(400, 200), 'end_pos': (600, 400), 'x_checked':False, 'o_checked': False},
   
    {'start_pos':(0,400), 'end_pos': (190, 600), 'x_checked':False, 'o_checked': False},
    {'start_pos':(200, 400), 'end_pos': (390, 600), 'x_checked':False, 'o_checked': False},
    {'start_pos':(400, 400), 'end_pos': (600, 600), 'x_checked':False, 'o_checked': False},
   
]
combinations=[
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]
mouse=(0,0)
turn = 0
paused = False
player=Player()
while running:
    # print(cells)
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not paused:
            mouse=pygame.mouse.get_pos()
            print(mouse)
            turn += 1
            

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    for cell in cells:
        pygame.draw.rect(screen, 'white', (cell['start_pos'][0], cell['start_pos'][1], 190, 190))
        if cell['start_pos'][0]<mouse[0]<cell['end_pos'][0] and cell['start_pos'][1]<mouse[1]<cell['end_pos'][1]:
            player.alternate(cell['x_checked'], cell['o_checked'], turn)
            cell[player.draw()]=True
            

        
        if cell['x_checked']:
            text_surface = my_font.render('X', False, 'black')
            screen.blit(text_surface, (cell['start_pos'][0]+10, cell['start_pos'][1]))
        if cell['o_checked']:
            text_surface = my_font.render('O', False, 'black')
            screen.blit(text_surface, (cell['start_pos'][0]+10, cell['start_pos'][1]))

    for comb in combinations:
        if cells[comb[0]]['x_checked'] and cells[comb[1]]['x_checked'] and cells[comb[2]]['x_checked']:
            text_surface=small_font.render('X WON', False, 'red')
            screen.blit(text_surface, (300, 300))
            paused=True
        elif cells[comb[0]]['o_checked'] and cells[comb[1]]['o_checked'] and cells[comb[2]]['o_checked']:
            text_surface=small_font.render('O WON', False, 'red')
            screen.blit(text_surface, (300, 300))
            paused=True

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()