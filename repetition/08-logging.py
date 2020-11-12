import logging
logging.basicConfig(level=logging.INFO)

# This will always be printed, and sent to STDOUT
print("Hello")

# This will be printed as a logging line, and sent to STDERR
logging.info("Hello")

# This will not be visible anywhere as long as we have level set to logging.INFO, since DEBUG is "lower" than INFO
logging.debug("Some debugging message")
