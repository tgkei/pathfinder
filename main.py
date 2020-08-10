import math
import pygame

from algorithms import astar  # pylint: disable=E0401
import util

WIDTH = 800

WINDOW = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Path simulator")


# TODO: change update_neighbors parts with following
# Additionally consider if path can go to diagonal
# MOVEMENTS = [(1, 0), (-1, 0), (0, 1), (0,-1)]


def main(window, width):
    ROWS = 50
    grid = util.make_grid(ROWS, width)

    start = None
    end = None
    # TODO: handle when path is not found
    found = False

    is_running = True

    while is_running:
        util.draw(window, grid, ROWS, width)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # pylint: disable=E1101
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

            if event.type == pygame.KEYDOWN:  # pylint: disable=E1101
                if event.key == pygame.K_SPACE:  # pylint: disable=E1101
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    algorithm = astar.A_star()
                    found = algorithm.search(
                        lambda: util.draw(window, grid, ROWS, width), grid, start, end
                    )

    pygame.quit()  # pylint: disable=E1101


if __name__ == "__main__":
    main(WINDOW, WIDTH)
