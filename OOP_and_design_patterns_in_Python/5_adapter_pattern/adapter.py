class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def _get_lights_and_obstacles(self, grid):
        lights = []
        obstacles = []
        for i in range(self.adaptee.dim[0]):
            for j in range(self.adaptee.dim[1]):
                if grid[i][j] == 1:
                    lights.append((i, j))
                elif grid[i][j] == -1:
                    obstacles.append((i, j))
                else:
                    continue
        return lights, obstacles

    def lighten(self, grid):
        dim = (len(grid[0]), len(grid)) # т.к. класс применяет сначала ширину, а потом высоту
        self.adaptee.set_dim(dim)
        lights, obstacles = self._get_lights_and_obstacles(grid)
        self.adaptee.set_obstacles(obstacles)
        self.adaptee.set_lights(lights)
        return self.adaptee.generate_lights()
