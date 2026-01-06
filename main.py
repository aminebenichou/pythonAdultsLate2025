table=[1, 2, 3, 4, 5, 6, 7, 8, 9]
def draw_table():
    print(f'{table[0]} | {table[1]} | {table[2]} ')
    print('__|___|__')
    print(f'{table[3]} | {table[4]} | {table[5]} ')
    print('__|___|__')
    print(f'{table[6]} | {table[7]} | {table[8]} ')
    print('  |   |  ')

def get_winner(limit, incr, step):
    j=0
    while j<limit:
        if table[j]==table[j+incr]==table[j+incr*2]:
            print("You win")
            return True
        j += step
    return False

player="x"
running=True
while running:
    draw_table()
    player_input=input("Enter a  number (1-9): ")
    i=0
    while i<len(table):
        if table[i]==int(player_input):
            table[i]=player
        i += 1

    if player=="x":
        player="O"
    else:
        player="x"
    

    
    if get_winner(7, 1, 3):
        running=False
    elif get_winner(3, 3, 1):
        running=False
   

    if table[0]==table[4]==table[8] or table[2]==table[4]==table[6]:
        print("You win")
        running=False
