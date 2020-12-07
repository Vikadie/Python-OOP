from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
        except IndexError:
            return "Hardware does not exist"
        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(express_software)
            System._software.append(express_software)
        except Exception as exc:
            return str(exc)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
        except IndexError:
            return "Hardware does not exist"
        light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(light_software)
            System._software.append(light_software)
        except Exception as exc:
            return str(exc)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = [s for s in System._software if s.name == software_name][0]
        except IndexError:
            return "Some of the components do not exist"
        if hardware.uninstall(software):
            System._software.remove(software)

    @staticmethod
    def analyze():
        return f"""System Analysis
Hardware Components: {len(System._hardware)}
Software Components: {len(System._software)}
Total Operational Memory: {sum([s.memory_consumption  
                                for s in System._software])} / {sum([h.memory for h in System._hardware])}
Total Capacity Taken: {sum([s.capacity_consumption 
                            for s in System._software])} / {sum([h.capacity for h in System._hardware])}"""

    @staticmethod
    def system_split():
        output = ''
        for hardware in System._hardware:
            output += f"Hardware Component - {hardware.name}\n"
            count_express_software = len([s for s in hardware.software_components if s.type == "Express"])
            output += f"Express Software Components: {count_express_software}\n"
            count_light_software = len([s for s in hardware.software_components if s.type == "Light"])
            output += f"Light Software Components: {count_light_software}\n"
            output += f"Memory Usage: {sum([s.memory_consumption for s in hardware.software_components])} / {hardware.memory}\n"
            output += f"Capacity Usage: {sum([s.capacity_consumption for s in hardware.software_components])} / {hardware.capacity}\n"
            output += f"Type: {hardware.type}\n"
            output += f"Software Components: {hardware.get_software_components()}"
        return output
