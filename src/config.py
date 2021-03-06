import os

IN_PRODUCTION = os.getenv("ENV_NAME", False)
SECRET_KEY = os.getenv("SECRET_KEY", "shhhh! it's a secret")

# infrastructure
local_db = "sqlite:////home/densolovev/Projects/learn-io/learn-io.db"
DATABASE_URI = os.getenv("DATABASE_URI", local_db)

# internal configuration
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "[%(asctime)s] %(name)s:%(lineno)s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    },
    "handlers": {"local": {"class": "logging.StreamHandler", "formatter": "standard"}},
    "loggers": {
        "app": {"handlers": ["local"], "level": "INFO" if IN_PRODUCTION else "DEBUG"}
    },
}
