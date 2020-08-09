import math
from queue import PriorityQueue
import pygame

WIDTH = 800

WINDOW = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Path simulator")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUISE = (64, 224, 208)


class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.width = width
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.total_rows = total_rows

    def get_pos(self):
        return self.col, self.row

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == PURPLE

    def reset(self):
        self.color = WHITE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_start(self):
        self.color = ORANGE

    def make_end(self):
        self.color = PURPLE

    def make_path(self):
        self.color = TURQUISE

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        pass

    def __lt__(self, other):
        return False


def h(p1, p2):
    x1, y1 = p1.get_pos()
    x2, y2 = p2.get_pos()
    return abs(x1 - x2) + abs(y1 - y2)


def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)
    return grid


def draw_grid(window, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(window, GREY, (0, i * gap), (width, i * gap))
        pygame.draw.line(window, GREY, (i * gap, 0), (i * gap, width))


def draw(window, grid, rows, width):
    for row in grid:
        for node in row:
            node.draw(window)

    draw_grid(window, rows, width)
    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap
    return row, col


def main(window, width):
    ROWS = 50
    grid = make_grid(ROWS, width)

    start = None
    end = None

    is_running = True
    is_started = False

    while is_running:
        draw(window, grid, ROWS, width)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # pylint: disable=E1101
                is_running = False

            if is_started:
                continue

            if pygame.mouse.get_pressed()[0]:  # clicking left mouse button
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]

                # first click = start
                if not start and not node.is_barrier() and not node.is_end():
                    start = node
                    start.make_start()
                # second click = end
                elif not end and not node.is_barrier() and not node.is_start():
                    end = node
                    end.make_end()
                # other click = barrier
                elif not node.is_end() and not node.is_start():
                    node.make_barrier()

            elif pygame.mouse.get_pressed()[2]:  #  click right mouse button
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]

                if node.is_start():
                    start = None
                elif node.is_end():
                    end = None

                node.reset()

    pygame.quit()  # pylint: disable=E1101


if __name__ == "__main__":
    main(WINDOW, WIDTH)
