import tkinter as tk
import time
import random
from tkinter import font

# warna tema
BG_DARK    = "#3A1A4A"
BG_CARD    = "#6B2D6E"
ACCENT     = "#1a1a1a"
ACCENT_LT  = "#1A0A20"
TEXT_DARK  = "#F5A800"
TEXT_LIGHT = "#FFD966"
SCORE_BG   = "#ED0707"

CHOICES = ["rock", "paper", "scissors"]
EMOJIS  = {"rock": "✊", "paper": "🤚", "scissors": "✌"}

Countdown = 5

def determine_winner(player, computer):
    if player == computer:
        return "draw"
    wins = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"}
    return "player" if wins[player] == computer else "computer"

class RockPaperScissors(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rock/Paper/Scissors")
        self.configure(bg=BG_DARK)
        self.resizable(False, False)

        self.player_score  = 0
        self.computer_score = 0
        self.countdown_id  = None
        self.time_left     = Countdown
        self.game_active   = True

        self._build_font()
        self._build_ui()
        self._start_countdown()

    # font
    def _build_font(self):
        self.font_title   = font.Font(family="Georgia", size=22, weight="bold")
        self.font_score   = font.Font(family="Georgia", size=13, weight="bold")
        self.font_emoji   = font.Font(family="Segoe UI Emoji", size=35)
        self.font_status  = font.Font(family="Georgia", size=12, slant="italic")
        self.font_timer   = font.Font(family="Georgia", size=13, weight="bold")
        self.font_btn     = font.Font(family="Georgia", size=12, weight="bold")
        self.font_sub     = font.Font(family="Georgia", size=10, slant="italic")

    # build UI
    def _build_ui(self):
        tk.Label(self, text="Rock  Paper  Scissors",
                 font=self.font_title, bg=BG_DARK, fg=TEXT_LIGHT,
                 pady=18).pack()

        # Card
        self.card = tk.Frame(self, bg=BG_CARD, bd=0,
                             padx=30, pady=24)
        self.card.pack(padx=30, pady=(0, 20))

        # Score row
        score_row = tk.Frame(self.card, bg=BG_CARD)
        score_row.pack(pady=(0, 18))

        self.lbl_pscore = self._score_badge(score_row, "Player: 0")
        self.lbl_pscore.pack(side="left", padx=8)
        self.lbl_cscore = self._score_badge(score_row, "Computer: 0")
        self.lbl_cscore.pack(side="left", padx=8)

        # choice buttons
        btn_row = tk.Frame(self.card, bg=BG_CARD)
        btn_row.pack()
        self.choice_btns = []
        for choice in CHOICES:
            btn = tk.Button(btn_row,
                            text=EMOJIS[choice],
                            font=self.font_emoji,
                            width=3, height=1,
                            bg=TEXT_LIGHT,
                            fg=ACCENT,
                            activebackground=ACCENT,
                            activeforeground=TEXT_LIGHT,
                            relief="solid", bd=2,
                            cursor="hand2",
                            command=lambda c=choice: self._player_choose(c))
            btn.pack(side="left", padx=10, pady=10)
            self.choice_btns.append(btn)

        # Status & Timer
        self.lbl_status = tk.Label(self.card,
                                   text="Choose your weapon!",
                                   font=self.font_status,
                                   bg=BG_CARD, fg=ACCENT,
                                   pady=2)
        self.lbl_status.pack()

        self.lbl_timer = tk.Label(self.card,
                                  text=f"Time left: {Countdown}s",
                                  font=self.font_timer,
                                  bg=BG_CARD, fg=ACCENT)
        self.lbl_timer.pack(pady=(0, 10))

        # play again
        self.btn_again = tk.Button(self.card,
                                   text="Play Again",
                                   font=self.font_btn,
                                   bg=ACCENT, fg=TEXT_LIGHT,
                                   activebackground=ACCENT_LT,
                                   activeforeground=TEXT_LIGHT,
                                   relief="flat", padx=20, pady=8,
                                   cursor="hand2",
                                   command=self._reset_round)
        self.btn_again.pack(pady=(4, 4))

        # sub-caption
        tk.Label(self, text="concepts learned: conditionals, randomness and program logic",
                 font=self.font_sub,
                 bg=BG_DARK, fg="#aaaacc",
                 wraplength=400, justify="center",
                 pady=10).pack()

    def _score_badge(self, parent, text):
        lbl = tk.Label(parent, text=text,
                       font=self.font_score,
                       bg=SCORE_BG, fg=ACCENT,
                       padx=12, pady=4,
                       relief="solid", bd=1)
        return lbl

    # countdown
    def _start_countdown(self):
        self.time_left = Countdown
        self.game_active = True
        self._tick()

    def _tick(self):
        if not self.game_active:
            return
        self.lbl_timer.config(text=f"Time left: {self.time_left}s")
        if self.time_left <= 0:
            self._time_up()
            return
        self.time_left -= 1
        self.countdown_id = self.after(1000, self._tick)

    def _time_up(self):
        self.game_active = False
        self._disable_buttons()
        # computer win
        comp = random.choice(CHOICES)
        self.computer_score += 1
        self._update_scores()
        self.lbl_status.config(
            text=f"Time's up! computer chose {EMOJIS[comp]}  —  computer win!")
        self.lbl_timer.config(text="Time left: 0s")

    # player choice
    def _player_choose(self, choice):
        if not self.game_active:
            return
        self.game_active = False
        if self.countdown_id:
            self.after_cancel(self.countdown_id)
        self._disable_buttons()

        comp = random.choice(CHOICES)
        result = determine_winner(choice, comp)

        if result == "player":
            self.player_score += 1
            msg = f"You chose {EMOJIS[choice]}  ·  Computer chose {EMOJIS[comp]}  → You Win!"
        elif result == "computer":
            self.computer_score += 1
            msg = f"You chose {EMOJIS[choice]}  ·  Computer chose {EMOJIS[comp]}  → Computer win!"
        else:
            msg = f"You chose {EMOJIS[choice]}  ·  Computer chose {EMOJIS[comp]}  → It's a Draw!"

        self._update_scores()
        self.lbl_status.config(text=msg)
        self.lbl_timer.config(text="—")

    # helper
    def _disable_buttons(self):
        for btn in self.choice_btns:
            btn.config(state="disabled",
                       bg="#cccccc", fg="#888888")

    def _enable_buttons(self):
        for btn in self.choice_btns:
            btn.config(state="normal",
                       bg=TEXT_LIGHT, fg=ACCENT)

    def _update_scores(self):
        self.lbl_pscore.config(text=f"Player: {self.player_score}")
        self.lbl_cscore.config(text=f"Computer: {self.computer_score}")

    def _reset_round(self):
        if self.countdown_id:
            self.after_cancel(self.countdown_id)
        self._enable_buttons()
        self.lbl_status.config(text="Choose your weapon!")
        self.lbl_timer.config(text=f"Time left: {Countdown}s")
        self._start_countdown()


if __name__ == "__main__":
    app = RockPaperScissors()
    app.mainloop()