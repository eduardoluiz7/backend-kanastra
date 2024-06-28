from abc import ABC, abstractmethod


class EmailSender(ABC):
    @abstractmethod
    def send_email(self, data, email):
        pass