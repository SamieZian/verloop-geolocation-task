from flask import Flask, make_response, request
import requests
# Here we used dicttoxml library to convert our JSON response to XML format
from dicttoxml import dicttoxml as toxml



# Declared variables for our application
my_app = Flask(__name__)
api_key = 'put-your-api-key'  # Put your Valid API key here
base_url = "https://maps.googleapis.com/maps/api/geocode/json"



# Buissness logic declared here like : 
# i) Finding longitude and latitude of given address
# ii) Converting output either in JSON or XML format as per given output_format in POST API
def address_response(address: str,output_format: str = "json"):

    # Creating google geocoding API URL 
    API = f"{base_url}?address={address}&key={api_key}"
    try :
        raw_data = requests.post(API)
        api_response = raw_data.json()['results'][0]['geometry']['location']

        result = {
            "coordinates": {
                "lat": api_response['lat'],
                "lng": api_response['lng']
            },
            "address": address
        }

        if output_format == "json":
            return result
        else:
            xml_response = toxml(result)
            return xml_response
    
    except :
        return 'Error / Something went wrong'



# Declared getAddressDetails route for API requests
@my_app.route('/getAddressDetails', methods=['POST'])
def getAddressDetails():
    request_content = request.json
    address = request_content['address']
    output_format = request_content['output_format']
    # Returning the Result/Response
    return make_response(address_response(address, output_format), 200)



# Starting our main funtion here
if __name__ == "__main__":
    my_app.run(debug=True)