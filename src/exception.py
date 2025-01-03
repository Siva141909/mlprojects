import sys
from src.logger import logging

def error_message_detail(error, error_detail: sys):
    '''
    Generate detailed error message including script name, line number, and error message.
    '''
    # Extract exception details
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script [{0}] at line [{1}]: {2}".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message


class CustomException(Exception):
    '''
    Custom Exception class for detailed error logging.
    '''
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
    
    def __str__(self):
        return self.error_message


# Main execution block (outside the class)
if __name__ == "__main__":
    try:
        # Example error
        a = 10 / 0
    except Exception as e:
        logging.info("An exception occurred: Division by zero")
        # Raise custom exception
        raise CustomException(e, sys)
