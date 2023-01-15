from controllers.ParkingStationController import ParkingStationController
from controllers.ReservationController import ReservationController
from controllers.loginController import LoginController
from controllers.userController import UserController
from controllers.GazStationController import GazStationController


def initialize_routes(api):
  api.add_resource(UserController, "/api/user")
  api.add_resource(LoginController, "/api/login")
  api.add_resource(ParkingStationController, "/api/parking/stations")
  api.add_resource(ReservationController, "/api/parking/stations/reserve")
  api.add_resource(GazStationController, "/api/gaz/stations")