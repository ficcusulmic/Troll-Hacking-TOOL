import tkinter as tk
from tkinter import messagebox, filedialog
import webbrowser
import random
import subprocess

def generate_userpass():
  username = input("Enter username: ")
  password_length = 10
  chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_-+=<>?"
  password = ''.join(random.choice(chars) for _ in range(password_length))
  messagebox.showinfo("Bruteforced", f"{username}\nPassword: {password}")

def take_down_nullforums():
  actions = [
    "Getting ready...",
    "Trying to bruteforce the cheese...",
    "Hacking into the mainframe...",
    "Searching for the secret backdoor...",
    "Deploying the rubber duck army...",
    "Unleashing the infinite monkeys with typewriters...",
    "Initiating the dance-off protocol...",
    "Summoning the ghost of ancient memes...",
    "The nf fox ate our pings, :( , aborading mission"
  ]

  for action in actions:
    if "The nf fox ate our pings, :( , aborading mission" in action:
      messagebox.showerror("Action", action)
    else:
      messagebox.showinfo("Action", action)

def quiz():
  questions = {
    "What tool do we use to null plugins?": "Recaf",
    "What is the first thing we look for? 1. API and Links 2. Plugin Version": "1",
    "What is the spigot API identifiers? 1. %%__USER__%% 2. %%__CLIENT__%%": "1"
  }

  score = 0
  total_questions = len(questions)

  for question, correct_answer in questions.items():
    user_answer = input(question + " ")
    if user_answer.lower() == correct_answer.lower():
      score += 1

  messagebox.showinfo("Quiz Result", f"You scored {score} out of {total_questions}.")

def rent_a_hitman():
  webbrowser.open_new("https://rentahitman.com")
app = tk.Tk()
app.title("Realzz Hacking tool by Ennthy")

def handle_choice(choice):
  if choice == 1:
    generate_userpass()
  elif choice == 2:
    webbrowser.open_new_tab("https://r.mtdv.me/giveaways/nullforumsgift")
  elif choice == 3:
    take_down_nullforums()
  elif choice == 4:
    quiz()
  else:
    messagebox.showerror("Error", "Invalid choice. Select 1, 2, 3, or 4.")

def activate_infinity_mode():
  subprocess.Popen(["gnome-terminal", "--", "sh", "-c", "printf '\e[92m'; while :; do echo -ne \"-\"; sleep 0.1; done"])

# GUI elements
menu_label = tk.Label(app, text="Select an option:")
menu_label.pack()

button1 = tk.Button(app, text="Break Nullforums Account", command=lambda: handle_choice(1))
button1.pack()

button2 = tk.Button(app, text="Free NullForums Premium", command=lambda: handle_choice(2))
button2.pack()

button3 = tk.Button(app, text="Take Down Nullforums", command=lambda: handle_choice(3))
button3.pack()

button4 = tk.Button(app, text="Real mens quiz", command=lambda: handle_choice(4))
button4.pack()

# Additional buttons
button5 = tk.Button(app, text="Activate Infinity Mode", command=activate_infinity_mode)
button5.pack()

button6 = tk.Button(app, text="Summon the Code Wizard", command=lambda: messagebox.showinfo("Code Wizard", "The Code Wizard has been summoned!"))
button6.pack()

button7 = tk.Button(app, text="Hack the Matrix", command=lambda: messagebox.showinfo("Matrix", "You have entered the Matrix!"))
button7.pack()

button8 = tk.Button(app, text="Unleash the Cyber Dragons", command=lambda: messagebox.showinfo("Cyber Dragons", "The Cyber Dragons are on the loose!"))
button8.pack()

button9 = tk.Button(app, text="Rent a hitman", command=rent_a_hitman)
button9.pack()

# EULA button and text
def show_eula():
  eula_text = """
  End User License Agreement (EULA):
  By using this application, you agree to be bound by the terms of this agreement.
  Please review the terms carefully before using the application.
  """
  messagebox.showinfo("EULA", eula_text)

eula_button = tk.Button(app, text="EULA", command=show_eula)
eula_button.pack()

def show_eula_download():
  eula_text = """
  Nonexistent License Grant:
You are granted a nontransferable, nonexclusive, and non-existent license to not use The Nullforums Tool on an imaginary device that doesn’t exist. This license is valid for the duration of your next daydream or until the next cosmic alignment, whichever comes first.
Non-Usage Restrictions:
You shall not not use The Nullforums Tool for any purpose, including but not limited to:
Not time travel (unless you bring snacks for the dinosaurs).
Not communicating with intergalactic beings (unless they know a good pizza joint in the Andromeda Galaxy).
Not solving quadratic equations (because they’re just too square).
Not achieving enlightenment (unless it involves disco balls and glitter).
Nonexistent Support and Updates:
We promise to provide absolutely no support, updates, or bug fixes for The Nullforums Tool. If you encounter any issues, please consult your imaginary friend or a parallel universe version of yourself.
Non-Warranty Disclaimer:
The Nullforums Tool comes with no warranties, express or implied. We disclaim any responsibility for:
Existential crises caused by contemplating the void (please consult your local existential therapist).
Spontaneous combustion while not using The Nullforums Tool (please consult your local fire department, even though they won’t find any fire).
Accidental summoning of eldritch beings (we recommend offering them a cup of imaginary tea).
Non-Indemnification:
You agree to not hold us harmless from any imaginary lawsuits, astral disputes, or cosmic misunderstandings related to The Nullforums Tool. In the event of a legal battle, we will send our top imaginary lawyer (who specializes in unicorn law and interdimensional paperwork).
Non-Transferability:
You may not not transfer The Nullforums Tool to anyone else, unless they can prove they’ve mastered the art of levitating marshmallows while juggling invisible flamingos.
Non-Choice of Law and Venue:
This EULA is governed by the laws of the Nonsensical Dimension, where gravity wears polka dots and logic takes coffee breaks. Any disputes shall be resolved in the Court of Cosmic Absurdity, presided over by Judge Quirkington the Third.
Non-Contact Information:
For nonexistent customer support, please send a telepathic message to the void. We’ll get back to you in approximately never (or sooner, depending on the alignment of celestial rubber ducks).
By not clicking the imaginary “Accept” button below (which doesn’t exist), you acknowledge that you’ve not read and not understood this EULA (even though it’s gibberish) and agree to not abide by its imaginary terms (which are subject to change during solar eclipses, lunar disco parties, and spontaneous interpretive dances by quasars).
  """

  file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[("Text files", "*.txt")])
  with open(file_path, 'w') as file:
    file.write(eula_text)

download_eula_button = tk.Button(app, text="DOWNLOAD EULA", command=show_eula_download)
download_eula_button.pack()

app.mainloop()
