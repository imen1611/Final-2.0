from bson import json_util
from flask_restful import Resource
from flask import request, Response 
from Services.ParkingStationService import ParkingStationService

class ParkingStationController(Resource):
    def get(self):
        token = json_util.loads(json_util.dumps(request.headers.get('token')))
        data, code = ParkingStationService.getAll(token)
        return Response(data, status=code, mimetype='application/json')

    def post(self):
        token = json_util.loads(json_util.dumps(request.headers.get('token')))
        parkingStation = json_util.loads(json_util.dumps(request.json))
        data, code = ParkingStationService.add(token, parkingStation)
        return Response(data, status=code, mimetype='application/json')

    def delete(self):
        token = json_util.loads(json_util.dumps(request.headers.get('token')))
        parkingStation = json_util.loads(json_util.dumps(request.json))
        data, code = ParkingStationService.delete(token, parkingStation)
        return Response(data, status=code, mimetype='application/json')        
