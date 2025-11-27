"""
A gui library for Pygame. Developed by 5Stygian :3.
"""

import pygame

class Rect(pygame.sprite.Sprite):
    """
    A class that rect-like pyggui classes inherit from. Can also be used on its own.

    Attributes:
        screen (pygame.surface.Surface): A pygame.surface.Surface object.

        fill (tuple[int, int, int] | pygame.color.Color): A color value.

        image (pygame.surface.Surface): The image of the object.
        rect (pygame.rect.Rect): The rect of the object.
    """

    def __init__(self, screen: pygame.surface.Surface, left: int, top: int, width: int, height: int,
                 fill: tuple[int, int, int] | pygame.color.Color):
        """
        Class constructor.

        Args:
            screen (pygame.surface.Surface): A pygame.Surface object.
            left (int): The x coord of the top left corner of the sprite.
            top (int): The y coord of the top left corner of the sprite.
            width (int): The width of the sprite.
            height (int): The height of the sprite.
            fill (tuple[int, int, int] | pygame.color.Color): A color value.
        """

        pygame.sprite.Sprite.__init__(self)

        self.screen = screen

        self.fill = fill

        self.image = pygame.surface.Surface([width, height])
        self.image.fill(self.fill)

        self.rect = self.image.get_rect()

        self.rect.x = left
        self.rect.y = top

    def draw(self) -> None:
        """Draws the rect."""

        self.screen.blit(self.image, self.rect)

    def centerToWindow(self, screen: pygame.surface.Surface) -> None:
        """
        Center the object to the center of the main window.

        Arguments:
            screen (pygame.surface.Surface): The screen you create when using pygame.display.set_mode().
        """

        self.rect.center = (int(screen.get_width() / 2), int(screen.get_height() / 2))

class Label(pygame.sprite.Sprite):
    """
    A class that can draw text.

    Attributes:
        screen (pygame.surface.Surface): A pygame.surface.Surface object.

        left (int): The x coord of the top left corner of the sprite.
        top (int): The y coord of the top left corner of the sprite.

        text (str): The text of the label.
        font (pygame.font.Font): The font of the label.
        color (tuple[int, int, int] | pygame.color.Color): A color value.

        image (pygame.surface.Surface): The image of the object.
        rect (pygame.rect.Rect): The rect of the object.
    """

    def __init__(self, screen: pygame.surface.Surface, left: int, top: int, text: str, font: pygame.font.Font,
                 color: tuple[int, int, int] | pygame.color.Color):
        """
        Class constructor.

        Args:
            screen (pygame.surface.Surface): A pygame.surface.Surface object.
            left (int): The x coord of the top left corner of the sprite.
            top (int): The y coord of the top left corner of the sprite.
            text (str): The text of the label.
            font (pygame.font.Font): The font of the label.
            color (tuple[int, int, int] | pygame.color.Color): A color value.
        """

        pygame.sprite.Sprite.__init__(self)

        self.screen = screen

        self.left = left
        self.top = top

        self.text = text
        self.font = font
        self.color = color

        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect()

        self.rect.x = self.left
        self.rect.y = self.top

    def draw(self) -> None:
        """Draw the label."""

        self.screen.blit(self.image, self.rect)

    def centerToWindow(self, screen: pygame.surface.Surface) -> None:
        """
        Center the object to the center of the main window.

        Arguments:
            screen (pygame.surface.Surface): The screen you create when using pygame.display.set_mode().
        """

        self.rect.center = (int(screen.get_width() / 2), int(screen.get_height() / 2))

