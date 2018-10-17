import os

import api.server
from logzero import logger

if __name__ == "__main__":
    logger.info("App running on port ")
    port = int(os.environ.get("PORT", 8000))
    api.server.run(port)
