from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self, name, capacity, memory):
        super().__init__(name=name, type="Power", capacity=int(0.25 * capacity), memory=int(1.75 * memory))
