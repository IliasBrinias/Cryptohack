import json
import jwt


def create_session(username):
    body = '{' \
              + '"admin": "' + "True" \
              + '", "username": "' + str(username) \
              + '"}'
    encoded = jwt.encode(json.loads(body), "secret", algorithm='HS256')
    return encoded


print("-------------Token Appreciation")
encrypt = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmbGFnIjoiY3J5cHRve2p3dF9jb250ZW50c19jYW5fYmVfZWFzaWx5X3ZpZX" \
          "dlZH0iLCJ1c2VyIjoiQ3J5cHRvIE1jSGFjayIsImV4cCI6MjAwNTAzMzQ5M30.shKSmZfgGVvd2OSB2CGezzJ3N6WAULo3w9zCl_T47KQ"
decoded = jwt.decode(encrypt, options={"verify_signature": False})
print("flag:",decoded["flag"])
print("-------------JWT Sessions")
# alg and secret key must be None
print(jwt.encode({'username': "", 'admin': True}, None, algorithm=None))
print("-------------JWT Secrets")
# default key from the documentation is 'secret'
print(jwt.encode({'username': "", 'admin': True}, "secret", algorithm='HS256'))
print("-------------RSA or HMAC?")
public = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsXRBeaADq9e5tKU5UzAc/Ty4e/kUmIMJJXeIYBy8qs9mfB2OISHIRLZj7jqxuhqa+bi6VNhIEGUdvOBQYGnZHoTGKsMDTjAiWVC7AQUVirLt1oZDNat+7hs5lnkscpx4B5tSEFR0C5uC9cDoolrZP366Bykb1nYfp7B8JIZS1iYgT6WWYO+aZ3/z95vJku1XiYSCbwGxntkP0w0bOBthKBfUIFHHa53ba6l8GT6ATAYA0hak8FTz7on+GQme0GYUV1DpnZ4Rx8x8/jWK49w/70/OxCKCYzXhYt/5tB2SweRUOsVSHYtpLa6ad0J4xydkmJaGshvYrHT5+Uk0zFHKpwIDAQAB"
# print(jwt.encode({'username': "", 'admin': True}, public, algorithm='RS256'))
print("-------------JSON in JSON")
print(create_session(""))
