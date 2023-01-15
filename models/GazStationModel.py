from configPack import mongo

class GazStationModel():
    def getAll():
        gazstations = list(mongo.db.gazstations.find())
        return gazstations

    def insert(gazstation):
        mongo.db.gazstations.insert_one(gazstation)

    def getByReference(reference):
        gazstation = mongo.db.gazstations.find(zip)
        return gazstation

    def updateOne(reference, update):
        mongo.db.gazstations.update_one(reference, {"$set": update})
    
    def deleteOne(reference):
        mongo.db.parkingstations.delete_one(reference)