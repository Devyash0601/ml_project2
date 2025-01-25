import sys

def error_message_detail(error, error_detail: sys):
    """
    Creates a detailed error message with file name, line number, and error details.
    
    Args:
        error (Exception): The exception instance.
        error_detail (sys): System details about the error.

    Returns:
        str: A detailed error message.
    """
    _, _, exc_tb = error_detail.exc_info()  # Get traceback object
    file_name = exc_tb.tb_frame.f_code.co_filename  # Extract the file name
    line_number = exc_tb.tb_lineno  # Extract the line number
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, line_number, str(error)
    )
    return error_message

class CustomException(Exception):
    """
    Custom exception class for handling errors in a more descriptive way.
    """
    def __init__(self, error_message, error_detail: sys):
        """
        Initializes the exception with a custom error message and details.
        
        Args:
            error_message (str): Custom error message to display.
            error_detail (sys): System details of the error.
        """
        super().__init__(error_message)  # Call the base class constructor
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        """
        Returns the detailed error message when the exception is printed.
        
        Returns:
            str: The detailed error message.
        """
        return self.error_message