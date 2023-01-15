from bson import json_util
from flask_restful import Resource
from flask import request, Response
from Services.ParkingStationService import ParkingStationService

class ReservationController(Resource):
    def post(self):
        token = json_util.loads(json_util.dumps(request.headers.get('token')))
        reference = json_util.loads(json_util.dumps(request.json))
        data, code = ParkingStationService.reserve(token, reference)
        return Response(data, status=code, mimetype='application/json')
