from flask_restful import Resource, reqparse

lista_hoteis = [
    { "hotel_id": "sky", "nome": "Hotel Sky", "estrelas": 4.8, "diaria": 195.99, "cidade": "Porto"},
    { "hotel_id": "mitras", "nome": "Mitras Hotel", "estrelas": 5, "diaria": 299.99, "cidade": "Lisboa"},
    { "hotel_id": "granja", "nome": "Granja Kids", "estrelas": 4.1, "diaria": 99.99, "cidade": "Famalicão"}
]

class Hoteis(Resource):
    def get(self):
        return { "hoteis": lista_hoteis }

class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("nome", type=str, required=True, help="Nome obrigatório")
    argumentos.add_argument("estrelas", type=float, required=True, help="Estrelas obrigatórip")
    argumentos.add_argument("diaria", type=float, required=True, help="Diária obrigatório")
    argumentos.add_argument("cidade", type=str, required=True, help="Cidade obrigatório")

    def get(self, id_hotel):
        for hotel in lista_hoteis:
             if hotel["hotel_id"] == id_hotel:
                  return hotel, 200
        return {"message": "Hotel not found"}

    def post(self, id_hotel):
        dados = Hotel.argumentos.parse_args() # Dicionário
        for hotel in lista_hoteis:
             if hotel["hotel_id"] == id_hotel:
                  return {"message": "Hotel with this id already exists"}
        novo_hotel = {"hotel_id": id_hotel, **dados}
        lista_hoteis.append(novo_hotel)
        return hotel, 200

    def put(self, id_hotel):
            ...

    def delete(self, id_hotel):
            ...