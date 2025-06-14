import pygame
import random

# Cấu hình ban đầu
pygame.init()
WIDTH, HEIGHT = 640, 480
ROWS, COLS = 6, 8
TILE_SIZE = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pikachu Đơn Giản")
font = pygame.font.SysFont(None, 36)

# Tạo bảng với các cặp ngẫu nhiên
def create_board():
    icons = [i for i in range((ROWS * COLS) // 2)] * 2
    random.shuffle(icons)
    board = [icons[i * COLS:(i + 1) * COLS] for i in range(ROWS)]
    return board

board = create_board()
selected = []
running = True

def draw_board():
    screen.fill((255, 255, 255))
    for i in range(ROWS):
        for j in range(COLS):
            val = board[i][j]
            rect = pygame.Rect(j*TILE_SIZE, i*TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, (200, 200, 255), rect)
            pygame.draw.rect(screen, (0, 0, 0), rect, 2)
            if val != -1:
                img = font.render(str(val), True, (0, 0, 0))
                screen.blit(img, (j*TILE_SIZE + 20, i*TILE_SIZE + 15))

def check_match():
    global selected
    if len(selected) == 2:
        (x1, y1), (x2, y2) = selected
        if board[y1][x1] == board[y2][x2] and (x1, y1) != (x2, y2):
            board[y1][x1] = board[y2][x2] = -1
        selected = []

# Game loop
while running:
    draw_board()
    pygame.display.flip()
    check_match()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos[0] // TILE_SIZE, event.pos[1] // TILE_SIZE
            if board[y][x] != -1:
                selected.append((x, y))
pygame.quit()

