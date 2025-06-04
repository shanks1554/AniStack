import traceback # To track the error
import sys

class CustomException(Exception):
    
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message) # To inherit from exception class
        self.error_message=self.get_detailed_error_message(error_message,error_detail)
    
    @staticmethod # Functions and methods become independent so no need to create this class everytime
    def get_detailed_error_message(error_message, error_detail:sys):
        
        _, _, exc_tb = traceback.sys.exc_info()
        file_name=exc_tb.tb_frame.f_code.co_filename
        line_number=exc_tb.tb_lineno

        return f"Error in {file_name}, line {line_number}: {error_message}"
    
    def __str__(self):
        return self.error_message
    
    