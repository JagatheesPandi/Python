from pathlib import Path

class PathManager:
    Root = (
        Path(__file__).resolve().parent.parent
    )
    CONFIG = Root / 'config'
    LOGS = Root / 'logs'
    REPORTS = Root / 'reports'
