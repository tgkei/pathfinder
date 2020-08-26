from collections import deque
from algorithms.algorithm import Algorithm  # pylint: disable=E0401
import pygame


@Algorithm.register("dfs")
class DFS(Algorithm):
    def search(self, draw, grid, start, end):
        open_queue = deque()
        open_queue.append(start)
        open_set = {start}  # prevent to cycle the path
        came_from = dict()

        while open_queue:
            for event in pygame.event.get():  # pylint: disable=E1101
                if event.type == pygame.QUIT:  # pylint: disable=E1101
                    pygame.quit()  # pylint: disable=E1101

            current = open_queue.pop()

            if current == end:
                self.find_path(came_from, current, draw)
                end.make_end()
                start.make_start()
                return True

            for neighbor in current.neighbors:
                if neighbor not in open_set:
                    came_from[neighbor] = current
                    open_queue.append(neighbor)
                    open_set.add(neighbor)
                    neighbor.make_open()

            if current != start:
                current.make_closed()

            draw()

        return False
