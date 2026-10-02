from abc import ABC, abstractmethod


class Contenu(ABC):

    @abstractmethod
    def charger(self):
        pass