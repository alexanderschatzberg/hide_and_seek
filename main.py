import arcade 

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 5


class MyGame(arcade.Window):

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.csscolor.GREY)
        self.wall_list = None
        self.player_list = None
        self.physics_engine = None

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Set up both sprites and their starting positions
        self.red_sprite = arcade.Sprite("static/redSprite.png", 0.1)
        self.green_sprite = arcade.Sprite("static/greenSprite.png", 0.1)

        self.red_sprite.center_x = (SCREEN_WIDTH / 2) + 100
        self.red_sprite.center_y = (SCREEN_HEIGHT / 2)
        self.green_sprite.center_x = (SCREEN_WIDTH / 2) - 100
        self.green_sprite.center_y = (SCREEN_HEIGHT / 2) 

        self.player_list.append(self.red_sprite)
        self.player_list.append(self.green_sprite)
        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEngineSimple(self.red_sprite, self.wall_list)

        self.player_sprite = self.red_sprite

    def on_draw(self):
        """Render the screen."""

        self.clear()
        # Code to draw the screen goes here
        self.player_list.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y += PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y -= PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x -= PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x += PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y -= PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y += PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x += PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x -= PLAYER_MOVEMENT_SPEED

    def on_update(self, delta_time):
        """Movement and game logic"""

        # Move the player with the physics engine
        self.physics_engine.update()


def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
