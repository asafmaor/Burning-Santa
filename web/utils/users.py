from santa.models import SantaUser, Address

__author__ = 'safo'


def register_new_user(santa_user, first_name, last_name, playa_name, city, address, is_willing_to_get, zipcode=''):
    santa_user.first_name = first_name
    santa_user.last_name = last_name
    santa_user.playa_name = playa_name
    santa_user.willing_to_get = is_willing_to_get
    santa_user.save()
    address = Address()
    address.city = city
    address.address = address
    address.save()
    return santa_user

# TODO: actually authenticate
def authenticate_midburn(username, password):
    return username != 'bad'


