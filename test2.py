#Thành Mạnh yêu Ngọc Anh
import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Cấu hình màn hình
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Đặt Bom")

# Màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Kích thước ô và số ô trên màn hình
cell_size = 40
num_cells_x = screen_width // cell_size
num_cells_y = screen_height // cell_size

# Lớp Ô
class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.bomb = False
        self.revealed = False
        self.neighbors = []

    def draw(self):
        rect = pygame.Rect(self.x * cell_size, self.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, WHITE, rect, 1)
        if self.revealed:
            if self.bomb:
                pygame.draw.circle(screen, RED, (self.x * cell_size + cell_size // 2, self.y * cell_size + cell_size // 2), cell_size // 2 - 4)
            else:
                pygame.draw.rect(screen, WHITE, rect)

    def reveal(self):
        self.revealed = True
        if not self.bomb and self.count_bombs() == 0:
            for neighbor in self.neighbors:
                if not neighbor.revealed:
                    neighbor.reveal()

    def count_bombs(self):
        count = 0
        for neighbor in self.neighbors:
            if neighbor.bomb:
                count += 1
        return count

# Tạo lưới ô
grid = []
for y in range(num_cells_y):
    row = []
    for x in range(num_cells_x):
        cell = Cell(x, y)
        row.append(cell)
    grid.append(row)

# Thiết lập số bom và tạo bom ngẫu nhiên
num_bombs = 10
bombs_placed = 0
while bombs_placed < num_bombs:
    x = random.randint(0, num_cells_x - 1)
    y = random.randint(0, num_cells_y - 1)
    cell = grid[y][x]
    if not cell.bomb:
        cell.bomb = True
        bombs_placed += 1

# Liên kết ô hàng xóm
for y in range(num_cells_y):
    for x in range(num_cells_x):
        cell = grid[y][x]
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dy == 0 and dx == 0:
                    continue
                nx = x + dx
                ny = y + dy
                if nx >= 0 and nx < num_cells_x and ny >= 0 and ny < num_cells_y:
                    neighbor = grid[ny][nx]
                    cell.neighbors.append(neighbor)

# Vòng lặp chính
running = True
clock = pygame.time.Clock()

while running:
    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Bấm chuột trái
                x, y = event.pos
                cell_x = x // cell_size
                cell_y = y // cell_size
                cell = grid[cell_y][cell_x]
                if not cell.revealed:
                    cell.reveal()

    # Vẽ màn hình
    screen.fill(BLACK)
    for row in grid:
        for cell in row:
            cell.draw()
    pygame.display.flip()

    # Giới hạn tốc độ khung hình
    clock.tick(30)

# Kết thúc Pygame
pygame.quit()
