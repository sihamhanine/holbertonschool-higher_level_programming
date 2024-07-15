def generate_invitations(template, attendees):
    import os
    
    # Vérifier les types d'entrée
    if not isinstance(template, str):
        print("Erreur : Le modèle n'est pas une chaîne de caractères.")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Erreur : Les participants ne sont pas une liste de dictionnaires.")
        return
    
    # Gérer les entrées vides
    if not template.strip():
        print("Erreur : Le modèle est vide, aucun fichier de sortie généré.")
        return
    if not attendees:
        print("Erreur : Aucune donnée fournie, aucun fichier de sortie généré.")
        return

    # Traiter chaque participant
    for idx, attendee in enumerate(attendees):
        processed_template = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key, "N/A")
            if value is None:
                value = "N/A"
            processed_template = processed_template.replace(f"{{{key}}}", value)
        
        # Générer le fichier de sortie
        output_filename = f"output_{idx + 1}.txt"
        with open(output_filename, 'w') as output_file:
            output_file.write(processed_template)
        print(f"Fichier généré : {output_filename}")

# Exemple d'utilisation
if __name__ == "__main__":
    # Lire le modèle à partir d'un fichier
    with open('template.txt', 'r') as file:
        template_content = file.read()

    # Liste des participants
    attendees = [
        {"name": "Alice", "event_title": "Conférence Python", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Atelier Data Science", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "Sommet AI", "event_date": None, "event_location": "Boston"}
    ]

    # Appeler la fonction avec le modèle et la liste des participants
    generate_invitations(template_content, attendees)