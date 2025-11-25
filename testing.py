if __name__ == "__main__":
    import pygame
    import pyggui as gui

    pygame.init()

    pygame.display.set_caption("pyggui")
    clock = pygame.time.Clock()
    running = True
    dt = 0

    screen = pygame.display.set_mode((1280, 720))
    screenDims = {
        "X": screen.get_width(), 
        "Y": screen.get_height()
    }

    def button1Foo():
        print("button1 click")

    def button2Foo():
        print("button2 click")

    menu = gui.Menu(
        screen,
        0, 0,
        300, screenDims["Y"],
        pygame.color.Color(255, 255, 255)
    )

    button = gui.Menu.Button(
        menu,
        screen,
        23, 50,
        90, 60,
        pygame.color.Color(80, 120, 160),
        onclick=button1Foo
    )

    button2 = gui.Menu.Button(
        menu,
        screen,
        167, 150,
        90, 60,
        pygame.color.Color(170, 120, 160),
        onclick=button2Foo
    )

    button.centerToParent()
    button2.centerToParent()

    while running:
        mousePos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0]:
                menu.addEventListener(mousePos)

            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
        
        screen.fill("black")

        menu.draw()

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
