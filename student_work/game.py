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
    'player': {"x": 1, "y": 1, "score": 0, "energy": 10, "max_energy": 10},
    'eagle_pos': {"x": 4, "y": 4},
    'collectibles': [
        {"x": 2, "y": 1, "collected": False},
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
        #make the ghosts start here {"x": 5, "y": 5},
        # The board starts from 0, not 1, as computers do.

        
    ],

    # ASCII icons
    ###Pac man code below
    'snake_head': "\U0001F432",
    'snake_body': "\U0001274E",
    'apple': "\U0001F34E",
    'obstacle': "\U00002B1C",
    ######Jackson code below
    # 'turtle': "\U0001F422",
    # 'eagle_icon': "\U0001F985",
    # 'obstacle': "\U0001FAA8",
    # 'leaf': "\U0001F343",
    'empty': "  "
}

def display_welcome_screen():
    print(" ")
    print("Welcome to Pac man!")
    print(" ")
    print("Use WSAD for movement")
    print("Avoid running into the walls / obstacles!")
    print("Don't touch the ghosts and collect all the apples")
    
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

            draw_board(stdscr)
            time.sleep(0.2)

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
                row += game_data['snake_head']
            # # Eagle
            # elif x == game_data['eagle_pos']['x'] and y == game_data['eagle_pos']['y']:
            #     row += game_data['eagle_icon']
             # Obstacles
            elif any(o['x'] == x and o['y'] == y for o in game_data['obstacles']):
                 row += game_data['obstacle']
            # Collectibles/ Food
            elif any(c['x'] == x and c['y'] == y and not c['collected'] for c in game_data['collectibles']):
                row += game_data['apple']
            else:
                row += game_data['empty']
        stdscr.addstr(y, 0, row, curses.color_pair(1))

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

    # Energy decreases per move
    #game_data['player']["energy"] -= 1

    # Score increases per move survived
    #game_data['player']["score"] += 1

    return True

display_welcome_screen()
time.sleep(3)
curses.wrapper(main)
#curses.wrapper(draw_board(stdscr))

