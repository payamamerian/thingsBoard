import json
from utility import utility  # Assuming this has the IEEE754_Hex_To_Float conversion function

class DF703:
    @staticmethod
    def parse_data_DF703(req_data):
        try:
            # Extracting packet size and other fields
            packet_size_hex = req_data[8:10]
            packet_size = int(packet_size_hex, 16)
            height = int(req_data[10:14], 16)
            gps_selection = req_data[14:16]

            # Process data based on GPS selection
            if gps_selection == '00':  # No GPS
                temperature = int(req_data[16:18], 16)
                alarm_status_hex = req_data[20:24]
                full_status = int(alarm_status_hex[0], 16)
                fire_status = int(alarm_status_hex[1], 16)
                fall_status = int(alarm_status_hex[2], 16)
                battery_status = int(alarm_status_hex[3], 16)
                battery_voltage_hex = req_data[24:28]
                battery_voltage = int(battery_voltage_hex, 16) * 0.01  # Convert to volts
                rsrp = utility.IEEE754_Hex_To_Float(req_data[28:36])
                imei = req_data[36:52]

                data = {
                    "packet_size": packet_size,
                    "height": height,
                    "temperature": temperature,
                    "full_status": full_status,
                    "fire_status": fire_status,
                    "fall_status": fall_status,
                    "battery_status": battery_status,
                    "battery_voltage": battery_voltage,
                    "rsrp": rsrp,
                    "imei": imei
                }

            else:  # With GPS
                longitude = utility.IEEE754_Hex_To_Float(req_data[16:24])
                latitude = utility.IEEE754_Hex_To_Float(req_data[24:32])
                temperature = int(req_data[32:34], 16)
                alarm_status_hex = req_data[36:40]
                full_status = int(alarm_status_hex[0], 16)
                fire_status = int(alarm_status_hex[1], 16)
                fall_status = int(alarm_status_hex[2], 16)
                battery_status = int(alarm_status_hex[3], 16)
                battery_voltage_hex = req_data[40:44]
                battery_voltage = int(battery_voltage_hex, 16) * 0.01  # Convert to volts
                rsrp = utility.IEEE754_Hex_To_Float(req_data[44:52])
                imei = req_data[52:68]

                data = {
                    "packet_size": packet_size,
                    "height": height,
                    "longitude": longitude,
                    "latitude": latitude,
                    "temperature": temperature,
                    "full_status": full_status,
                    "fire_status": fire_status,
                    "fall_status": fall_status,
                    "battery_status": battery_status,
                    "battery_voltage": battery_voltage,
                    "rsrp": rsrp,
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
