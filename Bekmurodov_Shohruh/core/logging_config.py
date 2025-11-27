import logging


def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s — %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
