import requests
from errors.errors import GenHealthPostException, GenHealthAuthException
"""
Creating a class to send things to gen-health.
this could be a simple def function but I thought it would be better to create a class
having the url we are forwarding to as a parameter to the object gives us some flexibility around
the source of the proxy. Mobile to one url maybe and 3rd party to other url.

flexibility to add data sources here was well
"""

class GenhealthService:

    def __init__(self, url: str):
        self.url = url

    # the token and json is what is changing in each request
    def post_to_genhealth(self, json_data: str, token: str):

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token,
        }

        response = requests.post(self.url, headers=headers, json=json_data)

        if not response.ok:

            if response.status_code == 401 or response.status_code == 403:
                raise GenHealthAuthException("Authentication Failure")
            else:
                raise GenHealthPostException("Unable to post to genhealth: Status " +
                                             str(response.status_code) + str(response.content))
        return response.json()
