import pygame
import random
from knot_control import KnotController


SCREEN_DIM = (800, 600)
SPEED_UP = 1.3
SPEED_DOWN = 0.7


def draw_help():
    """функция отрисовки экрана справки программы"""
    gameDisplay.fill((50, 50, 50))
    font1 = pygame.font.SysFont("courier", 24)
    font2 = pygame.font.SysFont("serif", 24)
    data = []
    data.append(["LClick", "Add new point"])
    data.append(["RClick", "Delete this point"])
    data.append(["H", "Show Help"])
    data.append(["R", "Restart"])
    data.append(["P", "Pause/Play"])
    data.append(["+", "More points"])
    data.append(["-", "Less points"])
    data.append(["Up", "More Speed"])
    data.append(["Down", "Less Speed"])
    data.append(["Space", "New figure"])
    data.append(["", ""])
    data.append([str(steps), "Current points"])

    pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
        (0, 0), (800, 0), (800, 600), (0, 600)], 5)
    for i, text in enumerate(data):
        gameDisplay.blit(font1.render(
            text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
        gameDisplay.blit(font2.render(
            text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    steps = 35
    working = True
    show_help = False
    pause = True
    k_controller = KnotController(SCREEN_DIM)

    hue = 0
    color = pygame.Color(0)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    k_controller.reset()
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_PLUS:
                    steps += 1
                if event.key == pygame.K_h:
                    show_help = not show_help
                if event.key == pygame.K_MINUS:
                    steps -= 1 if steps > 1 else 0
                if event.key == pygame.K_SPACE:
                    k_controller.add_new()
                if event.key == pygame.K_UP:
                    k_controller.current_knot().speed_change(koef=SPEED_UP)
                if event.key == pygame.K_DOWN:
                    k_controller.current_knot().speed_change(koef=SPEED_DOWN)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                point = event.pos
                speed = (random.random() * 2, random.random() * 2)
                k_controller.current_knot().add_point(point, speed)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                point = event.pos
                for knot in k_controller:
                    knot.delete_point(point)

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        for knot in k_controller:
            knot.draw_points(game_display=gameDisplay)
            knot.draw_lines(line_points=knot.get_knot(steps), game_display=gameDisplay, color=color)
        if not pause:
            for knot in k_controller:
                knot.set_points()
        if show_help:
            draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
