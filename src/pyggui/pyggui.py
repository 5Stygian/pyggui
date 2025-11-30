"""
A gui library for Pygame. Developed by 5Stygian :3.
"""

import pygame

from dataclasses import dataclass

from pygame.sysfont import font_constructor


class _Child:
    """An internal class used by pyggui. Do not use this class."""

    def __init__(self, parent):
        self.parent = parent
        if type(self) == Menu.Label and type(self.parent) == Menu.Button:
            pass
        elif type(self.parent) != Menu:
            raise TypeError(f"type of parent must be Menu, not {self.parent.__class__.__name__}")

        self.rect.x = self.parent.rect.x + self.left
        self.rect.y = self.parent.rect.y + self.top

        if type(self.parent) == Menu:
            self.parent.sprites.add(self)
        else:
            pass

class Color:
    """A class containing colors and color related methods. All members are static, so you don't need to create an object to access them."""

    @staticmethod
    def rgb(r: int, g: int, b: int) -> pygame.color.Color:
        """
        Syntactic sugar.

        Args:
            r (int): The red component of a rgb color.
            g (int): The green component of a rgb color.
            b (int): The blue component of a rgb color.

        Returns:
            (r, g, b) (pygame.color.Color): A pygame.color.Color object.
        """

        if type(r) != int:
            raise TypeError(f"type of r should be int, not {r.__class__.__name__}")
        if r < 0 or r > 255:
            raise ValueError(f"r should be in range 0 - 255, not {r}")

        if type(g) != int:
            raise TypeError(f"type of g should be int, not {g.__class__.__name__}")
        if g < 0 or g > 255:
            raise ValueError(f"g should be in range 0 - 255, not {g}")

        if type(b) != int:
            raise TypeError(f"type of b should be int, not {b.__class__.__name__}")
        if b < 0 or b > 255:
            raise ValueError(f"b should be in range 0 - 255, not {b}")

        return pygame.color.Color(r, g, b)

    @staticmethod
    def rgba(r: int, g: int, b: int, a: int) -> pygame.color.Color:
        """
        Syntactic sugar.

        Args:
            r (int): The red component of a rgba color.
            g (int): The green component of a rgba color.
            b (int): The blue component of a rgba color.
            a (int): The alpha component of a rgba color.

        Returns:
            (r, g, b, a) (pygame.color.Color): A pygame.color.Color object.
        """

        if type(r) != int:
            raise TypeError(f"type of r should be int, not {r.__class__.__name__}")
        if r < 0 or r > 255:
            raise ValueError(f"r should be in range 0 - 255, not {r}")

        if type(g) != int:
            raise TypeError(f"type of g should be int, not {g.__class__.__name__}")
        if g < 0 or g > 255:
            raise ValueError(f"g should be in range 0 - 255, not {g}")

        if type(b) != int:
            raise TypeError(f"type of b should be int, not {b.__class__.__name__}")
        if b < 0 or b > 255:
            raise ValueError(f"b should be in range 0 - 255, not {b}")

        if type(a) != int:
            raise TypeError(f"type of a should be int, not {a.__class__.__name__}")
        if a < 0 or a > 255:
            raise ValueError(f"a should be in range 0 - 255, not {a}")

        return pygame.color.Color(r, g, b, a=a)

    @dataclass
    class CSS3:
        """A dataclass containing all CSS3 colors."""

        aliceblue            = pygame.color.Color(240, 248, 255)
        antiquewhite         = pygame.color.Color(250, 235, 215)
        aqua                 = pygame.color.Color(0, 255, 255)
        aquamarine           = pygame.color.Color(127, 255, 212)
        azure                = pygame.color.Color(240, 255, 255)
        beige                = pygame.color.Color(245, 245, 220)
        bisque               = pygame.color.Color(255, 228, 196)
        black                = pygame.color.Color(0, 0, 0)
        blanchedalmond       = pygame.color.Color(255, 235, 205)
        blue                 = pygame.color.Color(0, 0, 255)
        blueviolet           = pygame.color.Color(138, 43, 226)
        brown                = pygame.color.Color(165, 42, 42)
        burlywood            = pygame.color.Color(222, 184, 135)
        cadetblue            = pygame.color.Color(95, 158, 160)
        chartreuse           = pygame.color.Color(127, 255, 0)
        chocolate            = pygame.color.Color(210, 105, 30)
        coral                = pygame.color.Color(255, 127, 80)
        cornsilk             = pygame.color.Color(255, 248, 220)
        cornflowerblue       = pygame.color.Color(100, 149, 237)
        crimson              = pygame.color.Color(220, 20, 60)
        cyan                 = pygame.color.Color(0, 255, 255)
        darkblue             = pygame.color.Color(0, 0, 139)
        darkcyan             = pygame.color.Color(0, 139, 139)
        darkgoldenrod        = pygame.color.Color(184, 134, 11)
        darkgray             = pygame.color.Color(169, 169, 169)
        darkgreen            = pygame.color.Color(0, 100, 0)
        darkgrey             = pygame.color.Color(169, 169, 169)
        darkkhaki            = pygame.color.Color(189, 183, 107)
        darkmagenta          = pygame.color.Color(139, 0, 139)
        darkolivegreen       = pygame.color.Color(85, 107, 47)
        darkorange           = pygame.color.Color(255, 140, 0)
        darkorchid           = pygame.color.Color(153, 50, 204)
        darkred              = pygame.color.Color(139, 0, 0)
        darksalmon           = pygame.color.Color(233, 150, 122)
        darkseagreen         = pygame.color.Color(143, 188, 143)
        darkslateblue        = pygame.color.Color(72, 61, 139)
        darkslategray        = pygame.color.Color(47, 79, 79)
        darkslategrey        = pygame.color.Color(47, 79, 79)
        darkturquoise        = pygame.color.Color(0, 206, 209)
        darkviolet           = pygame.color.Color(148, 0, 211)
        deeppink             = pygame.color.Color(255, 20, 147)
        deepskyblue          = pygame.color.Color(0, 191, 255)
        dimgray              = pygame.color.Color(105, 105, 105)
        dimgrey              = pygame.color.Color(105, 105, 105)
        dodgerblue           = pygame.color.Color(30, 144, 255)
        firebrick            = pygame.color.Color(178, 34, 34)
        floralwhite          = pygame.color.Color(255, 250, 240)
        forestgreen          = pygame.color.Color(34, 139, 34)
        fuchsia              = pygame.color.Color(255, 0, 255)
        gainsboro            = pygame.color.Color(220, 220, 220)
        ghostwhite           = pygame.color.Color(248, 248, 255)
        gold                 = pygame.color.Color(255, 215, 0)
        goldenrod            = pygame.color.Color(218, 165, 32)
        gray                 = pygame.color.Color(128, 128, 128)
        green                = pygame.color.Color(0, 128, 0)
        greenyellow          = pygame.color.Color(173, 255, 47)
        grey                 = pygame.color.Color(128, 128, 128)
        honeydew             = pygame.color.Color(240, 255, 240)
        hotpink              = pygame.color.Color(255, 105, 180)
        indianred            = pygame.color.Color(205, 92, 92)
        indigo               = pygame.color.Color(75, 0, 130)
        ivory                = pygame.color.Color(255, 255, 240)
        khaki                = pygame.color.Color(240, 230, 140)
        lavender             = pygame.color.Color(230, 230, 250)
        lavenderblush        = pygame.color.Color(255, 240, 245)
        lawngreen            = pygame.color.Color(124, 252, 0)
        lemonchiffon         = pygame.color.Color(255, 250, 205)
        lightblue            = pygame.color.Color(173, 216, 230)
        lightcoral           = pygame.color.Color(240, 128, 128)
        lightcyan            = pygame.color.Color(224, 255, 255)
        lightgoldenrodyellow = pygame.color.Color(250, 250, 210)
        lightgray            = pygame.color.Color(211, 211, 211)
        lightgreen           = pygame.color.Color(144, 238, 144)
        lightgrey            = pygame.color.Color(211, 211, 211)
        lightpink            = pygame.color.Color(255, 182, 193)
        lightsalmon          = pygame.color.Color(255, 160, 122)
        lightseagreen        = pygame.color.Color(32, 178, 170)
        lightskyblue         = pygame.color.Color(135, 206, 250)
        lightslategray       = pygame.color.Color(119, 136, 153)
        lightslategrey       = pygame.color.Color(119, 136, 153)
        lightsteelblue       = pygame.color.Color(176, 196, 222)
        lightyellow          = pygame.color.Color(255, 255, 224)
        lime                 = pygame.color.Color(0, 255, 0)
        limegreen            = pygame.color.Color(50, 205, 50)
        linen                = pygame.color.Color(250, 240, 230)
        magenta              = pygame.color.Color(255, 0, 255)
        maroon               = pygame.color.Color(128, 0, 0)
        mediumaquamarine     = pygame.color.Color(102, 205, 170)
        mediumblue           = pygame.color.Color(0, 0, 205)
        mediumorchid         = pygame.color.Color(186, 85, 211)
        mediumpurple         = pygame.color.Color(147, 112, 216)
        mediumseagreen       = pygame.color.Color(60, 179, 113)
        mediumslateblue      = pygame.color.Color(123, 104, 238)
        mediumspringgreen    = pygame.color.Color(0, 250, 154)
        mediumturquoise      = pygame.color.Color(72, 209, 204)
        mediumvioletred      = pygame.color.Color(199, 21, 133)
        midnightblue         = pygame.color.Color(25, 25, 112)
        mintcream            = pygame.color.Color(245, 255, 250)
        mistyrose            = pygame.color.Color(255, 228, 225)
        moccasin             = pygame.color.Color(255, 228, 181)
        navajowhite          = pygame.color.Color(255, 222, 173)
        navy                 = pygame.color.Color(0, 0, 128)
        oldlace              = pygame.color.Color(253, 245, 230)
        olive                = pygame.color.Color(128, 128, 0)
        olivedrab            = pygame.color.Color(107, 142, 35)
        orange               = pygame.color.Color(255, 165, 0)
        orangered            = pygame.color.Color(255, 69, 0)
        orchid               = pygame.color.Color(218, 112, 214)
        palegoldenrod        = pygame.color.Color(238, 232, 170)
        palegreen            = pygame.color.Color(152, 251, 152)
        paleturquoise        = pygame.color.Color(175, 238, 238)
        palevioletred        = pygame.color.Color(216, 112, 147)
        papayawhip           = pygame.color.Color(255, 239, 213)
        peachpuff            = pygame.color.Color(255, 218, 185)
        peru                 = pygame.color.Color(205, 133, 63)
        pink                 = pygame.color.Color(255, 192, 203)
        plum                 = pygame.color.Color(221, 160, 221)
        powderblue           = pygame.color.Color(176, 224, 230)
        purple               = pygame.color.Color(128, 0, 128)
        red                  = pygame.color.Color(255, 0, 0)
        rosybrown            = pygame.color.Color(188, 143, 143)
        royalblue            = pygame.color.Color(65, 105, 225)
        saddlebrown          = pygame.color.Color(139, 69, 19)
        salmon               = pygame.color.Color(250, 128, 114)
        sandybrown           = pygame.color.Color(244, 164, 96)
        seagreen             = pygame.color.Color(46, 139, 87)
        seashell             = pygame.color.Color(255, 245, 238)
        sienna               = pygame.color.Color(160, 82, 45)
        silver               = pygame.color.Color(192, 192, 192)
        skyblue              = pygame.color.Color(135, 206, 235)
        slateblue            = pygame.color.Color(106, 90, 205)
        slategray            = pygame.color.Color(112, 128, 144)
        slategrey            = pygame.color.Color(112, 128, 144)
        snow                 = pygame.color.Color(255, 250, 250)
        springgreen          = pygame.color.Color(0, 255, 127)
        steelblue            = pygame.color.Color(70, 130, 180)
        tan                  = pygame.color.Color(210, 180, 140)
        teal                 = pygame.color.Color(0, 128, 128)
        thistle              = pygame.color.Color(216, 191, 216)
        tomato               = pygame.color.Color(255, 99, 71)
        turquoise            = pygame.color.Color(64, 224, 208)
        violet               = pygame.color.Color(238, 130, 238)
        wheat                = pygame.color.Color(245, 222, 179)
        white                = pygame.color.Color(255, 255, 255)
        whitesmoke           = pygame.color.Color(245, 245, 245)
        yellow               = pygame.color.Color(255, 255, 0)
        yellowgreen          = pygame.color.Color(154, 205, 50)

