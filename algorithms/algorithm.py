from abc import ABC, abstractmethod

_registry = {}


class Algorithm(ABC):
    def __init__(self):
        pass

    @staticmethod
    def h(p1, p2):
        x1, y1 = p1.get_pos()
        x2, y2 = p2.get_pos()
        return abs(x1 - x2) + abs(y1 - y2)

    @staticmethod
    def find_path(came_from, current, draw):
        while current in came_from:
            current = came_from[current]
            current.make_path()
            draw()

    @abstractmethod
    def search(self, draw, grid, start, end):
        pass

    @classmethod
    def register(cls, name):
        def register_algo_by_name(algo_class):
            if name in _registry:
                raise LookupError("algorithm already registered")
            _registry[name] = algo_class
            return algo_class

        return register_algo_by_name

    @classmethod
    def get_algorithm(cls, name):
        if name not in _registry:
            raise LookupError(f"{name} is not registered")
        return _registry[name]
