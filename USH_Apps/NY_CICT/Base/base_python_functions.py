from robot.api.deco import keyword

import base64
import pyotp


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
    contact_id = contact_id.split(":")[1].strip()
    print(contact_id)
    if contact_id.isalnum() and len(contact_id) == 6:
        is_six_digit_alphanumneric = True
    else:
        is_six_digit_alphanumneric = False
    return is_six_digit_alphanumneric

