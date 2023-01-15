from bson import json_util
from flask_restful import Resource
from flask import request, Response 
from Services.GazStationService import GazStationService

class GazStationController(Resource):
    def get(self):
        token = json_util.loads(json_util.dumps(request.headers.get('token')))
        data, code = GazStationService.getAll(token)
        return Response(data, status=code, mimetype='application/json')

    def post(self):
        token = json_util.loads(json_util.dumps(request.headers.get('token')))
        gazStation = json_util.loads(json_util.dumps(request.json))
        data, code = GazStationService.add(token, gazStation)
        return Response(data, status=code, mimetype='application/json')

    def delete(self):
        token = json_util.loads(json_util.dumps(request.headers.get('token')))
        gazStation = json_util.loads(json_util.dumps(request.json))
        data, code = GazStationService.delete(token, gazStation)
        return Response(data, status=code, mimetype='application/json')        
