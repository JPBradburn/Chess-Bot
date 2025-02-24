import pygame
import sys
import two_player_game
import play_as_white_vs_ai
import play_as_black_vs_ai


class ChessGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 640))  # Adjust window size for menu
        pygame.display.set_caption('Chess Game')
        self.clock = pygame.time.Clock()
        self.running = True
        self.mode = None
        self.font = pygame.font.SysFont('dejavusans', 36)

    def draw_menu(self):
        """Draw the initial game menu."""
        self.screen.fill((0, 0, 0))  # Black background

        options = [
            "1. Two Player Mode",
            "2. Play as White vs AI",
            "3. Play as Black vs AI"
        ]

        self.buttons = []  # Store button hitboxes
        for i, option in enumerate(options):
            text = self.font.render(option, True, (255, 255, 255))
            rect = text.get_rect(topleft=(100, 100 + i * 50))
            self.screen.blit(text, rect.topleft)
            self.buttons.append(rect)  # Store the clickable area for each option

        pygame.display.flip()

    def menu(self):
        """Handle menu interactions to select game mode."""
        while self.running:
            self.draw_menu()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    for i, rect in enumerate(self.buttons):
                        if rect.collidepoint(x, y):  # Check if click is inside a button
                            self.mode = ["two_player", "white_vs_ai", "black_vs_ai"][i]
                            return

    def run(self):
        """Start the game based on the selected mode."""
        self.menu()

        if self.mode == "two_player":
            print("Starting Two Player Mode...")
            two_player_game.main()
            pygame.quit()
            sys.exit()
        elif self.mode == "white_vs_ai":
            print("Playing as white vs ai")
            play_as_white_vs_ai.main()
            pygame.quit()
            sys.exit()
        elif self.mode == "black_vs_ai":
            print("Playing as black vs ai")
            play_as_black_vs_ai.main()
            pygame.quit()
            sys.exit()


def main():
    game = ChessGame()
    game.run()


if __name__ == "__main__":
    main()
