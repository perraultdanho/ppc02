import tkinter as tk
import random

# Initialiser la fenêtre de jeu
window = tk.Tk()
window.title("Jeu Pierre, Papier, Ciseaux")
window.geometry("400x350")  # Définir les dimensions de la fenêtre
window.config(bg="lightblue")  # Définir la couleur d'arrière-plan

# Créer une étiquette pour le titre du jeu
title_label = tk.Label(window, text="Pierre, Papier, Ciseaux", font=("Helvetica", 16), bg="lightblue")
title_label.pack(pady=20)

# Créer une étiquette pour inviter l'utilisateur à faire un choix
prompt_label = tk.Label(window, text="Choisissez Pierre, Papier ou Ciseaux :", font=("Helvetica", 12), bg="lightblue")
prompt_label.pack()

# Créer un champ de saisie pour que l'utilisateur entre son choix
user_choice = tk.Entry(window, font=("Helvetica", 12))
user_choice.pack(pady=10)

# Créer un label pour afficher les résultats
result_label = tk.Label(window, text="", font=("Helvetica", 12), bg="lightblue")
result_label.pack()

# Fonction pour générer le choix de l'ordinateur
def generate_computer_choice():
    choices = ["pierre", "papier", "ciseaux"]
    return random.choice(choices)

# Fonction pour gérer la logique du jeu
def play():
    user_pick = user_choice.get().lower()  # Récupérer le choix de l'utilisateur et le convertir en minuscule
    if user_pick not in ["pierre", "papier", "ciseaux"]:
        result_label.config(text="Choix invalide ! Veuillez entrer pierre, papier ou ciseaux.")
        return
    
    comp_pick = generate_computer_choice()  # Générer le choix de l'ordinateur
    
    # Déterminer le résultat du jeu
    result_text = f"Votre choix : {user_pick}\nChoix de l'ordinateur : {comp_pick}\n"
    
    if user_pick == comp_pick:
        result_text += "Match nul !"
    elif (user_pick == "pierre" and comp_pick == "ciseaux") or \
         (user_pick == "papier" and comp_pick == "pierre") or \
         (user_pick == "ciseaux" and comp_pick == "papier"):
        result_text += "Vous avez gagné !"
    else:
        result_text += "L'ordinateur a gagné !"
    
    # Afficher le résultat
    result_label.config(text=result_text)

# Fonction pour réinitialiser le jeu
def reset():
    user_choice.delete(0, tk.END)  # Effacer le champ de saisie
    result_label.config(text="")  # Effacer le résultat

# Fonction pour quitter l'application
def exit_game():
    window.quit()  # Fermer la fenêtre de jeu

# Créer un bouton pour lancer le jeu
play_button = tk.Button(window, text="Jouer", font=("Helvetica", 12), command=play)
play_button.pack(pady=10)

# Créer un bouton pour réinitialiser le jeu
reset_button = tk.Button(window, text="Réinitialiser", font=("Helvetica", 12), command=reset)
reset_button.pack(pady=10)

# Créer un bouton pour quitter l'application
exit_button = tk.Button(window, text="Quitter", font=("Helvetica", 12), command=exit_game)
exit_button.pack(pady=10)

# Lancer la boucle principale de l'application
window.mainloop()
