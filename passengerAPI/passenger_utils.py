import traceback
from django.db import transaction
from commonlib import utils as commonlib_utils
from driverAPI.models import Driver, DriverHistory, CarOwnedByDriver
from passengerAPI.models import Passenger, PassengerHistory
from driverAPI import constants as driver_constants


def passenger_registration(params, request):
    try:
        first_name = params['first_name']
        last_name = params['last_name']
        email = params['email']
        number = params['number']
        password = params['password']

        if (not first_name) or (not last_name) or (not email) or (not number) or (not password):
            return {
                'status': 'error',
                'error_code': 'P001',
                'messages': ['Please pass mandatory parameters.']
            }

        if number and number.strip() != "" and not commonlib_utils.validate_mobile_number(number):
            return {
                'status': 'error',
                'error_code': 'P002',
                'message': ['please provide valid mobile number.']
            }

        try:
            new_passenger = Passenger.objects.create(first_name=first_name, last_name=last_name,
                                                     email=email, number=number, password=password)
            new_passenger.save()

            response_list = [
                {
                    'first_name': new_passenger.first_name,
                    'last_name': new_passenger.last_name,
                    'email': new_passenger.email,
                    'number': new_passenger.number,
                    'password': new_passenger.password
                }
            ]

            return {
                'status': 'success',
                'error_code': '',
                'message': response_list
            }
        except:
            traceback.print_exc()
    except:
        traceback.print_exc()


def book_cab(params, request):
    try:
        passenger_number = params['passenger_number']
        source_address = params['source_address']
        destination_address = params['destination_address']

        if (not passenger_number) or (not source_address) or (not destination_address):
            return {
                'status': 'error',
                'error_code': 'P001',
                'messages': ['Please pass mandatory parameters.']
            }

        if passenger_number and passenger_number.strip() != "" and not commonlib_utils.validate_mobile_number(
                passenger_number):
            return {
                'status': 'error',
                'error_code': 'P002',
                'message': ['please provide valid mobile number.']
            }

        try:
            with transaction.atomic():
                # find current passenger
                fetch_passenger = Passenger.objects.get(number=passenger_number)

                # find all available driver
                fetch_drivers = CarOwnedByDriver.objects.select_related('driver').filter(status=driver_constants.FREE)

                fetch_driver = None
                if fetch_drivers:
                    fetch_driver = fetch_drivers[0]
                    fetch_driver.status = driver_constants.OCCUPIED
                    fetch_driver.save()
                else:
                    return {
                        'status': 'success',
                        'error_code': '',
                        'message': ['No cabs are available right now.']
                    }

                new_ph = PassengerHistory.objects.create(passenger=fetch_passenger, driver=fetch_driver.driver,
                                                         source_address=source_address,
                                                         destination_address=destination_address)
                new_ph.save()

                new_dh = DriverHistory.objects.create(passenger=fetch_passenger, driver=fetch_driver.driver,
                                                      source_address=source_address,
                                                      destination_address=destination_address)
                new_dh.save()

                response_list = [
                    {
                        'passenger_name': fetch_passenger.first_name,
                        'driver_name': fetch_driver.driver.first_name,
                        'source_address': source_address,
                        'destination_address': destination_address,
                        'car_number': fetch_driver.car_number,
                        'message': 'Cab Booked Successfully'
                    }
                ]

                return {
                    'status': 'success',
                    'error_code': '',
                    'message': response_list
                }

        except:
            traceback.print_exc()
    except:
        traceback.print_exc()


def passenger_history(params, request):
    try:
        passenger_number = params['passenger_number']

        if not passenger_number:
            return {
                'status': 'error',
                'error_code': 'P001',
                'messages': ['Please pass mandatory parameters.']
            }

        if passenger_number and passenger_number.strip() != "" and not commonlib_utils.validate_mobile_number(
                passenger_number):
            return {
                'status': 'error',
                'error_code': 'P002',
                'message': ['please provide valid mobile number.']

            }

        try:
            fetch_passenger_history = PassengerHistory.objects.select_related('passenger').filter(passenger__number=passenger_number)

            if fetch_passenger_history:
                response_list = []
                for ph in fetch_passenger_history:
                    # ph = passenger_history
                    passenger_details = {
                        'passenger_name': ph.passenger.first_name,
                        'driver_name': ph.driver.first_name,
                        'source_address': ph.source_address,
                        'destination_address': ph.destination_address
                    }
                    response_list.append(passenger_details)

                return {
                    'status': 'success',
                    'error_code': '',
                    'message': response_list
                }
            else:
                return {
                    'status': 'error',
                    'error_code': 'P003',
                    'message': ['Passenger history does not exist.']
                }
        except:
            traceback.print_exc()
    except:
        traceback.print_exc()
