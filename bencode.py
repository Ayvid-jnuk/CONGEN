def bencode_encode(data):
    try:
        if isinstance(data, int):
            return f"i{data}e"
        elif isinstance(data, str):
            return f"{len(data)}:{data}"
        elif isinstance(data, list):
            return f"l{''.join(bencode_encode(item) for item in data)}e"
        elif isinstance(data, dict):
            items = ''.join(f"{bencode_encode(str(key))}{bencode_encode(value)}" for key, value in sorted(data.items()))
            return f"d{items}e"
        else:
            raise TypeError("Unsupported data type for bencoding")
    except Exception as e:
        raise ValueError(f"Error in bencoding: {e}")
    
def bencode_decode(b_data):
    try:
        def decode_data(position):
            if b_data[position] == "i":
                position += 1
                try:
                    end_position = b_data.index("e", position)
                except ValueError:
                    raise ValueError("Invalid bencode format: missing 'e' for integer termination")
                number_str = (b_data[position:end_position])
                try:
                    number = int(number_str)
                except ValueError:
                    raise ValueError(f"Invalid integer value: {number_str}")
                return number, end_position + 1
    
            elif b_data[position].isdigit():
                colon_position = b_data.index(":", position)
                if colon_position == -1:
                    raise ValueError("Invalid bencode format: missing ':' for string length")
                length_str = b_data[position:colon_position]
                try:
                    length = int(length_str)
                except ValueError:
                    raise ValueError(f"Invalid string length: {length_str}")
                start = colon_position + 1
                end = start + length
                if end > len(b_data):
                    raise ValueError("Invalid bencode format: string length exceeds data length")
                string = b_data[start:end]
                return string, end
            
            elif b_data[position] == "l":
                position += 1
                lst = []
                while True:
                    if position >= len(b_data):
                        raise ValueError("Invalid bencode format: list not terminated with 'e'")
                    if b_data[position] == "e":
                        return lst, position + 1
                    item, position = decode_data(position)
                    lst.append(item)
            
            elif b_data[position] == "d":
                position += 1
                dct = {}
                while True:
                    if position >= len(b_data):
                        raise ValueError("Invalid bencode format: dictionary not terminated with 'e'")
                    if b_data[position] == "e":
                        return dct, position + 1
                    key, position = decode_data(position)
                    if not isinstance(key, str):
                        raise ValueError("Invalid bencode format: dictionary keys must be strings")
                    value, position = decode_data(position)
                    dct[key] = value
            
            else:
                raise ValueError(f"Invalid bencode format at position {position}")
            
        decoded_value, final_position = decode_data(0)
        if final_position != len(b_data):
            raise ValueError("Invalid bencode format: extra data after valid bencode")
        return decoded_value
    except Exception as e:
        raise ValueError(f"Error in bdecoding: {e}")
    