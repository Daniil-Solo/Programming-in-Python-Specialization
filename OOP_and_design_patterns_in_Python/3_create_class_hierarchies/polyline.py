import pygame

from vec import Vec2d


class Polyline:
    def __init__(self, points, speeds):
        self.points = points
        self.speeds = speeds

    def add_point(self, point, speed):
        x, y = point
        vec = Vec2d(x, y)
        self.points.append(vec)
        x_speed, y_speed = speed
        vec_sped = Vec2d(x_speed, y_speed)
        self.speeds.append(vec_sped)

    def set_points(self, screed_dim):
        width, height = screed_dim
        for p in range(len(self.points)):
            self.points[p] = self.points[p] + self.speeds[p]
            if self.points[p].x > width or self.points[p].x < 0:
                self.speeds[p] = Vec2d(-self.speeds[p].x, self.speeds[p].y)
            if self.points[p].y > height or self.points[p].y < 0:
                self.speeds[p] = Vec2d(self.speeds[p].x, -self.speeds[p].y)

    def draw_points(self, game_display, style='points', width=3, color=(255, 255, 255)):
        if style == "line":
            for p_n in range(-1, len(self.points) - 1):
                pygame.draw.line(game_display, color,
                                 (int(self.points[p_n].x), int(self.points[p_n].y)),
                                 (int(self.points[p_n + 1].x), int(self.points[p_n + 1].y)), width)
        elif style == "points":
            for p in self.points:
                pygame.draw.circle(game_display, color,
                                   (int(p[0]), int(p[1])), width)
