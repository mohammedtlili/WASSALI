from models.input_model import Transport, Marchandise, Categorie


def calcul(request_input: Transport) -> Marchandise:
    # prix = 0
    prix = request_input.temps_service * request_input.nmbre_km
    prix_min = prix
    if request_input.categorie == Categorie.utilitaire:
        prix = (0.14435 * request_input.nmbre_km)+(request_input.temps_service*3.7)+((request_input.temps_service* 119.3) / 8.43)
        prix_min = (0.14435 * request_input.nmbre_km)+(request_input.temps_service*3.7)+((request_input.temps_service* 87.96) / 8.43)

    elif (request_input.categorie == Categorie.fourgon) or (request_input.categorie == Categorie.camionette):
        prix = (0.23005 * request_input.nmbre_km)+(request_input.temps_service*3.7)+((request_input.temps_service* 201.03) / 8.43)
        prix_min = (0.23005 * request_input.nmbre_km)+(request_input.temps_service*3.7)+((request_input.temps_service* 138.35) / 8.43)

    elif (request_input.categorie == Categorie.porteur):
        prix = (0.28505 * request_input.nmbre_km)+(request_input.temps_service*3.7)+((request_input.temps_service* 214.16) / 8.43)
        prix_min = (0.28505 * request_input.nmbre_km)+(request_input.temps_service*3.7)+((request_input.temps_service* 182.72) / 8.43)

    else:
        print("choix invalide")

    interval_prix = Marchandise(prix_min=prix_min, prix_max=prix)

    return interval_prix

