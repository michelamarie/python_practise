#!/usr/bin/python3

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - % (levelname)s - %(message)s')


logging.debug("Start of program.")

logging.critical("Critical message!")
logging.warning("This is a warning, missy!")
logging.info("Here is some information for you.")
logging.debug("Geek-level message here.")


