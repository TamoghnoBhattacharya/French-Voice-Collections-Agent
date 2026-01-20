def opening_line(preset):
    style = preset["opening_style"]
    brand = preset["brand_name"]

    if style == "direct":
        return f"Bonjour, je vous appelle de la part de {brand}."
    if style == "formal":
        return f"Bonjour, ici le {preset['signature']}."
    return f"Bonjour, je me permets de vous appeler concernant {brand}."

def identification():
    return (
        "Pour des raisons de confidentialité, puis-je confirmer "
        "que je parle bien à la bonne personne ?"
    )

def context():
    return (
        "Je vous appelle au sujet d’un dossier administratif concernant "
        "un paiement en attente. Rien d’urgent."
    )

def payment_offer():
    return (
        "Souhaitez-vous que je vous envoie un lien de paiement sécurisé, "
        "ou préférez-vous que nous planifiions un rappel ?"
    )

def robot_answer(preset):
    return (
        "Je suis un assistant dédié à la gestion de ce dossier, "
        "formé pour vous répondre clairement et avec respect."
        + (
            " Si vous le souhaitez, je peux aussi organiser un échange "
            "avec un conseiller."
            if preset.get("offer_handoff", False)
            else ""
        )
    )

def deescalation():
    return (
        "Je comprends. Mon intention est simplement de vous informer, "
        "sans aucune pression."
    )

def closing():
    return "Merci pour votre temps. Je vous souhaite une excellente journée."
