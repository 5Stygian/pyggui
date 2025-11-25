"""
A gui library for Pygame. Developed by 5Stygian :3.
"""

import pygame

class Rect(pygame.sprite.Sprite):
    """
    A class that all pyggui classes inherit from.

    Attributes:
        screen (pygame.Surface): A pygame.Surface object.
        
        background (tuple[int, int, int] | pygame.color.Color): A color value.
    """
    
    def __init__(self, screen: pygame.Surface, left: int, top: int, width: int, height: int, background: tuple[int, int, int]|pygame.color.Color):
        """
        Class constructor.
        
        Parameters:
            screen (pygame.Surface): A pygame.Surface object.
            left (int): The x coord of the top left corner of the sprite.
            top (int): The y coord of the top left corner of the sprite.
            width (int): The width of the sprite.
            height (int): The height of the sprite.
            background (tuple[int, int, int] | pygame.color.Color): A color value.
        """

        pygame.sprite.Sprite.__init__(self)

        self.screen = screen

        self.background = background

        self.image = pygame.Surface([width, height])
        self.image.fill(self.background)

        self.rect = self.image.get_rect()

        self.rect.x = left
        self.rect.y = top

    def draw(self) -> None:
        """Draws the sprite."""

        self.screen.blit(self.image, self.rect)



class Menu(Rect):
    """
    The base class for pyggui objects.
    
    Attributes:
        sprites (pygame.sprite.Group): A group of all child sprites of the object.
        buttons (pygame.sprite.Group): A group of all child buttons of the object.

        screen (pygame.Surface): A pygame.Surface object.
        
        background (tuple[int, int, int] | pygame.color.Color): A color value.
    """

    def __init__(self, *args):
        """
        Class constructor.

        Parameters:
            screen (pygame.Surface): A pygame.Surface object.

            left (int): The x coord of the top left corner of the sprite.
            top (int): The y coord of the top left corner of the sprite.

            width (int): The width of the sprite.
            height (int): The height of the sprite.

            background (tuple[int, int, int] | pygame.color.Color): A color value.
        """

        super().__init__(*args)

        self.sprites: pygame.sprite.Group = pygame.sprite.Group()
        self.buttons: pygame.sprite.Group = pygame.sprite.Group()

    def draw(self):
        """Draws all child sprites."""

        self.screen.blit(self.image, self.rect)

        for sprite in self.sprites:
            sprite.screen.blit(sprite.image, sprite.rect)

    def addEventListener(self, mousePos) -> None:
        """
        Calls each child buttons onclick function.

        Arguments:
            mousePos (tuple[int, int]): The position of the mouse.
        """

        for button in self.buttons:
            if button.onclick is not None and button.rect.contains((*mousePos, 1, 1)):
                button.onclick()

    class Button(Rect):
        """
        A button.

        Attributes:
            parent (Menu): A Menu object.
            onclick (callable): A function.

            screen (pygame.Surface): A pygame.Surface object.
        """

        def __init__(self, parent, *args, onclick = None):
            """
            Class Constructor.

            Parameters:
                parent (Menu): A Menu object.
                onclick (callable): A function.

                screen (pygame.Surface): A pygame.Surface object.

                left (int): The leftmost coord of the sprite.
                bottom (int): The bottommost coord of the sprite.
                
                width (int): The width of the sprite.
                height (int): The height of the sprite.
                
                background (tuple[int, int, int] | pygame.color.Color): A color value.
            """

            super().__init__(*args)

            self.parent = parent
            if type(self.parent) != Menu:
                raise TypeError(f"type of parent must be Menu, not {self.parent.__class__.__name__}")

            self.onclick = onclick
            if self.onclick is not None and callable(onclick) == False:
                raise TypeError(f"type of onclick must be callable, not {self.onclick.__class__.__name__}")

            self.rect.x = self.parent.rect.left + self.rect.left
            self.rect.y = self.parent.rect.top + self.rect.top

            self.parent.sprites.add(self)
            self.parent.buttons.add(self)

        def centerToParent(self) -> None:
            """Center the object to the parents centerx"""

            self.rect.x = int(self.parent.rect.width/2 - self.rect.width/2)

        def addEventListener(self, mousePos) -> None:
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
