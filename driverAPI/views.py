from rest_framework.views import APIView
from . import driver_utils
from commonlib import utils as commonlib_utils
from rest_framework import status


class DriverRegistration(APIView):
    def post(self, request):
        params = {
            'first_name': request.data.get('first_name', None),
            'last_name': request.data.get('last_name', None),
            'email': request.data.get('email', None),
            'number': request.data.get('number', None),
            'password': request.data.get('password', None)
        }

        result = driver_utils.driver_registration(params, request)
        return commonlib_utils.response(result, status.HTTP_200_OK)


class CarOwnByDriver(APIView):
    def post(self, request):
        params = {
            'driver_number': request.data.get('driver_number', None),
            'car_number': request.data.get('car_number', None),
            'license_number': request.data.get('license_number', None),
        }

        result = driver_utils.car_own_by_driver(params, request)
        return commonlib_utils.response(result, status.HTTP_200_OK)


class RideCompleted(APIView):
    def post(self, request):
        params = {
            'driver_number': request.data.get('driver_number', None),
            'car_number': request.data.get('car_number', None)
        }

        result = driver_utils.ride_completed(params, request)
        return commonlib_utils.response(result, status.HTTP_200_OK)

class DriverHistory(APIView):
    def post(self, request):
        params = {
            'driver_number': request.data.get('driver_number', None)
        }

        result = driver_utils.driver_history(params, request)
        return commonlib_utils.response(result, status.HTTP_200_OK)
