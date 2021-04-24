from rest_framework.views import APIView
from . import passenger_utils
from commonlib import utils as commonlib_utils
from rest_framework import status


class PassengerRegistration(APIView):
    def post(self, request):
        params = {
            'first_name': request.data.get('first_name', None),
            'last_name': request.data.get('last_name', None),
            'email': request.data.get('email', None),
            'number': request.data.get('number', None),
            'password': request.data.get('password', None)
        }

        result = passenger_utils.passenger_registration(params, request)
        return commonlib_utils.response(result, status.HTTP_200_OK)


class BookCab(APIView):
    def post(self, request):
        params = {
            'passenger_number': request.data.get('passenger_number', None),
            'source_address': request.data.get('source_address', None),
            'destination_address': request.data.get('destination_address', None)
        }

        result = passenger_utils.book_cab(params, request)
        return commonlib_utils.response(result, status.HTTP_200_OK)


class PassengerHistory(APIView):
    def post(self, request):
        params = {
            'passenger_number': request.data.get('passenger_number', None)
        }

        result = passenger_utils.passenger_history(params, request)
        return commonlib_utils.response(result, status.HTTP_200_OK)
