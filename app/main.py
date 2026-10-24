class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight

class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list[int]) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords


    def go_forward(self, step: int=1) -> None:
        self.coords[1] += step
        


    def go_back(self, step: int=1) -> None:
        self.coords[1] -= step




    def go_left(self, step: int=1) -> None:
        self.coords[0] -= step


    def go_right(self, step: int=1) -> None:
        self.coords[0] += step



class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list[int]) -> None:
        super().__init__(name, weight, coords)
        


    def go_up(self, step: int=1) -> None:
        self.coords[2] += step


    def go_down(self, step: int=1) -> None:
        self.coords[2] -= step

class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str, weight: int, coords: list[int], max_load_weight: int, curent_load: Cargo=None) -> None:
        super().__init__(name, weight, coords)
        self.curent_load = curent_load
        self.max_load_weight = max_load_weight