# The goals for this phase include:
# - Pick out some icons for your game
# - Establish a starting position for each icon
# - Pick a size for your playing space
# - Print your playing space with starting position of each icon

# To make this work, you may have to type this into the terminal --> pip install curses
import curses
import random
import time

game_data = {
    'width': 11,
    'height': 11,
    'player': {"x": 1, "y": 1, "score": 0},
    'ghost_pos': {"x": 5, "y": 5},
    'ghost2_pos': {"x": 5, "y": 5},
    'collectibles': [
        {"x": 2, "y": 1, "collected": False},
        {"x": 3, "y": 1, "collected": False},
        {"x": 4, "y": 1, "collected": False},
        {"x": 5, "y": 1, "collected": False},
        {"x": 6, "y": 1, "collected": False},
        {"x": 7, "y": 1, "collected": False},
        {"x": 8, "y": 1, "collected": False},
        {"x": 9, "y": 1, "collected": False},
        {"x": 1, "y": 2, "collected": False},
        {"x": 4, "y": 2, "collected": False},
        {"x": 6, "y": 2, "collected": False},
        {"x": 9, "y": 2, "collected": False},
        {"x": 1, "y": 3, "collected": False},
        {"x": 4, "y": 3, "collected": False},
        {"x": 6, "y": 3, "collected": False},
        {"x": 9, "y": 3, "collected": False},
        {"x": 3, "y": 3, "collected": False},
        {"x": 7, "y": 3, "collected": False},
        {"x": 3, "y": 4, "collected": False},
        {"x": 7, "y": 4, "collected": False},
        {"x": 1, "y": 4, "collected": False},
        {"x": 4, "y": 4, "collected": False},
        {"x": 6, "y": 4, "collected": False},
        {"x": 9, "y": 4, "collected": False},
        {"x": 5, "y": 4, "collected": False},
        {"x": 9, "y": 5, "collected": False},
        {"x": 8, "y": 5, "collected": False},
        {"x": 7, "y": 5, "collected": False},
        {"x": 3, "y": 5, "collected": False},
        {"x": 2, "y": 5, "collected": False},
        {"x": 1, "y": 5, "collected": False},
        {"x": 9, "y": 6, "collected": False},
        {"x": 7, "y": 6, "collected": False},
        {"x": 6, "y": 6, "collected": False},
        {"x": 4, "y": 6, "collected": False},
        {"x": 3, "y": 6, "collected": False},
        {"x": 1, "y": 6, "collected": False},
        {"x": 9, "y": 7, "collected": False},
        {"x": 6, "y": 7, "collected": False},
        {"x": 5, "y": 7, "collected": False},
        {"x": 4, "y": 7, "collected": False},
        {"x": 1, "y": 7, "collected": False},
        {"x": 9, "y": 8, "collected": False},
        {"x": 8, "y": 8, "collected": False},
        {"x": 6, "y": 8, "collected": False},
        {"x": 4, "y": 8, "collected": False},
        {"x": 2, "y": 8, "collected": False},
        {"x": 1, "y": 8, "collected": False},
        {"x": 8, "y": 9, "collected": False},
        {"x": 7, "y": 9, "collected": False},
        {"x": 6, "y": 9, "collected": False},
        {"x": 5, "y": 9, "collected": False},
        {"x": 4, "y": 9, "collected": False},
        {"x": 3, "y": 9, "collected": False},
        {"x": 2, "y": 9, "collected": False},
    ],
    'obstacles': [
        {"x": 0, "y": 0},
        {"x": 0, "y": 1},
        {"x": 0, "y": 2},
        {"x": 0, "y": 3},
        {"x": 0, "y": 4},
        {"x": 0, "y": 5},
        {"x": 0, "y": 6},
        {"x": 0, "y": 7},
        {"x": 0, "y": 8},
        {"x": 0, "y": 9},
        {"x": 0, "y": 10},
        {"x": 1, "y": 0},
        {"x": 2, "y": 0},
        {"x": 3, "y": 0},
        {"x": 4, "y": 0},
        {"x": 5, "y": 0},
        {"x": 6, "y": 0},
        {"x": 7, "y": 0},
        {"x": 8, "y": 0},
        {"x": 9, "y": 0},
        {"x": 10, "y": 0},
        {"x": 10, "y": 1},
        {"x": 10, "y": 2},
        {"x": 10, "y": 3},
        {"x": 10, "y": 4},
        {"x": 10, "y": 5},
        {"x": 10, "y": 6},
        {"x": 10, "y": 7},
        {"x": 10, "y": 8},
        {"x": 10, "y": 9},
        {"x": 10, "y": 10},
        {"x": 0, "y": 10},
        {"x": 1, "y": 10},
        {"x": 2, "y": 10},
        {"x": 3, "y": 10},
        {"x": 4, "y": 10},
        {"x": 5, "y": 10},
        {"x": 6, "y": 10},
        {"x": 7, "y": 10},
        {"x": 8, "y": 10},
        {"x": 9, "y": 10},
        {"x": 10, "y": 10},
        {"x": 4, "y": 5},
        {"x": 6, "y": 5},
        {"x": 5, "y": 6},
        {"x": 2, "y": 2},
        {"x": 3, "y": 2},
        {"x": 2, "y": 3},
        {"x": 2, "y": 4},
        {"x": 5, "y": 2},
        {"x": 5, "y": 3},
        {"x": 8, "y": 2},
        {"x": 7, "y": 2},
        {"x": 8, "y": 3},
        {"x": 8, "y": 4},
        {"x": 2, "y": 6},
        {"x": 2, "y": 7},
        {"x": 3, "y": 7},
        {"x": 3, "y": 8},
        {"x": 1, "y": 9},
        {"x": 5, "y": 8},
        {"x": 9, "y": 9},
        {"x": 7, "y": 8},
        {"x": 7, "y": 8},
        {"x": 7, "y": 7},
        {"x": 8, "y": 7},
        {"x": 8, "y": 6},
        #make the ghosts start here {"x": 5, "y": 5},
        # The board starts from 0, not 1, as computers do.

        
    ],

    # ASCII icons
    ###Pac man code below
    'pac_man': "\U0001F432",
    'ghost': "\U0001F47B",
    'apple': "\U0001F34E",
    'obstacle': "\U00002B1C",
    'empty': "  "
}

