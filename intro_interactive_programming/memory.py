''' implementation of card game - Memory '''

import simplegui
import random


#globals
CANVAS_SIZE = [600, 300] # canvas dimentions
NUM_OF_CARDS = 16        # specifies card number
CARD_SIZE = [50, 100]    # cards are logically 50x100 pixels in size
DECK = []                # stores card values
EXPOSED = [0, 0]         # boolean list of turned/unturned cards
CARD_POSITIONS = []      # list of lists of card position mappings
TURNS = 0                # the try counter
GAME_STATE = 0           # state machine persistance
CLICKED_CARD = [0, 0]    # state machine persistance




def new_game():
    ''' helper function to initialize globals '''
    global DECK, EXPOSED, GAME_STATE, TURNS
    GAME_STATE = 0
    TURNS = 0
    # create the deck of cards by joining two decks of equal size
    cards_1 = range(1, (NUM_OF_CARDS // 2) + 1)
    cards_2 = range(1, (NUM_OF_CARDS // 2) + 1)
    DECK = cards_1 + cards_2
    # shuffle the deck
    random.shuffle(DECK)
    # list to set them all face down
    EXPOSED = [False] * NUM_OF_CARDS
    # figure out where they all go
    calc_card_positions()




def calc_card_offsets():
    ''' helper calculates the offsets of the cards '''
    offsets = []
    # make sure rows x cols = NUM_OF_CARDS !!!!
    rows = 2
    cols = 8
    pos = [0, 0]       # point mappings of card polygons
    offset = [50, 50]  # amount grid of cards are from left upper corner
    shift = [60, 110]  # sets spacing between cards
    # generate a list of lists of offsets
    for row in range(rows):
        for col in range(cols):
            pos[0] = col * shift[0] + offset[0]
            pos[1] = row * shift[1] + offset[1]
            offsets.append(list(pos))
    return offsets




def calc_card_positions():
    ''' helper calculates the positions of the cards using pre-calculated offsets '''
    # get the offets
    offset = calc_card_offsets()
    # generate a list of lists of card positions using the offsets
    for card in range(NUM_OF_CARDS):
        CARD_POSITIONS.append(list([[offset[card][0], offset[card][1]],
                                    [offset[card][0] + CARD_SIZE[0], offset[card][1]],
                                    [offset[card][0] + CARD_SIZE[0], offset[card][1] + CARD_SIZE[1]],
                                    [offset[card][0], offset[card][1] + CARD_SIZE[1]]]))




# define event handlers
def mouseclick(pos):
    ''' game state logic, here is the state machine '''
    global GAME_STATE, TURNS
    # find where we clicked, returns > zero if clicked on a card...
    card = mouse_is_on_a_card(pos)
    # game state machine, but better to check these super states first
    if False in EXPOSED and card > 0 and not EXPOSED[card - 1]:
        # ok, not all cards are exposed and mouse was clicked on a card
        # and the clicked card was not already exposed
        # messy but need to card minus one to match list addressing...
        if GAME_STATE == 0:
            # no cards exposed, store card
            CLICKED_CARD[0] = card - 1
            # turn the card
            EXPOSED[CLICKED_CARD[0]] = True
            # update state
            GAME_STATE = 1
        elif GAME_STATE == 1:
            # one card exposed, store new card
            CLICKED_CARD[1] = card - 1
            # turn the card
            EXPOSED[CLICKED_CARD[1]] = True
            # increment the counter
            TURNS += 1
            # update state
            GAME_STATE = 2
        else: # GAME_STATE == 2
            # two cards exposed, compare values stored in DECK[]
            if DECK[CLICKED_CARD[0]] != DECK[CLICKED_CARD[1]]:
                # unlucky, turn back the last two cards
                EXPOSED[CLICKED_CARD[0]] = False
                EXPOSED[CLICKED_CARD[1]] = False
            # store first card again
            CLICKED_CARD[0] = card - 1
            # turn the card
            EXPOSED[CLICKED_CARD[0]] = True
            # update state
            GAME_STATE = 1




def mouse_is_on_a_card(pos):
    ''' helper to find if pos is within one of the cards,
        returns zero if not on a card, or a card number from 1 to 16 '''
    for card in range(NUM_OF_CARDS):
        if pos[0] > CARD_POSITIONS[card][0][0] and \
           pos[0] < CARD_POSITIONS[card][1][0] and \
           pos[1] < CARD_POSITIONS[card][2][1] and \
           pos[1] < CARD_POSITIONS[card][3][1]:
            # found a card so return with card num + 1
            return card + 1
    # not on a card so return zero
    return 0




def draw(canvas):
    ''' the draw handler '''
    back_fill_color = 'Green'
    face_fill_color = 'White'
    line_color = 'Red'
    text_colour = 'Black'
    line_width = 3
    font_size = 24
    label.set_text("Turns = " + str(TURNS))
    for card in range(NUM_OF_CARDS):
        if EXPOSED[card]:
            # exposed card so display outline and value
            canvas.draw_polygon(CARD_POSITIONS[card], line_width, line_color, face_fill_color)
            canvas.draw_text(str(DECK[card]), calc_text_posn(card), font_size, text_colour)
        else:
            # card is face down, don't show value
            canvas.draw_polygon(CARD_POSITIONS[card], line_width, line_color, back_fill_color)




def calc_text_posn(card):
    ''' Helper derives the text position from the card position so we can place
        the value in the middle of the card when the card is exposed.
        Assumes that card is the card number integer
        Uses global CARD_POSITIONS '''
    posn = [0, 0]
    posn[0] = CARD_POSITIONS[card][0][0] + CARD_SIZE[0] // 3
    posn[1] = CARD_POSITIONS[card][0][1] + CARD_SIZE[1] // 2
    return posn




# create frame and add a button and labels
frame = simplegui.create_frame("Memory", CANVAS_SIZE[0], CANVAS_SIZE[1])
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(TURNS))




# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)




# get things rolling
new_game()
frame.start()


