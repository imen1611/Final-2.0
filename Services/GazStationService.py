import json
from Services.UserService import UserService
from models.GazStationModel import GazStationModel
from bson import json_util


class GazStationService():
    def getAll(token):
        data, code = UserService.find(token)
        if code == 200:
            gazStations = GazStationModel.getAll()
            for counter in range(len(gazStations)):
                gazStations[counter].pop("_id")
            data, code = json.dumps(gazStations), 200
        return data, code

    def add(token, gazStation):
        data, code = UserService.find(token)
        if code == 200:
            data = json.loads(data) #load data to python 
            user = data['user']
            if ("role" in user):
                if (user["role"].lower() == "admin"):
                    GazStationModel.insert(gazStation)
                    del gazStation['_id']
                    data, code = json.dumps(gazStation), 200
                    return data, code
                else:
                    data, code = json.dumps(
                        {"message": "only admin can add parking stations"}), 403
        return data, code
    def delete(token, reference):
        data, code = UserService.find(token)
        if code == 200:
            data = json.loads(data) #load data to python 
            user = data['user']
            if ("role" in user):
                if (user["role"].lower() == "admin"):
                 parking_station=GazStationModel.getByReference(reference)        
                 if parking_station:
                     GazStationModel.deleteOne(reference)
                     print(reference)
                     data, code = json.dumps({"message": "parking station deleted successfully"}), 200
                     return data, code
                else:
                    data, code = json.dumps(
                    {"message": "only admin can delete parking stations"}), 403
            return data, code           