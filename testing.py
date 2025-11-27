"""A testing file for development."""

if __name__ == "__main__":
    import pygame
    import pyggui as gui

    from collections import namedtuple

    pygame.init()

    pygame.display.set_caption("pyggui")
    clock = pygame.time.Clock()
    running = True
    dt = 0

    screen = pygame.display.set_mode((1280, 720))
    ScreenDimensions = namedtuple("ScreenDimensions", ('width', 'height', 'center', 'centerx', 'centery'))
    ScreenDims = ScreenDimensions(
        int(screen.get_width()),
        int(screen.get_height()),
        (int(screen.get_width() / 2), int(screen.get_height() / 2)),
        int(screen.get_width() / 2),
        int(screen.get_height() / 2),
    )

    font = pygame.font.Font("Rubik\Rubik-VariableFont_wght.ttf", size=24)

    rect = gui.Rect(
        screen,
        0, 0,
        100, 100,
        (255,255,255)
    )

    menu = gui.Menu(
        screen,
        100, 0,
        300, ScreenDims.height,
        pygame.color.Color(255, 255, 255)
    )

    button = gui.Menu.Button(
        menu,
        screen,
        0, 0,
        200, 60,
        (170, 70, 120),
        onclick=lambda x="1": print(x)
    )
    button.centerToParent()

    menuLabel = gui.Menu.Label(
        menu,
        screen,
        0, 0,
        "TEST",
        font,
        (0, 0, 0)
    )
    menuLabel.centerToParent()

    rect.centerToWindow(screen)

    print(type(menu))

    while running:
        mousePos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0]:
                menu.addEventListener(mousePos)

            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        screen.fill("black")

        rect.draw()
        menu.drawAll()

        pygame.display.flip()
        dt = clock.tick(60) / 1000
else:
    class FuckYouException(Exception):
        def __init__(self, message):
            super().__init__(message)
            self.message = message

        def __repr__(self) -> str:
            return super().__repr__()

    raise FuckYouException("dont run ts like that")