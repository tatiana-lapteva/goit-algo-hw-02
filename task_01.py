"""
Завдання 1
Потрібно розробити програму, яка імітує приймання й обробку заявок: програма має автоматично генерувати нові заявки
(ідентифіковані унікальним номером або іншими даними), додавати їх до черги, а потім послідовно видаляти з черги для
"обробки", імітуючи таким чином роботу сервісного центру.
"""

from queue import Queue
import random
from time import sleep


class Request:
  def __init__(self):
    self.request_id = random.randint(1000, 9999)

  def __str__(self):
        return f"{self.request_id}"

class Processing:
    def __init__(self):
        self.processing_requests = Queue()

    def generate_request(self,):
        """ generate new request and add to queue """
        request_id = Request()
        self.processing_requests.put(request_id)
        print(f"Request ID {request_id} added to queue")


    def process_request(self):
        """ process queue items """
        while not self.processing_requests.empty():
            current_request = self.processing_requests.get()
            print("Processing ", current_request)
            sleep(random.uniform(0.5, 2.0))
        else:
            print("Queue is empty")


if __name__ == "__main__":
    try:
        processing = Processing()
        while True:
            for i in range(5):
                request_id = processing.generate_request()

            processing.process_request()

    except KeyboardInterrupt:
        print("\nThe processing is stopped")




