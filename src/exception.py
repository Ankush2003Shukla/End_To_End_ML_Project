import sys

def Detail_Error_Message(Error,Error_detail:sys):
    _,_,exc_tb = Error_detail.exc_info()

    filename = exc_tb.tb_frame.f_code.co_filename

    Error_Message = "---------->Error Occured in System<---------- |||||| Script Name : [{0}] , Line Number : [{1}] and Error Message : [{2}]".format(
        filename,exc_tb.tb_lineno,str(Error)
    )

    return Error_Message

class Custom_Exception(Exception):
    def __init__(self,Error_Message,Error_Detail:sys):
        super().__init__(Error_Message)
        self.Error_Message = Detail_Error_Message(Error_Message,Error_detail=Error_Detail)

    def __str__(self) -> str:
        return self.Error_Message