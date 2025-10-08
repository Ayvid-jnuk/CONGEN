class BaseConverter:
    @staticmethod
    def decimal_to_binary(decimal):
        if isinstance(decimal, str):
            if decimal.strip().isdigit():
                decimal = int(decimal.strip())
            else:
                raise ValueError("Input must be a non-negative integer.")
    
        if not isinstance(decimal, int) or decimal < 0:
            raise ValueError("Input must be a non-negative integer.")
        
        return bin(decimal).replace("0b", "")
    
    @staticmethod
    def binary_to_decimal(binary):
        if isinstance(binary, int):
            binary = str(binary)

        if isinstance(binary, str):
            binary = binary.strip()
            if not all(char in '01' for char in binary):
                raise ValueError("Input must be a binary string.")
        else:
            raise ValueError("Input must be a binary string.")
        
        return int(binary, 2)
    
    @staticmethod
    def decimal_to_hexadecimal(decimal):
        if isinstance(decimal, str):
            if decimal.strip().isdigit():
                decimal = int(decimal.strip())
            else:
                raise ValueError("Input must be a non-negative integer.")
        
        if not isinstance(decimal, int) or decimal < 0:
            raise ValueError("Input must be a non-negative integer.")
        else:
            return hex(decimal).replace("0x", "").upper()
        
    @staticmethod
    def hexadecimal_to_decimal(hexadecimal):
        if isinstance(hexadecimal, int):
            hexadecimal = str(hexadecimal)

        if isinstance(hexadecimal, str):
            hexadecimal = hexadecimal.strip().upper()

            if hexadecimal.startswith("0X"):
                hexadecimal = hexadecimal[2:]

            if not all(char in '0123456789ABCDEF' for char in hexadecimal):
                raise ValueError("Input must be a hexadecimal string.")
            
            return int(hexadecimal, 16)
        else:
            raise ValueError("Input must be a hexadecimal string.")
        
    @staticmethod
    def binary_to_hexadecimal(binary):
        decimal = BaseConverter.binary_to_decimal(binary)
        return BaseConverter.decimal_to_hexadecimal(decimal)
    
    @staticmethod
    def hexadecimal_to_binary(hexadecimal):
        decimal = BaseConverter.hexadecimal_to_decimal(hexadecimal)
        return BaseConverter.decimal_to_binary(decimal)
    
    @staticmethod
    def decimal_to_octal(decimal):
        if isinstance(decimal, str):
            if decimal.strip().isdigit():
                decimal = int(decimal.strip())
            else:
                raise ValueError("Input must be a non-negative integer.")
        
        if not isinstance(decimal, int) or decimal < 0:
            raise ValueError("Input must be a non-negative integer.")
        else:
            return oct(decimal).replace("0o", "")
        
    @staticmethod
    def octal_to_decimal(octal):
        if isinstance(octal, int):
            octal = str(octal)

        if isinstance(octal, str):
            octal = octal.strip()
            if not all(char in '01234567' for char in octal):
                raise ValueError("Input must be an octal string.")
        else:
            raise ValueError("Input must be an octal string.")
        
        return int(octal, 8)
    
    @staticmethod
    def binary_to_octal(binary):
        decimal = BaseConverter.binary_to_decimal(binary)
        return BaseConverter.decimal_to_octal(decimal)
    
    @staticmethod
    def octal_to_binary(octal):
        decimal = BaseConverter.octal_to_decimal(octal)
        return BaseConverter.decimal_to_binary(decimal)
    
    @staticmethod
    def hexadecimal_to_octal(hexadecimal):
        decimal = BaseConverter.hexadecimal_to_decimal(hexadecimal)
        return BaseConverter.decimal_to_octal(decimal)
    
    @staticmethod
    def octal_to_hexadecimal(octal):
        decimal = BaseConverter.octal_to_decimal(octal)
        return BaseConverter.decimal_to_hexadecimal(decimal)
    
 