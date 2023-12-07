# Python
import struct

class DF703:
    @staticmethod
    def parse_data_DF703(req_data):
        try:
            # Check if the data starts with '80'
            if not req_data.startswith('80'):
                print("Invalid data: does not start with '80'")
                return None

            # Remove the packet head
            req_data = req_data[2:]

            # Extracting each field based on the provided structure
            forced_bit = req_data[0:2]
            device_type = req_data[2:4]
            report_data_type = req_data[4:6]
            packet_size = int(req_data[6:8], 16)
            height = int(req_data[8:12], 16)
            gps = req_data[12:14]
            longitude = struct.unpack('!f', bytes.fromhex(''.join(reversed([req_data[14:22][i:i+2] for i in range(0, 8, 2)]))))[0] if gps == '01' else None
            latitude = struct.unpack('!f', bytes.fromhex(''.join(reversed([req_data[22:30][i:i+2] for i in range(0, 8, 2)]))))[0] if gps == '01' else None
            temperature = int(req_data[30:32], 16)
            reserved = req_data[32:34]
            fall_angle = int(req_data[34:36], 16)
            status_hex = req_data[36:40]
            full_status = int(status_hex[0], 16)
            fire_status = int(status_hex[1], 16)
            fall_status = int(status_hex[2], 16)
            power_status = int(status_hex[3], 16)
            battery_voltage = int(req_data[40:44], 16) * 0.01  # Convert to volts
            rsrp = struct.unpack('!f', bytes.fromhex(''.join(reversed([req_data[44:52][i:i+2] for i in range(0, 8, 2)]))))[0]
            frame_count = int(req_data[52:56], 16)
            device_id = req_data[56:72]  # Extract the IMEI directly
            imei = device_id[1:]  # Skip the first character
            packet_tail = req_data[72:74]

            data = {
                "forced_bit": forced_bit,
                "device_type": device_type,
                "report_data_type": report_data_type,
                "packet_size": packet_size,
                "height": height,
                "gps": gps,
                "longitude": longitude,
                "latitude": latitude,
                "temperature": temperature,
                "reserved": reserved,
                "fall_angle": fall_angle,
                "full_status": full_status,
                "fire_status": fire_status,
                "fall_status": fall_status,
                "power_status": power_status,
                "battery_voltage": battery_voltage,
                "rsrp": rsrp,
                "frame_count": frame_count,
                "imei": imei,
                "packet_tail": packet_tail
            }

            return data

        except Exception as e:
            print(f"Error parsing data: {e}")
            return None

# Example usage
if __name__ == "__main__":
    sample_data = "800001011E0692001A00000000016E008027C40001186962703655111781"
    print(DF703.parse_data_DF703(sample_data))