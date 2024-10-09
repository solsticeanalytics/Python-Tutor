from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_car(self) -> 'Car':
        pass

    @abstractmethod
    def create_engine(self) -> 'Engine':
        pass


class LuxuryCarFactory(AbstractFactory):
    def create_car(self) -> 'Car':
        return LuxuryCar()

    def create_engine(self) -> 'Engine':
        return LuxuryEngine()


class SportsCarFactory(AbstractFactory):
    def create_car(self) -> 'Car':
        return SportsCar()

    def create_engine(self) -> 'Engine':
        return SportsEngine()


class Car(ABC):
    @abstractmethod
    def start(self) -> str:
        pass


class LuxuryCar(Car):
    def start(self) -> str:
        return "Starting the luxury car..."


class SportsCar(Car):
    def start(self) -> str:
        return "Starting the sports car..."


class Engine(ABC):
    @abstractmethod
    def rev(self) -> str:
        pass


class LuxuryEngine(Engine):
    def rev(self) -> str:
        return "Revving the luxury engine..."


class SportsEngine(Engine):
    def rev(self) -> str:
        return "Revving the sports engine..."


def client_code(factory: AbstractFactory) -> None:
    car = factory.create_car()
    engine = factory.create_engine()

    print(car.start())
    print(engine.rev())


if __name__ == "__main__":
    luxury_car_factory = LuxuryCarFactory()
    client_code(luxury_car_factory)

    sports_car_factory = SportsCarFactory()
    client_code(sports_car_factory)