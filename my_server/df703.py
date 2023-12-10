import struct

class DF703:
    @staticmethod
    def byte_to_ascii_digits(byte):
        """Converts a single byte to two ASCII digits."""
        high_nibble = byte >> 4  # Extracts the high 4 bits
        low_nibble = byte & 0x0F  # Extracts the low 4 bits
        return f"{high_nibble}{low_nibble}"

    @staticmethod
    def parse_data_DF703(req_data):
        # Convert hex string to bytes if necessary
        if isinstance(req_data, str):
            req_data = bytes.fromhex(req_data)

        # Unpacking the common fields
        packet_head, forced_bit, device_type, report_data_type, packet_size, height, gps_selection = struct.unpack('>BBBBBHB', req_data[:8])

        parsed_data = {
            'Packet Head': f"{packet_head:02x}",
            'Forced Bit': f"{forced_bit:02x}",
            'Device Type': f"{device_type:02x}",
            'Report Data Type': f"{report_data_type:02x}",
            'Packet Size': f"{packet_size:02x}",
            'Height': height,
            'GPS Selection': f"{gps_selection:02x}"
        }

        # Conditional parsing based on GPS Selection
        offset = 8
        if gps_selection == 0x01:
            longitude, latitude = struct.unpack('>ff', req_data[offset:offset+8])
            offset += 8
            parsed_data.update({'Longitude': longitude, 'Latitude': latitude})
        
        temperature = req_data[offset]
        parsed_data['Temperature'] = temperature
        offset += 1

        # Parsing Reserved, Fall Angle, and Status
        reserved, fall_angle = struct.unpack('>BB', req_data[offset:offset+2])
        offset += 2
        parsed_data['Reserved'] = reserved
        parsed_data['Fall Angle'] = fall_angle

        # Status is two bytes
        status_bytes = req_data[offset:offset + 2]
        full_status = (status_bytes[0] & 0xF0) >> 4
        fire_status = status_bytes[0] & 0x0F
        fall_status = (status_bytes[1] & 0xF0) >> 4
        power_status = status_bytes[1] & 0x0F
        parsed_data.update({'Full Status': full_status, 'Fire Status': fire_status, 'Fall Status': fall_status, 'Power Status': power_status})
        offset += 2

        # Battery Voltage
        battery_voltage_hex = ''.join(f"{byte:02x}" for byte in req_data[offset:offset+2])
        battery_voltage_mV = int(battery_voltage_hex, 16) * 10
        parsed_data['Battery Voltage'] = battery_voltage_mV
        offset += 2

        # RSRP
        rsrp_bytes = req_data[offset:offset + 4]
        rsrp_float = struct.unpack('>f', rsrp_bytes)[0]
        parsed_data['RSRP'] = rsrp_float
        offset += 4

        # Frame Count
        frame_count_bytes = req_data[offset:offset + 2]
        frame_count_decimal = int.from_bytes(frame_count_bytes, byteorder='big')
        parsed_data['Frame Count'] = frame_count_decimal
        offset += 2

        # Device ID and IMEI
        device_id_bytes = req_data[offset:offset + 8]
        imei_bytes = device_id_bytes[1:]
        imei_str = ''.join(DF703.byte_to_ascii_digits(byte) for byte in imei_bytes)
        parsed_data['IMEI'] = imei_str

        return parsed_data

# Example usage
if __name__ == "__main__":
    data = b'\x80\x00\x01\x02\x1e\x04W\x00\x17\x00\x00\x00\x00\x01e\x00\x00x\xc4\x00\x01\x18e8P`\x06\x81Q\x81'
    parsed_data = DF703.parse_data(data)
    print(parsed_data)


