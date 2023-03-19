import tkinter as tk
from characters import Warrior, Hunter, Mage, Healer
from game_functions import create_team, create_wave, is_wave_defeated, is_team_defeated, play_round
from upgrade_save_load import upgrade_phase, save_game, load_game

class GameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Heroes vs Villains")
        self.geometry("400x200")

        self.team = create_team()
        self.wave_num = 1
        self.wave = create_wave(self.wave_num)

        self.start_button = tk.Button(self, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=10)

        self.load_button = tk.Button(self, text="Load Game", command=self.load_saved_game)
        self.load_button.pack(pady=10)

    def start_game(self):
        for hero_name in self.team:
            name = input(f"Enter a name for your {hero_name.capitalize()}: ")
            self.team[hero_name].name = name

        self.play_game()

    def load_saved_game(self):
        self.team, self.wave_num = load_game()
        self.wave = create_wave(self.wave_num)
        self.play_game()

    def play_game(self):
        while self.wave_num < 5 and not is_team_defeated(self.team):
            self.play_wave()
            if not is_wave_defeated(self.wave):
                break

            if self.wave_num < 4:
                upgrade_phase(self.team)

            self.wave_num += 1
            self.wave = create_wave(self.wave_num)

        if is_team_defeated(self.team):
            print("The team has been defeated!")
        elif self.wave_num == 5 and is_wave_defeated(self.wave):
            print("Congratulations! The team has defeated the dragon and won the game!")

    def play_wave(self):
        print(f"Wave {self.wave_num} begins: {[v.name for v in self.wave]}")

        while not is_wave_defeated(self.wave) and not is_team_defeated(self.team):
            play_round(self.team, self.wave)
            save_game(self.team, self.wave_num)

if __name__ == "__main__":
    app = GameApp()
    app.mainloop()