def display_welcome_screen():
    print(" ")
    print("Welcome to Pac man!")
    print(" ")
    print("Use WSAD for movement")
    print("Avoid running into the walls / obstacles!")
    print("Don't touch the ghosts and collect all the apples")
    print("Size up the terminal")
    
def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)

    draw_board(stdscr)

    while True:
        try:
            key = stdscr.getkey()
        except:
            key = None

        if key:
            if key.lower() == "q":
                break
            move_player(key)
        #these allow the collectibles to be collected and for the ghosts to move
        check_collectibles()
        move_ghost()
        move_ghost2()

        # These check the win/loss condtions are met
        if game_data['player']["score"] >= 55: #changed the <= to >= and the 0 to 20
            break

        if (game_data['player']["x"] == game_data['ghost_pos']["x"] and
            game_data['player']["y"] == game_data['ghost_pos']["y"]):
            break
        
        if (game_data['player']["x"] == game_data['ghost2_pos']["x"] and
            game_data['player']["y"] == game_data['ghost2_pos']["y"]):
            break

        draw_board(stdscr)
        time.sleep(0.3)
        
        #What these output will change based on if you won or lost
    stdscr.clear()
    if game_data['player']['score'] >= 55:
        stdscr.addstr(2, 2, "You won")
    else:
        stdscr.addstr(2, 2, "GAME OVER")
    stdscr.addstr(3, 2, f"Apples collected: {game_data['player']['score']}/55")
    stdscr.refresh()
    time.sleep(3)

