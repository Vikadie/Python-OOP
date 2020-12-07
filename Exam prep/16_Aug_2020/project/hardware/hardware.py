from project.software.software import Software


class Hardware:
    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software: Software):
        # check available the capacity and memory for each installation
        memory_remained = self.memory - sum([s.memory_consumption for s in self.software_components])
        capacity_remained = self.capacity - sum([s.capacity_consumption for s in self.software_components])
        if (software.memory_consumption > memory_remained) or (software.capacity_consumption > capacity_remained):
            raise Exception("Software cannot be installed")
        self.software_components.append(software)

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)
            return True
        return False

    def get_software_components(self):
        if self.software_components:
            return ', '.join([s.name for s in self.software_components])
        return  # return 'None'
