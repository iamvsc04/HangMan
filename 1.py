#game for vocabulary improvement
import pygame
import math
import random
pygame.init()
WIDTH, HEIGHT = 900, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game For Vocabulary Improvement")
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 1.95 + GAP) * 13) / 2)
starty = 390
A = 65
for i in range(26):
    x = startx + GAP * 2.5 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2.5))
    letters.append([x, y, chr(A + i), True])
LETTER_FONT = pygame.font.SysFont('comicsans', 30)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 40)
char_font=pygame.font.SysFont('comicsans', 40)
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)
hangman_status = 0
words = ["IDEAS", "REPLITS", "PYTHON", "PYGAMES","DUMPLINGS","APPLE","BANANA","CARROT","EGGS","FISH","CRAB","GINGER"]
word = random.choice(words)
guessed = []
WHITE = (255,255,255)
BLACK = (0,0,0)
def draw():
    win.fill(WHITE)
    text = TITLE_FONT.render("Guess the Word Having letter "+word[-1], 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 8))  
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))

    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 2)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
    win.blit(images[hangman_status], (70, 120))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(2000)

def main():
    global hangman_status
    FPS = 60
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1

        draw()
        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break
        if won:
            display_message("You WON!")
            break
        if hangman_status == 6:
            display_message("You LOST!")
            break
while True:
    main()
    pygame.quit()
