import json
from utility import utility  # Assuming this has the IEEE754_Hex_To_Float conversion function

class DF703:
    @staticmethod
    def parse_data_DF703(req_data):
        # Check if data starts with the packet head '80'
        if not req_data.startswith("80"):
            print("Invalid packet header")
            return json.dumps({})

        # Remove the packet head (first 2 characters) and tail (last 2 characters)
        req_data = req_data[2:-2]

        try:
            # Parsing initial fields
            index = 8  # Skip first 8 characters (4 initial fields)
            height = int(req_data[index:index+4], 16)
            index += 4
            gps_selection = req_data[index:index+2]
            index += 2

            if gps_selection == '01':  # With GPS
                longitude = utility.IEEE754_Hex_To_Float(req_data[index:index+8])
                index += 8
                latitude = utility.IEEE754_Hex_To_Float(req_data[index:index+8])
                index += 8
            else:
                longitude = latitude = None

            temperature = int(req_data[index:index+2], 16)
            index += 2  # Skip Reserved byte

            fall_angle = int(req_data[index:index+2], 16)
            index += 2

            status_flags = req_data[index:index+4]
            full_status = int(status_flags[0], 16)
            fire_status = int(status_flags[1], 16)
            fall_status = int(status_flags[2], 16)
            power_status = int(status_flags[3], 16)
            index += 4

            battery_voltage = int(req_data[index:index+4], 16) * 0.01
            index += 4
            rsrp = utility.IEEE754_Hex_To_Float(req_data[index:index+8])
            index += 8
            frame_count = int(req_data[index:index+4], 16)
            index += 4
            device_id_hex = req_data[index:index+16]
            imei = '1' + device_id_hex

            data = {
                "height": height,
                "gps_selection": gps_selection,
                "longitude": longitude,
                "latitude": latitude,
                "temperature": temperature,
                "fall_angle": fall_angle,
                "full_status": full_status,
                "fire_status": fire_status,
                "fall_status": fall_status,
                "power_status": power_status,
                "battery_voltage": battery_voltage,
                "rsrp": rsrp,
                "frame_count": frame_count,
                "imei": imei
            }

            return json.dumps(data)

        except Exception as e:
            print(f"Error parsing data: {e}")
            return json.dumps({})

# Example usage
if __name__ == "__main__":
    sample_data = "800001011E0692001A00000000016E008027C40001186962703655111781"
    print(DF703.parse_data_DF703(sample_data))
