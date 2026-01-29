# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 700))
clock = pygame.time.Clock()
running = True

pygame.font.init()
my_font = pygame.font.SysFont(None, 350)
small_font = pygame.font.SysFont(None, 50)
exit_btn_color='black'
reset_btn_color='black'

class Player:

    sign=None
    initial_sign=None

    def choose_sign(self, choice):
        self.sign = choice

    def alternate(self, is_valid_x, is_valid_o, turn):
        if self.sign=="x" and (not is_valid_o):
            self.sign='o'
        elif self.sign=="o" and (not is_valid_x):
            self.sign='x'

    def get_winner(self, cells):
        for comb in combinations:
            if cells[comb[0]]['x_checked'] and cells[comb[1]]['x_checked'] and cells[comb[2]]['x_checked']:
                text_surface=small_font.render('X WON', False, 'red')
                screen.blit(text_surface, (300, 300))
                return True
            elif cells[comb[0]]['o_checked'] and cells[comb[1]]['o_checked'] and cells[comb[2]]['o_checked']:
                text_surface=small_font.render('O WON', False, 'red')
                screen.blit(text_surface, (300, 300))
                return True
            
        return False

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
clicks = 0
while running:
    # print(cells)
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if 0<pygame.mouse.get_pos()[0]<200 and 600<pygame.mouse.get_pos()[1]<700:
            exit_btn_color='white'
        else:
            exit_btn_color='black'

        if 450<pygame.mouse.get_pos()[0]<650 and 600<pygame.mouse.get_pos()[1]<700:
            reset_btn_color='white'
        else:
            reset_btn_color='black'

        if event.type == pygame.MOUSEBUTTONDOWN and not paused:
            clicks += 1
            print(clicks)
            mouse=pygame.mouse.get_pos()
            print(mouse)
            if player.sign != None:
                turn += 1
            

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    if player.sign == None:
        pygame.draw.rect(screen, 'black', (100, 200, 150, 150))
        x= small_font.render('O', False, 'white')
        screen.blit(x, (150, 250))
        pygame.draw.rect(screen, 'black', (300, 200, 150, 150))
        o= small_font.render('X', False, 'white')
        screen.blit(o, (350, 250))


        if 100<mouse[0]<250  and 200<mouse[1]<350:
            player.choose_sign('x')
            player.initial_sign="x"
            print('mouse: ', mouse)
            mouse=(0, 0)

        elif 300<mouse[0]<450 and 200<mouse[1]<350:
            player.choose_sign('o')
            player.initial_sign="o"
            
            print('mouse: ', mouse)
            mouse=(0, 0)


    
    else:
        
        # RENDER YOUR GAME HERE
        for cell in cells:
            pygame.draw.rect(screen, 'white', (cell['start_pos'][0], cell['start_pos'][1], 190, 190))
            if cell['start_pos'][0]<mouse[0]<cell['end_pos'][0] and cell['start_pos'][1]<mouse[1]<cell['end_pos'][1]:
                print("drawing launched")
                print(cell)
                player.alternate(cell['x_checked'], cell['o_checked'], turn)
                if (player.sign=="x" and not cell['o_checked']) or (player.sign=="o" and not cell['x_checked']):
                    cell[player.draw()]=True 
                print(cell)
                mouse=(0,0)

            
            if cell['x_checked']:
                text_surface = my_font.render('X', False, 'black')
                screen.blit(text_surface, (cell['start_pos'][0]+10, cell['start_pos'][1]))
            if cell['o_checked']:
                text_surface = my_font.render('O', False, 'black')
                screen.blit(text_surface, (cell['start_pos'][0]+10, cell['start_pos'][1]))


    
        paused = player.get_winner(cells)
        reset = small_font.render('Reset', False, reset_btn_color)
        screen.blit(reset, (500, 650))
        if 500<mouse[0]<600 and 600<mouse[1]<700 :
            for cell in cells:
                cell['x_checked']=False
                cell['o_checked']=False
                player.sign=player.initial_sign

        reset = small_font.render('Exit', False, exit_btn_color)
        screen.blit(reset, (20, 650))
        if 0<mouse[0]<200 and 600<mouse[1]<700 :
            running=False
        # for comb in combinations:
        #     if cells[comb[0]]['x_checked'] and cells[comb[1]]['x_checked'] and cells[comb[2]]['x_checked']:
        #         text_surface=small_font.render('X WON', False, 'red')
        #         screen.blit(text_surface, (300, 300))
        #         paused=True
        #     elif cells[comb[0]]['o_checked'] and cells[comb[1]]['o_checked'] and cells[comb[2]]['o_checked']:
        #         text_surface=small_font.render('O WON', False, 'red')
        #         screen.blit(text_surface, (300, 300))
        #         paused=True

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()