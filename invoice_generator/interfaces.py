from abc import ABC, abstractmethod

class InvoiceGenerator(ABC):
    @abstractmethod
    def generate_invoice(self, data):
        pass

