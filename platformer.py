import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = 'platformer'

class Platformer(arcade.Window):
    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        pass

    def on_draw(self):
        """Render the screen."""

        self.clear()
        # Code to draw the screen goes here

def main():
    window = Platformer()
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()
