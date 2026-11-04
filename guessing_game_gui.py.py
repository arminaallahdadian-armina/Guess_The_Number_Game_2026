import tkinter as tk
import random


# Main Window

window = tk.Tk()
window.title("Guess The Number 🎀")
window.state("zoomed")
window.configure(bg="#F3E8FF")
window.resizable(True, True)

# Game Variables

secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 5


# Main Card


card = tk.Frame(
    window,
    bg="white",
    padx=30,
    pady=25
)
card.pack(padx=40, pady=35, fill="both", expand=True)

# Game Title

title = tk.Label(
    card,
    text="GUESS THE NUMBER 🎀",
    font=("Segoe UI", 26, "bold"),
    bg="white",
    fg="#A855F7"
)
title.pack(pady=(35, 20))

# =========================
# Welcome Message
# =========================

welcome = tk.Label(
    card,
    text="Let's see how lucky you are! 💗",
    font=("Segoe UI", 15),
    bg="white",
    fg="#777777"
)
welcome.pack(pady=10)

# =========================
# Game Instructions
# =========================

instructions = tk.Label(
    card,
    text="Guess a number between 1 and 100",
    font=("Segoe UI", 14),
    bg="white",
    fg="#555555"
)
instructions.pack(pady=25)

# =========================
# Hearts Section
# =========================

heart_frame = tk.Frame(card, bg="white")
heart_frame.pack(pady=20)

hearts = []

for i in range(5):
    heart = tk.Label(
        heart_frame,
        text="💗",
        font=("Segoe UI Emoji", 32),
        bg="white"
    )
    heart.pack(side="left", padx=12)
    hearts.append(heart)

# =========================
# Number Entry
# =========================

number_entry = tk.Entry(
    card,
    font=("Segoe UI", 22),
    justify="center",
    width=15,
    bg="#FFF0F6",
    fg="#A855F7",
    relief="flat"
)
number_entry.pack(pady=25)

# =========================
# Feedback Message
# =========================

feedback = tk.Label(
    card,
    text="Good luck! You've got this! 🌸",
    font=("Segoe UI", 15, "bold"),
    bg="white",
    fg="#A855F7",
    wraplength=700
)
feedback.pack(pady=25)

# =========================
# Remaining Chances
# =========================

chances_label = tk.Label(
    card,
    text="5 chances remaining",
    font=("Segoe UI", 13),
    bg="white",
    fg="#888888"
)
chances_label.pack(pady=10)

# =========================
# Rank Message
# =========================

rank_label = tk.Label(
    card,
    text="",
    font=("Segoe UI", 16, "bold"),
    bg="white",
    fg="#A855F7"
)
rank_label.pack(pady=5)
# Emoji Rain Animation

def emoji_rain():
    emojis = ["🎉", "💗", "🌸", "✨", "🥳", "💜"]

    def create_emoji():
        emoji = tk.Label(
            window,
            text=random.choice(emojis),
            font=("Segoe UI Emoji", 24),
            bg="#F3E8FF"
        )

        x = random.randint(
            20,
            max(20, window.winfo_width() - 50)
        )

        emoji.place(x=x, y=-40)

        def fall():
            y = emoji.winfo_y()

            if y < window.winfo_height():
                emoji.place(y=y + 8)
                window.after(35, fall)
            else:
                emoji.destroy()

        fall()

    for i in range(25):
        window.after(i * 150, create_emoji)

# =========================
# Check Guess Function
# =========================

def check_guess():
    global attempts

    user_input = number_entry.get().strip()

    if not user_input.isdigit():
        feedback.config(
            text="Oops! Please enter a valid number! 💗",
            fg="#E879A5"
        )
        return

    guess = int(user_input)

    if guess < 1 or guess > 100:
        feedback.config(
            text="Please enter a number between 1 and 100!",
            fg="#E879A5"
        )
        return

    attempts += 1
    number_entry.delete(0, tk.END)

    # Winning Condition

    if guess == secret_number:

        ranks = {
            1: "Excellent! 🌟",
            2: "Very Good! 💖",
            3: "Good! 🌸",
            4: "Acceptable! ✨",
            5: "Lucky Winner! 🍀"
        }

        feedback.config(
            text="YOU DID IT! Congratulations! 🎉🥳",
            fg="#A855F7"
        )

        chances_label.config(
            text="You won the game!"
        )

        rank_label.config(
            text=f"Your Rank: {ranks[attempts]}"
        )

        guess_button.config(state="disabled")
        number_entry.config(state="disabled")

        emoji_rain()
        return

    # Wrong Guess

    hearts[attempts - 1].config(
        text="♡",
        fg="#D8B4E2"
    )

    remaining = max_attempts - attempts

    chances_label.config(
        text=f"{remaining} chances remaining"
    )

    difference = abs(secret_number - guess)

    if guess > secret_number:
        direction = "Try a smaller number! ⬇️"
    else:
        direction = "Try a bigger number! ⬆️"

    if difference <= 5:
        message = f"{direction}\nSO CLOSE! You're almost there! 💗"
    elif difference <= 15:
        message = f"{direction}\nYou're getting closer! 🌸"
    else:
        message = f"{direction}\nToo far! Keep trying! 🥺"

    feedback.config(
        text=message,
        fg="#A855F7"
    )

    # Losing Condition

    if attempts == max_attempts:

        feedback.config(
            text=f"GAME OVER! The number was {secret_number} 💔",
            fg="#E879A5"
        )

        chances_label.config(
            text="No chances remaining!"
        )

        guess_button.config(state="disabled")
        number_entry.config(state="disabled")

# Restart Game Function

def restart_game():
    global secret_number, attempts

    secret_number = random.randint(1, 100)
    attempts = 0

    for heart in hearts:
        heart.config(text="💗", fg="#A855F7")

    feedback.config(
        text="Good luck! You've got this! 🌸",
        fg="#A855F7"
    )

    chances_label.config(text="5 chances remaining")
    rank_label.config(text="")

    guess_button.config(state="normal")
    number_entry.config(state="normal")
    number_entry.delete(0, tk.END)
    number_entry.focus()

# Guess Button

guess_button = tk.Button(
    card,
    text="GUESS ✨",
    font=("Segoe UI", 16, "bold"),
    bg="#E9A8D4",
    fg="white",
    activebackground="#D88BC0",
    relief="flat",
    width=20,
    height=2,
    cursor="hand2",
    command=check_guess
)
guess_button.pack(pady=15)

 # Play Again Button

again_button = tk.Button(
    card,
    text="PLAY AGAIN 🔄",
    font=("Segoe UI", 14, "bold"),
    bg="#C4B5FD",
    fg="white",
    relief="flat",
    width=20,
    height=2,
    cursor="hand2",
    command=restart_game
)
again_button.place(x=30, y=35)

# Enter Key Support

number_entry.bind(
    "<Return>",
    lambda event: check_guess()
)

# =========================
# Run Game
# =========================

number_entry.focus()

window.mainloop()