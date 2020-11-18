from pyspectator.processor import Cpu
from datetime import timedelta, datetime
from time import sleep


def generate_report(duration: timedelta):
    cpu = Cpu(monitoring_latency=0.01)

    measurements = []
    with cpu:
        end_time = datetime.now() + duration

        now = datetime.now()
        while datetime.now() < end_time:
            try:
                a = cpu.load
                measurements.append((now, a))
            except:
                pass
            # print(cpu.load, cpu.temperature)
            now = datetime.now()
            sleep(0.02)

    return measurements

