import traceback
from commonlib import utils as commonlib_utils
from driverAPI.models import Driver, CarOwnedByDriver


def driver_registration(params, request):
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
            new_passenger = Driver.objects.create(first_name=first_name, last_name=last_name,
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
            print(traceback.print_exc())
    except:
        print(traceback.print_exc())


def car_own_by_driver(params, request):
    try:
        driver_number = params['driver_number']
        car_number = params['car_number']
        license_number = params['license_number']

        if (not driver_number) or (not car_number) or (not license_number):
            return {
                'status': 'error',
                'error_code': 'P001',
                'messages': ['Please pass mandatory parameters.']
            }

        if driver_number and driver_number.strip() != "" and not commonlib_utils.validate_mobile_number(driver_number):
            return {
                'status': 'error',
                'error_code': 'P002',
                'message': ['please provide valid mobile number.']
            }

        try:
            fetch_driver = Driver.objects.get(number=driver_number)

            new_car = CarOwnedByDriver.objects.create(driver=fetch_driver, car_number=car_number,
                                                      license_number=license_number)
            new_car.save()

            response_list = [
                {
                    'driver_name': new_car.driver.first_name,
                    'car_number': new_car.car_number,
                    'license_number': new_car.license_number,
                    'status': new_car.status
                }
            ]

            return {
                'status': 'success',
                'error_code': '',
                'message': response_list
            }
        except:
            print(traceback.print_exc())
    except:
        print(traceback.print_exc())
