import logging
import re

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# File handler
file_handler = logging.FileHandler('address_validation.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def validate_address(address):
    try:
        if address is None:
            logger.error("Validation failed: address cannot be None")
            raise ValueError("address cannot be None")
        elif not isinstance(address, str):
            logger.error("Validation failed: address must be a string")
            raise ValueError("address must be a string")
        elif len(address) < 10:
            logger.error("Validation failed: address must have at least 10 characters")
            raise ValueError("address must have at least 10 characters")
        elif not re.match(r'^[a-zA-Z0-9\s,.-]+$', address): # match() function is used to match the string with the regular expression
            logger.error("Validation failed: address contains invalid characters")
            raise ValueError("address contains invalid characters")
        logger.info("Validation successful: address is valid")
        return True
    except ValueError as e:
        logger.exception(f"Exception occurred: {e}")
        return False

def test_address_validation(addresses):
    for address in addresses:
        if validate_address(address):
            print(f"'{address}' is valid")
        else:
            print(f"'{address}' is invalid")

# Test the function
addresses = input("Enter your addresses separated by semicolons: ").strip().split(';')
test_address_validation(addresses)

# strip use for remove white space from start and end of string
# slpit use for split the string by semicolon.
