from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, temperature):
        pass

class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

class TemperatureSensor(Subject):
    def __init__(self):
        self._observers = []
        self._temperature = 0

    def register_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature):
        self._temperature = temperature
        self.notify_observers()

# Factory Pattern

class TemperatureSensorFactory:
    def create_temperature_sensor(self, city):
        return CityTemperatureSensor(city)

# Concrete Temperature Sensors

class CityTemperatureSensor(Observer):
    def __init__(self, city):
        self._city = city

    def update(self, temperature):
        print(f"Temperature in {self._city}: {temperature}°C")

# Client code

if __name__ == "__main__":
    temperature_sensor = TemperatureSensor()
    factory = TemperatureSensorFactory()

    observer1 = CityTemperatureSensor("New York")
    observer2 = CityTemperatureSensor("Los Angeles")

    temperature_sensor.register_observer(observer1)
    temperature_sensor.register_observer(observer2)

    temperature_sensor.set_temperature(25)