def draw_board(stdscr):
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, -1)

    stdscr.clear()
    for y in range(game_data['height']):
        row = ""
        for x in range(game_data['width']):
            # Player
            if x == game_data['player']['x'] and y == game_data['player']['y']:
                row += game_data['pac_man']
            # # ghosts
            elif x == game_data['ghost_pos']['x'] and y == game_data['ghost_pos']['y']:
                 row += game_data['ghost']

            elif x == game_data['ghost2_pos']['x'] and y == game_data['ghost2_pos']['y']:
                 row += game_data['ghost']
             # walls
            elif any(o['x'] == x and o['y'] == y for o in game_data['obstacles']):
                 row += game_data['obstacle']
            # Collectibles/ Food
            elif any(c['x'] == x and c['y'] == y and not c['collected'] for c in game_data['collectibles']):
                row += game_data['apple']
            else:
                row += game_data['empty']
        stdscr.addstr(y, 0, row, curses.color_pair(1))
    
    stdscr.addstr(game_data['height'] + 1, 0, f"Apples Collected: {game_data['player']['score']}/55")

def move_ghost():
    directions = [
        (0, -1),  # up
        (0, 1),   # down
        (-1, 0),  # left
        (1, 0)    # right
    ]

    random.shuffle(directions)

    ex = game_data['ghost_pos']["x"]
    ey = game_data['ghost_pos']["y"]

    valid_moves = []

    for dx, dy in directions:
        new_x = ex + dx
        new_y = ey + dy

        # Inside board?
        if not (0 <= new_x < game_data['width'] and
                0 <= new_y < game_data['height']):
            continue

        # wall collision?
        if any(o["x"] == new_x and o["y"] == new_y
               for o in game_data['obstacles']):
            continue

        valid_moves.append((new_x, new_y))

    # If there are valid moves, pick one
    if valid_moves:
        new_x, new_y = random.choice(valid_moves)
        game_data['ghost_pos']["x"] = new_x
        game_data['ghost_pos']["y"] = new_y

def move_ghost2():
    directions = [
        (0, -1),  # up
        (0, 1),   # down
        (-1, 0),  # left
        (1, 0)    # right
    ]

    random.shuffle(directions)

    ex = game_data['ghost2_pos']["x"]
    ey = game_data['ghost2_pos']["y"]

    valid_moves = []

    for dx, dy in directions:
        new_x = ex + dx
        new_y = ey + dy

        # Inside board?
        if not (0 <= new_x < game_data['width'] and
                0 <= new_y < game_data['height']):
            continue

        # wall collision?
        if any(o["x"] == new_x and o["y"] == new_y
               for o in game_data['obstacles']):
            continue

        valid_moves.append((new_x, new_y))

    # If there are valid moves, pick one
    if valid_moves:
        new_x, new_y = random.choice(valid_moves)
        game_data['ghost2_pos']["x"] = new_x
        game_data['ghost2_pos']["y"] = new_y

def check_collectibles():
    for c in game_data['collectibles']:
        if (not c["collected"] and game_data['player']["x"] == c["x"] and game_data['player']["y"] == c["y"]):

            c["collected"] = True
            
            game_data['player']["score"] = ( 
                game_data['player']["score"] + 1
            )

def move_player(key):
    key = key.lower()
    px = game_data['player']["x"]
    py = game_data['player']["y"]

    new_x, new_y = px, py

    if key == "w" and py > 0:
        new_y -= 1
    elif key == "s" and py < game_data['height'] - 1:
        new_y += 1
    elif key == "a" and px > 0:
        new_x -= 1
    elif key == "d" and px < game_data['width'] - 1:
        new_x += 1
    else:
        return False

    # Check obstacle collision
    if any(o["x"] == new_x and o["y"] == new_y for o in game_data['obstacles']):
        return False

    game_data['player']["x"] = new_x
    game_data['player']["y"] = new_y


    return True

display_welcome_screen()
time.sleep(3)
curses.wrapper(main)


