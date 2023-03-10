import logging

logging.basicConfig(filename="test.log",filemode="w",format="%(asctime)s  %(message)s")

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

logger.debug("HI this is debug info hope you fixed it.")
logger.info("Hi this is information for ops team.")
logger.warning("This is warning for you.")
logger.error("This is error message for the dev team")
logger.critical("This is critical informations.")

#While Doing exception handling log whenever exception is there. 
