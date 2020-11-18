from datetime import datetime
from typing import Tuple, List

def format_report(report: List[Tuple[datetime, int]]):
    return "\n".join( [
        time.strftime('%H:%M:%S.%f') + ' ' + str(measurements)
        for time, measurements in report]
    )