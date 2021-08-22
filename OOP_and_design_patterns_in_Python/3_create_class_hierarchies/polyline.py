import pygame

from vec import Vec2d


class Polyline:
    def __init__(self, screen_dim):
        self.points = []
        self.speeds = []
        self.width, self.height = screen_dim

    def add_point(self, point, speed):
        x, y = point
        vec = Vec2d(x, y)
        self.points.append(vec)
        x_speed, y_speed = speed
        vec_sped = Vec2d(x_speed, y_speed)
        self.speeds.append(vec_sped)

    def delete_point(self, point, area=3):
        target = Vec2d(point[0], point[1])
        for p, i in zip(self.points, range(len(self.points))):
            if (target.x - area <= p.x <= target.x + area) and (target.y - area <= p.y <= target.y + area):
                self.points.remove(self.points[i])
                self.speeds.remove(self.speeds[i])
                return

    def set_points(self):
        for p in range(len(self.points)):
            self.points[p] = self.points[p] + self.speeds[p]
            if self.points[p].x > self.width or self.points[p].x < 0:
                self.speeds[p] = Vec2d(-self.speeds[p].x, self.speeds[p].y)
            if self.points[p].y > self.height or self.points[p].y < 0:
                self.speeds[p] = Vec2d(self.speeds[p].x, -self.speeds[p].y)

    def draw_lines(self, line_points, game_display, width=3, color=(255, 255, 255)):
        for p_n in range(-1, len(line_points) - 1):
            pygame.draw.line(game_display, color, line_points[p_n].int_pair(), line_points[p_n + 1].int_pair(), width)

    def draw_points(self, game_display, width=3, color=(255, 255, 255)):
        for p in self.points:
            pygame.draw.circle(game_display, color, p.int_pair(), width)

    def reset(self):
        self.points = []
        self.speeds = []
