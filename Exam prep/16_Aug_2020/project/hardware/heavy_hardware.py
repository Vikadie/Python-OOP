from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    def __init__(self, name, capacity, memory):
        super().__init__(name=name, type="Heavy", capacity=2 * capacity, memory=int(0.75 * memory))
