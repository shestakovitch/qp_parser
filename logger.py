import logging
import os
import sys
from pathlib import Path
from typing import Optional

LOG_FORMAT = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
PROJECT_DIR = Path(__file__).resolve().parent
DEFAULT_LOG_FILE = PROJECT_DIR / "qp_parser.log"


def _has_file_handler(root_logger: logging.Logger, log_file: Path) -> bool:
    resolved = log_file.resolve()
    return any(
        isinstance(handler, logging.FileHandler) and Path(handler.baseFilename) == resolved
        for handler in root_logger.handlers
    )


def _has_console_handler(root_logger: logging.Logger) -> bool:
    return any(
        isinstance(handler, logging.StreamHandler) and not isinstance(handler, logging.FileHandler)
        for handler in root_logger.handlers
    )


def setup_logging(
    level: Optional[str] = None,
    log_file: str | Path = DEFAULT_LOG_FILE,
) -> logging.Logger:
    log_level = (level or os.getenv("LOG_LEVEL", "INFO")).upper()
    numeric_level = getattr(logging, log_level, logging.INFO)
    log_file = Path(log_file)

    root_logger = logging.getLogger()
    root_logger.setLevel(numeric_level)

    formatter = logging.Formatter(LOG_FORMAT, datefmt=LOG_DATE_FORMAT)

    if not _has_console_handler(root_logger):
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(numeric_level)
        console_handler.setFormatter(formatter)
        root_logger.addHandler(console_handler)

    if not _has_file_handler(root_logger, log_file):
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setLevel(numeric_level)
        file_handler.setFormatter(formatter)
        root_logger.addHandler(file_handler)

    logging.getLogger("urllib3").setLevel(logging.WARNING)

    logger = logging.getLogger("qp_parser")
    logger.info("Логирование запущено (уровень: %s, файл: %s)", log_level, log_file)
    return logger
