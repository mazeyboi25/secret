import threading
import time

def process_order(order_id):
    print(f"Order {order_id}: Verifying order")
    time.sleep(1)

    print(f"Order {order_id}: Processing payment")
    time.sleep(1)

    print(f"Order {order_id}: Packaging item")
    time.sleep(1)

    print(f"Order {order_id}: Ready for shipping")
    time.sleep(1)

    print(f"Order {order_id} completed.\n")


orders = range(1, 11)

threads = []

print("Processing Orders...\n")

for order in orders:
    t = threading.Thread(target=process_order, args=(order,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All orders completed.")
