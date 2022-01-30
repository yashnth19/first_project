import Logger

class training_data_validator:
    def __init__(self):
        self.log_writer=Logger.logger_tool()
        self.file_object = open("Logs.txt", 'a+')

    def check_logger(self):
        try:
            self.log_writer.log_this(self.file_object,"logging checked")
        except Exception as e:
            raise e

