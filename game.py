from hero import Hero, Player, Computer


class Game:
    def __init__(self, player: Hero, computer: Hero):
        self.player = player
        self.computer = computer

    def start(self):
        print("Игра началась!")
        while self.player.is_alive() and self.computer.is_alive():
            self.player_turn()
            if not self.computer.is_alive():
                print(f"{self.computer.get_name()} проиграл!")
                break

            self.computer_turn()
            if not self.player.is_alive():
                print(f"{self.player.get_name()} проиграл!")
                break

    def player_turn(self):
        self.player.attack(self.computer)
        print(f"{self.computer.get_name()} осталось здоровья: {self.computer.get_health()}")

    def computer_turn(self):
        self.computer.attack(self.player)
        print(f"{self.player.get_name()} осталось здоровья: {self.player.get_health()}")


if __name__ == '__main__':
    player_hero = Player("Игрок")
    computer_hero = Computer("Компьютер")
    game = Game(player_hero, computer_hero)
    game.start()