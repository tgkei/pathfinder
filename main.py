import time
from argparse import ArgumentParser
import math
import pygame

from algorithms.algorithm import Algorithm  # pylint: disable=E0401
import util

WIDTH = 600
ROWS = 30
NO_PATH_TEXT = "NO PATH FOUND"
FONT_SIZE = 64

pygame.init()  # pylint: disable=E1101
WINDOW = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Path simulator")


# # TODO: have to change to register decorator later shouldn't be here
# _ALGORITHM = {"astar": astar.A_star, "dfs": dfs.DFS, "bfs": bfs.BFS}


# TODO: change update_neighbors parts with following
# Additionally consider if path can go to diagonal
# MOVEMENTS = [(1, 0), (-1, 0), (0, 1), (0,-1)]


def main(window, width, algo):
    grid = util.make_grid(ROWS, width)

    start = None
    end = None
    # TODO: handle when path is not found
    found = False

    is_running = True

    while is_running:
        util.draw(window, grid, ROWS, width)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # pylint: disable=e1101
                is_running = False

            if pygame.mouse.get_pressed()[0]:  # clicking left mouse button
                pos = pygame.mouse.get_pos()
                row, col = util.get_clicked_pos(pos, ROWS, width)
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
                row, col = util.get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]

                if node.is_start():
                    start = None
                elif node.is_end():
                    end = None

                node.reset()

            if event.type == pygame.KEYDOWN:  # pylint: disable=e1101
                if event.key == pygame.K_SPACE:  # pylint: disable=e1101
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    algorithm = algo
                    found = algorithm.search(
                        lambda: util.draw(window, grid, ROWS, width), grid, start, end
                    )
                    if not found:
                        largeText = pygame.font.Font("freesansbold.ttf", FONT_SIZE)
                        TextSurf, TextRect = util.text_objects(NO_PATH_TEXT, largeText)
                        TextRect.center = ((WIDTH // 2), (WIDTH // 2))
                        WINDOW.blit(TextSurf, TextRect)

                        pygame.display.update()

                        time.sleep(2)

                if event.key == pygame.K_r:  # pylint: disable=E1101
                    start = None
                    end = None
                    grid = util.make_grid(ROWS, WIDTH)

    pygame.quit()  # pylint: disable=E1101


if __name__ == "__main__":
    parser = ArgumentParser(description="Path finding visualizer")
    parser.add_argument("--algorithm", "-algo", default="astar", help="which argument")
    args = parser.parse_args()
    algorithm = args.algorithm

    algo = Algorithm.get_algorithm(algorithm)()
    main(WINDOW, WIDTH, algo)
