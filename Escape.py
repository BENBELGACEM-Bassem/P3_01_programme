#! Escape_game/project_env/bin/python
# coding: utf-8
# Head module of the game to launch and quit

import game

# Create a game instance
Escape = game.Game()
# launch the game and quit if the player quits
Escape.main()
game.ch.st.pygame.quit()
quit()
