from algorithms.abcalgo import Abc_algo  # pylint: disable=E0401
import pygame


class BFS(Abc_algo):
    def search(self, draw, grid, start, end):
        open_stack = []
        open_stack.append(start)
        open_set = {start}  # prevent to cycle the path
        came_from = dict()

        while open_stack:
            for event in pygame.event.get():  # pylint: disable=E1101
                if event.type == pygame.QUIT:  # pylint: disable=E1101
                    pygame.quit()  # pylint: disable=E1101

            current = open_stack.pop()

            if current == end:
                self.find_path(came_from, current, draw)
                end.make_end()
                start.make_start()
                return True

            for neighbor in current.neighbors:
                if neighbor not in open_set:
                    came_from[neighbor] = current
                    open_stack.append(neighbor)
                    open_set.add(neighbor)
                    neighbor.make_open()

            if current != start:
                current.make_closed()

            draw()

        return False
