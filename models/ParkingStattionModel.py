from configPack import mongo
from bson.objectid import ObjectId


class ParkingStationModel():
    def getAll():
        parkingstations = list(mongo.db.parkingstations.find())
        return parkingstations

    def insert(parkingstation):
        mongo.db.parkingstations.insert_one(parkingstation)

    def getOne(id):
        parkingstation = mongo.db.parkingstations.find_one(
            {"_id": ObjectId(id)})
        return parkingstation

    def getByReference(reference):
        parkingstation = mongo.db.parkingstations.find_one(reference)
        return parkingstation

    def updateOne(reference, update):
      mongo.db.parkingstations.update_one(reference, {"$set": update})

    def deleteOne(reference):
        mongo.db.parkingstations.delete_one(reference)
