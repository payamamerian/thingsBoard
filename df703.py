import json
from utility import utility  # Assuming utility has the required IEEE754_Hex_To_Float conversion function

class DF703:
    @staticmethod
    def parse_data_DF703(req_data):
        try:
            # Example data parsing based on the protocol specification
            # Extracting specific fields from the data string
            # This is a simplistic interpretation and may need adjustments based on actual data format

            # Assuming req_data is a string in the format as specified in the DF703 documentation
            height_hex = req_data[8:12]
            temperature_hex = req_data[16:18]
            longitude_hex = req_data[20:28]  # Only if GPS data is included
            latitude_hex = req_data[28:36]  # Only if GPS data is included

            # Converting hexadecimal values to integers or floats as required
            height = int(height_hex, 16)  # Height in mm
            temperature = int(temperature_hex, 16)  # Temperature in Celsius
            longitude = utility.IEEE754_Hex_To_Float(longitude_hex)  # Convert to float
            latitude = utility.IEEE754_Hex_To_Float(latitude_hex)  # Convert to float

            # Create a JSON object with the parsed data
            data = {
                "height": height,
                "temperature": temperature,
                "longitude": longitude,
                "latitude": latitude
            }

            return json.dumps(data)  # Return data as JSON string

        except Exception as e:
            print(f"Error parsing data: {e}")
            return json.dumps({})

# Example usage
if __name__ == "__main__":
    sample_data = "800001011E0692001A00000000016E008027C40001186962703655111781"
    print(DF703.parse_data_DF703(sample_data))
