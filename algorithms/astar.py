from queue import PriorityQueue
from algorithms.algorithm import Algorithm  # pylint: disable=E0401
import pygame


@Algorithm.register("astar")
class A_star(Algorithm):
    def search(self, draw, grid, start, end):
        cnt = 1
        open_queue = PriorityQueue()
        open_queue.put((0, cnt, start))
        came_from = dict()
        g_score = {node: float("inf") for row in grid for node in row}
        g_score[start] = 0
        f_score = {node: float("inf") for row in grid for node in row}
        f_score[start] = self.h(start, end)

        open_set = {start}

        while open_set:
            for event in pygame.event.get():  # pylint: disable=E1101
                if event.type == pygame.QUIT:  # pylint: disable=E1101
                    pygame.quit()  # pylint: disable=E1101

            current = open_queue.get()[2]
            open_set.remove(current)

            if current == end:
                self.find_path(came_from, end, draw)
                end.make_end()
                start.make_start()
                return True

            for neighbor in current.neighbors:
                tmp_g_score = g_score[current] + 1

                # update previous path and all weights if new g_score is better than previous
                if tmp_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tmp_g_score
                    f_score[neighbor] = tmp_g_score + self.h(neighbor, end)

                    # add neighbor if it is not in queue
                    # TODO: should consider else statement
                    if neighbor not in open_set:
                        cnt += 1
                        open_queue.put((f_score[neighbor], cnt, neighbor))
                        open_set.add(neighbor)
                        neighbor.make_open()

            if current != start:
                current.make_closed()

            draw()

        return False
