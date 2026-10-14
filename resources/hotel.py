from flask_restful import Resource

lista_hoteis = [
    { "hotel_id": "sky", "nome": "Hotel Sky", "estrelas": 4.8, "diaria": 195.99, "cidade": "Porto"},
    { "hotel_id": "mitras", "nome": "Mitras Hotel", "estrelas": 5, "diaria": 299.99, "cidade": "Lisboa"},
    { "hotel_id": "granja", "nome": "Granja Kids", "estrelas": 4.1, "diaria": 99.99, "cidade": "Famalicão"}
]

class Hoteis(Resource):
    def get(self):
        return { "hoteis": lista_hoteis }