class Rect(pygame.sprite.Sprite):
    """
    A class that rect-like pyggui classes inherit from. Can also be used on its own.

    Attributes:
        screen (pygame.surface.Surface): A pygame.surface.Surface object.

        fill (tuple[int, int, int] | pygame.color.Color): A color value.

        left (int): The x coord of the top left corner of the sprite.
        top (int): The y coord of the top left corner of the sprite.

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

        self.left = left
        self.top = top

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
                 color: tuple[int, int, int] | pygame.color.Color,):
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

    def update(self) -> None:
        self.font.render(self.text, True, self.color)
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

        left (int): The x coord of the top left corner of the sprite.
        top (int): The y coord of the top left corner of the sprite.

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
            if type(sprite) == Menu.Button:
                sprite.label.draw()

    def addEventListener(self, mousePos: tuple[int, int]) -> None:
        """
        Calls each child buttons onclick function.

        Args:
            mousePos (tuple[int, int]): The position of the mouse.
        """

        for button in self.buttons:
            if button.onclick is not None and button.rect.contains((*mousePos, 1, 1)):
                button.onclick()

    class Label(_Child, Label):
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
            _Child.__init__(self, parent)

            self.parent.labels.add(self)

        def centerToParent(self) -> None:
            """Center the object to the parents centerx."""

            self.rect.centerx = self.parent.rect.centerx

    class Button(_Child, Rect):
        """
        Renders a button to the screen.

        Attributes:
            parent (Menu): A Menu object.
            onclick (callable): A function.

            fill (tuple[int, int, int] | pygame.color.Color): The color of the background.

            left (int): The x coord of the top left corner of the sprite.
            top (int): The y coord of the top left corner of the sprite.

            screen (pygame.surface.Surface): A pygame.surface.Surface object.
        """

        def __init__(self, parent, *args,
                     onclick = None, text: str = "", font: pygame.font.Font = pygame.font.get_default_font(), textColor: tuple[int, int, int]|pygame.color.Color = Color.CSS3.white):
            """
            Class constructor.

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

            Rect.__init__(self, *args)
            _Child.__init__(self, parent)

            self.onclick = onclick
            if self.onclick is not None and not callable(onclick):
                raise TypeError(f"type of onclick must be callable, not {self.onclick.__class__.__name__}")

            # text
            self.text = text
            self.font = font
            self.textColor = textColor

            if self.font is None or type(self.font) != pygame.font.Font:
                raise TypeError(f"type of font should be pygame.font.Font, not {self.font.__class__.__name__}")
            else:
                self.labels = pygame.sprite.Group()

                self.label = Menu.Label(
                    self,
                    self.screen,
                    0, 0,
                    self.text,
                    self.font,
                    self.textColor
                )

                self.label.rect.center = self.rect.center

                self.label.draw()

            self.parent.buttons.add(self)

        def centerToParent(self) -> None:
            """Center the object to its parents centerx."""

            self.rect.centerx = self.parent.rect.centerx
            if self.label:
                self.label.rect.centerx = self.label.parent.rect.centerx

        def addEventListener(self, mousePos: tuple[int, int]) -> None:
            """
            Calls the objects onclick function.

            Args:
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