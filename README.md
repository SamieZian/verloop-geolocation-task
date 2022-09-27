# verloop-geolocation-task
Problem statement: You have to create an API endpoint, which returns data related to geolocation.  Use case: When an address is passed in the body, the corresponding latitude and longitude are returned in the response. The format in which the response is returned is dictated by the `output_format` flag, the options for this flag are “json” or “xml”. If the output flag is set to json the response from the API should be in json format and if the flag is set to xml the response should be in xml format.

# Git Clone
`git clone https://github.com/SamieZian/verloop-geolocation-task.git`

### Go to verloop_geo_api.py file & change `api_key` with your valid google geocoding API key ( Refer line No : 10)
`api_key = 'put-your-api-key'` --> `api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'`

### Go to terminal ( Install all dependencies )
`pip install -r requirements.txt`

### Run the application
`python verloop_geo_api.py`



![geo_coding_api_json](https://user-images.githubusercontent.com/76624147/192455132-d4296e95-08b4-46b2-86da-8065bd78e83e.png)
![geo_coding_api_xml](https://user-images.githubusercontent.com/76624147/192455152-c766ace2-00d0-4faf-9d93-76659cd5a961.png)
