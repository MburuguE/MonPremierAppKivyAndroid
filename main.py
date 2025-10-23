# main.py

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class BonjourApp(App):
    def build(self):
        # Création du conteneur principal (vertical)
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        # 1. Champ de saisie pour le nom
        self.nom_input = TextInput(
            hint_text="Entrez votre nom ici",
            multiline=False,
            size_hint=(1, 0.2)
        )
        self.layout.add_widget(self.nom_input)

        # 2. Bouton pour afficher le message
        self.bouton_saluer = Button(
            text="Saluer",
            size_hint=(1, 0.2)
        )
        # Assigner la fonction 'saluer' au clic du bouton
        self.bouton_saluer.bind(on_press=self.saluer)
        self.layout.add_widget(self.bouton_saluer)

        # 3. Étiquette pour afficher le message de bienvenue
        self.message_label = Label(
            text="Veuillez entrer votre nom.",
            font_size='20sp',
            size_hint=(1, 0.6)
        )
        self.layout.add_widget(self.message_label)

        return self.layout

    def saluer(self, instance):
        """
        Fonction appelée lors du clic sur le bouton.
        Récupère le nom et met à jour l'étiquette.
        """
        nom = self.nom_input.text.strip() # Récupère le texte et supprime les espaces
        
        if nom:
            # Met à jour le texte de l'étiquette avec le message de bienvenue
            self.message_label.text = f"Bonjour, {nom} ! Bienvenue sur l'application Kivy."
        else:
            # Message d'erreur si le champ est vide
            self.message_label.text = "Veuillez entrer un nom valide s'il vous plaît."

if __name__ == '__main__':
    BonjourApp().run()