class Menu(Rect):
    """
    A class that rect-like pyggui classes inherit from. Can also be used on its own.

    Attributes:
        parent (Menu | None): A Menu object.
        screen (pygame.surface.Surface): A pygame.surface.Surface object.

        fill (tuple[int, int, int] | pygame.color.Color): A color value.

        image (pygame.surface.Surface): The image of the object.
        rect (pygame.rect.Rect): The rect of the object.

        sprites (pygame.sprite.Group): A pygame.sprite.Group object that contains all the child sprites of the object.
        buttons (pygame.sprite.Group): A pygame.sprite.Group object that contains all the child buttons of the object.
        labels (pygame.sprite.Group): A pygame.sprite.Group object that contains all the child labels of the object.
    """

    def __init__(self, *args, parent = None):
        """
        Class constructor.

        Args:
            screen (pygame.surface.Surface): A pygame.Surface object.
            left (int): The x coord of the top left corner of the sprite.
            top (int): The y coord of the top left corner of the sprite.
            width (int): The width of the sprite.
            height (int): The height of the sprite.
            fill (tuple[int, int, int] | pygame.color.Color): A color value.

        Keyword Args:
            parent (Menu | None): A Menu object.
        """

        super().__init__(*args)

        if parent is not None:
            self.parent = parent
            if type(parent) != Menu:
                raise TypeError(f"type of parent should be Menu, not {self.parent.__class__.__name__}")

        self.sprites = pygame.sprite.Group()
        self.buttons = pygame.sprite.Group()
        self.labels  = pygame.sprite.Group()

    def drawAll(self) -> None:
        """Draws all child objects of this menu, as well as the menu itself."""

        self.draw()
        for sprite in self.sprites:
            sprite.draw()

    def addEventListener(self, mousePos: tuple[int, int]) -> None:
        """
        Calls each child buttons onclick function.

        Arguments:
            mousePos (tuple[int, int]): The position of the mouse.
        """

        for button in self.buttons:
            if button.onclick is not None and button.rect.contains((*mousePos, 1, 1)):
                button.onclick()

    class Label(Label):
        """
        A class that can draw text. Aligned to a parent Menu.

        Attributes:
            parent (pyggui.Menu): A Menu object.
            screen (pygame.surface.Surface): A pygame.surface.Surface object.

            left (int): The x coord of the top left corner of the sprite.
            top (int): The y coord of the top left corner of the sprite.

            text (str): The text of the label.
            font (pygame.font.Font): The font of the label.
            color (tuple[int, int, int] | pygame.color.Color): A color value.

            image (pygame.surface.Surface): The image of the object.
            rect (pygame.rect.Rect): The rect of the object.
        """

        def __init__(self, parent, *args):
            """
            Class constructor.

            Args:
                screen (pygame.surface.Surface): A pygame.surface.Surface object.
                left (int): The x coord of the top left corner of the sprite.
                top (int): The y coord of the top left corner of the sprite.
                text (str): The text of the label.
                font (pygame.font.Font): The font of the label.
                color (tuple[int, int, int] | pygame.color.Color): A color value.
            """

            Label.__init__(self, *args)

            self.parent = parent

            self.rect.x = self.parent.rect.left + self.rect.left
            self.rect.y = self.parent.rect.top + self.rect.top

            self.parent.sprites.add(self)
            self.parent.labels.add(self)

        def centerToParent(self) -> None:
            """Center the object to the parents centerx."""

            self.rect.centerx = self.parent.rect.centerx

    class Button(Rect):
        """
        Renders a button to the screen.

        Attributes:
            parent (Menu): A Menu object.
            onclick (callable): A function.

            screen (pygame.surface.Surface): A pygame.surface.Surface object.
        """

        def __init__(self, parent, *args,
                     onclick = None):
            """
            Class Constructor.

            Args:
                parent (Menu): A Menu object.

                screen (pygame.surface.Surface): A pygame.surface.Surface object.

                left (int): The leftmost coord of the sprite.
                bottom (int): The bottommost coord of the sprite.

                width (int): The width of the sprite.
                height (int): The height of the sprite.

                fill (tuple[int, int, int] | pygame.color.Color): A color value.

            Keyword Args:
                onclick (callable): A function.
            """

            super().__init__(*args)

            self.parent = parent
            if type(self.parent) != Menu:
                raise TypeError(f"type of parent must be Menu, not {self.parent.__class__.__name__}")

            self.onclick = onclick
            if self.onclick is not None and not callable(onclick):
                raise TypeError(f"type of onclick must be callable, not {self.onclick.__class__.__name__}")

            self.rect.x = self.parent.rect.left + self.rect.left
            self.rect.y = self.parent.rect.top + self.rect.top

            self.parent.sprites.add(self)
            self.parent.buttons.add(self)

        def centerToParent(self) -> None:
            """Center the object to the parents centerx."""

            self.rect.centerx = self.parent.rect.centerx

        def addEventListener(self, mousePos: tuple[int, int]) -> None:
            """
            Calls the objects onclick function.

            Arguments:
                mousePos (tuple[int, int]): The position of the mouse.
            """

            if self.onclick is not None and self.rect.contains((*mousePos, 1, 1)):
                self.onclick()

if __name__ == "__main__":
    class FuckYouException(Exception):
        def __init__(self, message):
            super().__init__(message)
            self.message = message

        def __repr__(self) -> str:
            return super().__repr__()

    raise FuckYouException("dont run ts like that")