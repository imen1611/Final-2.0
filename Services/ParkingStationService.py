import json
from Services.UserService import UserService
from models.ParkingStattionModel import ParkingStationModel
from bson import json_util


class ParkingStationService():
    def getAll(token):
        data, code = UserService.find(token)
        if code == 200:
            parkingStations = ParkingStationModel.getAll()
            for counter in range(len(parkingStations)):
                parkingStations[counter].pop("_id")
            data, code = json.dumps(parkingStations), 200
        return data, code

    def add(token, parkingStation):
        data, code = UserService.find(token)
        if code == 200:
            data = json.loads(data) #load data to python 
            user = data['user']
            if ("role" in user):
                if (user["role"].lower() == "admin"):
                    ParkingStationModel.insert(parkingStation)
                    del parkingStation['_id']
                    data, code = json.dumps(parkingStation), 200
                    return data, code
                else:
                    data, code = json.dumps(
                        {"message": "only admin can add parking stations"}), 403
        return data, code

    def reserve(token, reference):
        data, code = UserService.find(token)
        if code == 200:
            data = json.loads(data)
            user = data['user']
            parking = ParkingStationModel.getByReference(reference)
            if (parking["available"] == "True"):
                parking = json.loads(json_util.dumps(parking))
                parking["client"] = user["email"]
                parking["available"] = "False"
                del parking["_id"]
                ParkingStationModel.updateOne(reference, parking)
                data, code = json.dumps(parking), 200
                return data, code
            else:
                data, code = json.dumps(
                    {"message": "this parking is not available"}), 409
                return data, code
        return data, code
    def delete(token, reference):
        data, code = UserService.find(token)
        if code == 200:
            data = json.loads(data) #load data to python 
            user = data['user']
            if ("role" in user):
                if (user["role"].lower() == "admin"):
                 parking_station=ParkingStationModel.getByReference(reference)        
                 if parking_station:
                     ParkingStationModel.deleteOne(reference)
                     print(reference)
                     data, code = json.dumps({"message": "parking station deleted successfully"}), 200
                     return data, code
                else:
                    data, code = json.dumps(
                    {"message": "only admin can delete parking stations"}), 403
            return data, code   