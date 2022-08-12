"""
Создайте программу для игры в "Крестики-нолики"

"""
import pygame
import sys


def win_game(mas, sign):
    count_zer = 0
    diag = []
    diag1 = []
    for i in range(3):
        diag.append(mas[i][i])
        diag1.append(mas[2 - i][i])
        if diag.count(sign) == 3 or diag1.count(sign) == 3:
            return sign + ' win'
    for row in mas:
        count_zer += row.count(0)
        if row.count(sign) == 3:
            return sign + ' win'
    for col in range(3):
        if [x[col] for x in mas].count(sign) == 3:
            return sign + ' win'
    if count_zer == 0:
        return 'Piece \n for restart press SPACE'
    return False


pygame.init()
size_block = 100
margin = 15
width = height = size_block * 3 + margin * 4

size_window = (width, height)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption('TIC-TAC-TOE')
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
count = 0
game_over = False
mas = [[0] * 3 for i in range(3)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()

            col = x_mouse // (size_block + margin)
            row = y_mouse // (size_block + margin)

            if mas[row][col] == 0:
                if count % 2 == 0:
                    mas[row][col] = 'X'
                else:
                    mas[row][col] = 'O'
                count += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            count = 0
            mas = [[0] * 3 for i in range(3)]
            screen.fill(black)

    if not game_over:
        for row in range(3):
            for col in range(3):
                if mas[row][col] == 'X':
                    color = blue

                elif mas[row][col] == 'O':
                    color = green
                else:
                    color = white
                x = col * size_block + (col + 1) * margin
                y = row * size_block + (row + 1) * margin
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                if mas[row][col] == 'X':
                    pygame.draw.line(screen, green, (x + size_block / 4, y + size_block / 4),
                                     (x + size_block * 3 / 4, y + size_block * 3 / 4), 10)
                    pygame.draw.line(screen, green, (x + size_block / 4, y + size_block * 3 / 4),
                                     (x + size_block * 3 / 4, y + size_block / 4), 10)
                elif mas[row][col] == 'O':
                    pygame.draw.circle(screen, blue, (x + size_block / 2, y + size_block / 2), size_block * 1.27 / 4,
                                       10)

    if (count - 1) % 2 == 0:
        game_over = win_game(mas, 'X')
    else:
        game_over = win_game(mas, 'O')

    if game_over:
        screen.fill(black)
        font = pygame.font.SysFont('Monserrat', 77)
        text1 = font.render(game_over, True, white)
        test_rect = text1.get_rect()
        text_x = screen.get_width() / 2 - test_rect.width / 2
        text_y = screen.get_height() / 2 - test_rect.height / 2
        screen.blit(text1, [text_x, text_y])
        font = pygame.font.SysFont('Monserrat', 35)
        text2 = font.render('Press SPACE for Restart!', True, white)
        test_rect = text2.get_rect()
        text_x = screen.get_width() / 2 - test_rect.width / 2
        text_y = screen.get_height() / 2 + test_rect.height * 2
        screen.blit(text2, [text_x, text_y])

    pygame.display.update()
