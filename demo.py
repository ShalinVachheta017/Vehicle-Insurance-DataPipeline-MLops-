# demo.py
"""
Demo script for testing or demonstrating features in the Vehicle Insurance Data Pipeline MLops project.
"""
# from src.logger import logging

# logging.debug("This is a debug message from demo.py")
# logging.info("This is an info message from demo.py")
# logging.warning("This is a warning message from demo.py")
# logging.error("This is an error message from demo.py")
# logging.critical("This is a critical message from demo.py")

# # below code is to check the exception config
# from src.logger import logging
# from src.exception import MyException
# import sys

# try:
#     a = 1+'Z'
# except Exception as e:
#     logging.info(e)
#     raise MyException(e, sys) from e


from src.pipline.training_pipeline import TrainPipeline

pipline = TrainPipeline()
pipline.run_pipeline()