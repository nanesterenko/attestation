from abc import ABC, abstractmethod


class Shops(ABC):
    """Интерфейс общий для всех магазинов."""
    @abstractmethod
    def get_catalog(self):
        pass


class Luckycosmetic(Shops):
    def get_catalog(self):
        print("Получить каталог магазина Luckycosmetic")


class Mykoreashops(Shops):
    def get_catalog(self):
        print("Получить каталог магазина Mykoreashops")


class Holyyskin(Shops):
    def get_catalog(self):
        print("Получить каталог магазина Holyyskin")


class AggregatorMediator(ABC):
    """Создаем посредника, согласно соответствующему шаблону."""
    @abstractmethod
    def get_catalog(self):
        pass

    @abstractmethod
    def return_goods_to_user(self):
        pass


class Aggregator(AggregatorMediator):
    """Реализация конкретной логики взаимодействия."""
    def get_catalog(self):
        print("Получаем каталоги всех доступных магазинов")

    def return_goods_to_user(self):
        print("Возвращаем результаты поиска")


class User():
    """Пользователь нужен для общения с посредником."""
    def look_for_goods(self):
        print("Выполняет поиск товара")