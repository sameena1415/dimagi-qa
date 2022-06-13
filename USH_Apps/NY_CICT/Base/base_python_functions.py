from robot.api.deco import keyword

import base64
import pyotp
from selenium.common.exceptions import TimeoutException


@keyword("Generate 2FA Token")
def generate_auth_token(secret):
    encoded = base64.b64encode(base64.b64decode(secret))
    totp = pyotp.TOTP(encoded)
    token = str(totp.now())
    print("Current OTP:", token)
    return token


@keyword("Check Contact ID")
def check_if_six_digit_alphanumneric(contact_id):
    is_six_digit_alphanumneric = None
    contact_id = get_string(contact_id)
    if contact_id.isalnum() and len(contact_id) == 6:
        is_six_digit_alphanumneric = True
    else:
        is_six_digit_alphanumneric = False
    return is_six_digit_alphanumneric


@keyword("Get String")
def get_string(string_name):
    string_name = string_name.split(":")[1].strip()
    print(string_name)
    return string_name
