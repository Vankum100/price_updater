import logging
import sys

import utils.globals as g


class CustomFormatter(logging.Formatter):
    """Custom formatter to set the color of the logging level"""

    BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

    # Define the color codes
    RESET_SEQ = "\033[0m"
    COLOR_SEQ = "\033[1;%dm"
    COLORS = {
        "WARNING": YELLOW,
        "INFO": GREEN,
        "DEBUG": BLUE,
        "CRITICAL": RED,
        "ERROR": RED,
    }

    def format(self, record):
        # Set the color based on the level of the message
        levelname = record.levelname
        if levelname in self.COLORS:
            color = self.COLOR_SEQ % (30 + self.COLORS[levelname])
            levelname_color = f"{color}{levelname}{self.RESET_SEQ}"
            record.levelname = levelname_color
        return super().format(record)


def get_logger(name: str, level: int = logging.INFO):
    """Creates the global Logger.

    Creates a :class:`Logger<logging.Logger>` named :any:`name` and sets it as
    the :data:`global logger<utils.globals.log>`. Messages are formatted using
    the format string ``"%(asctime)s - [%(levelname)s] %(name)s: %(message)s"``.

    The Logger uses three :class:`Handlers<logging.Handler>` to log to:

    * :abbr:`stdout (standard output)` stream with
      :attr:`logging level<logging.Handler.level>` :any:`level`.
    * :file:`log.txt` with logging level :attr:`~logging.INFO`.
    * :file:`log_debug.txt` with logging level :attr:`~logging.DEBUG`.

    Parameters
    ----------
    name: str
        The :attr:`~logging.Logger.name` of the Logger.
    level: int, optional
        The :attr:`logging level<logging.Handler.level>` of the ``stdout``
        :class:`StreamHandler<logging.StreamHandler>`.

    Returns
    -------
    logging.Logger
        The Logger which is created.
    """
    logger: logging.Logger = logging.getLogger(name)
    logger.setLevel(level)

    # Use the custom formatter
    formatter: logging.Formatter = CustomFormatter(
        "%(asctime)s - [%(levelname)s] %(name)s: %(message)s"
    )

    handler: logging.Handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    file_handler: logging.Handler = logging.FileHandler(
        filename="log.txt", encoding="utf-8", mode="w"
    )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    file_handler_debug: logging.Handler = logging.FileHandler(
        filename="log-debug.txt", encoding="utf-8", mode="w"
    )
    file_handler_debug.setLevel(logging.DEBUG)
    file_handler_debug.setFormatter(formatter)
    logger.addHandler(file_handler_debug)

    g.log = logger
