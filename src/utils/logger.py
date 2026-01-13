import logging #python built-in module for logging message 
import os  # os modules to handle folder creation and file path 

def get_logger():
    """
    Returns a configured logger object for cloud monitoring project.
    This will write logs to a central file with format in local system but its 
    ignored by .gitignore which will help use to make our project lite
    along with information that we can use in case of program error.
    """

    #step 1 : Define logs folder 
    log_dir = "logs" # Folder where files will be stored 
    os.makedirs(log_dir, exist_ok=True) #create folder if it doesn't exist ( but we already have)
    
    #Define log file path 
    # full path to log file: this format is compatanle acros mac,windows,linux
    log_file = os.path.join(log_dir,"monitor.log")

    #here we create logger object
    logger = logging.getLogger("cloud-moinitor")
    #named logger so all modules share the same name 
    logger.setLevel(logging.DEBUG)
    #logging lever , whe have 4 differnet types this is basic one. [ debug ]

    if logger.handlers: # avoide duplicate 
        return logger
    
    # creating file hander 
    # file handler writes logs to the specified log file 
    file_handler = logging.FileHandler(log_file)

    #defining log format 
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    # with timestamp--- log level -- actual message 

    #connect format to file handler 
    file_handler.setFormatter(formatter)

    # return the ready to use logger 
    logger.addHandler(file_handler)

    #return the ready to use logger 
    return logger