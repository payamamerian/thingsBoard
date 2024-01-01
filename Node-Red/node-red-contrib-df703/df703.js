module.exports = function(RED) {
    function DF703Node(config) {
        RED.nodes.createNode(this, config);

        this.on('input', function(msg) {
            const req_data = msg.payload;

            // Convert hex string to bytes if necessary
            if (typeof req_data === 'string') {
                req_data = Buffer.from(req_data, 'hex');
            }

            // Unpacking the common fields
            const packet_head = req_data.readUInt8(0);
            const forced_bit = req_data.readUInt8(1);
            const device_type = req_data.readUInt8(2);
            const report_data_type = req_data.readUInt8(3);
            const packet_size = req_data.readUInt8(4);
            const height = req_data.readUInt16BE(5);
            const gps_selection = req_data.readUInt8(7);

            const parsed_data = {
                'Packet Head': packet_head.toString(16).padStart(2, '0'),
                'Forced Bit': forced_bit.toString(16).padStart(2, '0'),
                'Device Type': device_type.toString(16).padStart(2, '0'),
                'Report Data Type': report_data_type.toString(16).padStart(2, '0'),
                'Packet Size': packet_size.toString(16).padStart(2, '0'),
                'Height': height,
                'GPS Selection': gps_selection.toString(16).padStart(2, '0'),
            };

            // Conditional parsing based on GPS Selection
            let offset = 8;
            if (gps_selection === 0x01) {
                const longitude = req_data.readFloatBE(offset);
                const latitude = req_data.readFloatBE(offset + 4);
                offset += 8;
                parsed_data['Longitude'] = longitude;
                parsed_data['Latitude'] = latitude;
            }

            const temperature = req_data.readUInt8(offset);
            parsed_data['Temperature'] = temperature;
            offset += 1;

            // Parsing Reserved, Fall Angle, and Status
            const reserved = req_data.readUInt8(offset);
            const fall_angle = req_data.readUInt8(offset + 1);
            offset += 2;
            parsed_data['Reserved'] = reserved;
            parsed_data['Fall Angle'] = fall_angle;

            // Status is two bytes
            const status_bytes = req_data.slice(offset, offset + 2);
            const full_status = (status_bytes[0] & 0xF0) >> 4;
            const fire_status = status_bytes[0] & 0x0F;
            const fall_status = (status_bytes[1] & 0xF0) >> 4;
            const power_status = status_bytes[1] & 0x0F;
            parsed_data['Full Status'] = full_status;
            parsed_data['Fire Status'] = fire_status;
            parsed_data['Fall Status'] = fall_status;
            parsed_data['Power Status'] = power_status;
            offset += 2;

            // Battery Voltage
            const battery_voltage_hex = req_data.slice(offset, offset + 2).toString('hex');
            const battery_voltage_mV = parseInt(battery_voltage_hex, 16) * 10;
            parsed_data['Battery Voltage'] = battery_voltage_mV;
            offset += 2;

            // RSRP
            const rsrp_bytes = req_data.slice(offset, offset + 4);
            const rsrp_float = rsrp_bytes.readFloatBE(0);
            parsed_data['RSRP'] = rsrp_float;
            offset += 4;

            // Frame Count
            const frame_count_bytes = req_data.slice(offset, offset + 2);
            const frame_count_decimal = frame_count_bytes.readUInt16BE(0);
            parsed_data['Frame Count'] = frame_count_decimal;
            offset += 2;

            // Device ID and IMEI
            const device_id_bytes = req_data.slice(offset, offset + 8);
            const imei_bytes = device_id_bytes.slice(1);
            const imei_str = Array.from(imei_bytes).map(byte => DF703.byte_to_ascii_digits(byte)).join('');
            parsed_data['IMEI'] = imei_str;

            msg.payload = parsed_data;
            this.send(msg);
        });
    }

    RED.nodes.registerType("df703", DF703Node);
}
