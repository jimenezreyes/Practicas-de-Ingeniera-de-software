from alchemyClasses.Renta import Renta

def get_all_rentas():
    return Renta.query.all()

def get_renta_by_id(id):
    return Renta.query.filter(Renta.idRenta == id)