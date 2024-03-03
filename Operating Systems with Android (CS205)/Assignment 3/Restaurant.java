import java.util.concurrent.*;
import java.util.concurrent.atomic.AtomicInteger;
import java.io.*;
import java.util.*;

public class Restaurant {
    // Variables for configuration values
    private static int NUM_CHEFS;
    private static int NUM_WAITERS;
    private static int NUM_ORDERS;
    private static long TIME_PLACEMENT;
    private static long TIME_PREPARATION;
    private static long TIME_SERVING;
    private static int ORDER_QUEUE_SIZE;
    private static int PREPARED_QUEUE_SIZE;

    // Queues for placing and preparing orders
    private static BlockingQueue<Order> orderQueue;
    private static BlockingQueue<Order> preparedQueue;

    // Atomic variable to track the number of orders placed
    private static AtomicInteger ordersPlaced = new AtomicInteger(0);

    // Synchronization control for chefs and waiters
    private static CountDownLatch latch;

    private static final Object logLock = new Object(); // Class-level variable for log synchronization

    public static void main(String[] args) {
        // Read configuration from file
        readConfig();

        // Initialize queues
        orderQueue = new LinkedBlockingQueue<>(ORDER_QUEUE_SIZE);
        preparedQueue = new LinkedBlockingQueue<>(PREPARED_QUEUE_SIZE);

        // Initialize CountDownLatch
        latch = new CountDownLatch(NUM_CHEFS + NUM_WAITERS);

        try {
            // Start waiter and chef threads
            for (int i = 0; i < NUM_WAITERS; i++) {
                new Thread(new Waiter(i), "Waiter-" + i).start();
            }
            for (int i = 0; i < NUM_CHEFS; i++) {
                new Thread(new Chef(i), "Chef-" + i).start();
            }

            // Wait for all threads to finish
            latch.await();

            // Termination message
            System.out.println("All orders are served. Restaruant is closed now.");

            // Exit the program
            System.exit(0);

        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    // Method to read configuration from a file
    private static void readConfig() {
        try (Scanner scanner = new Scanner(new File("config.txt"))) {
            NUM_CHEFS = scanner.nextInt();
            NUM_WAITERS = scanner.nextInt();
            NUM_ORDERS = scanner.nextInt();
            TIME_PLACEMENT = scanner.nextLong();
            TIME_PREPARATION = scanner.nextLong();
            TIME_SERVING = scanner.nextLong();
            ORDER_QUEUE_SIZE = scanner.nextInt();
            PREPARED_QUEUE_SIZE = scanner.nextInt();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void log(String threadType, int threadId, String action, int orderId) {
        synchronized (logLock) {
            long timeStamp = System.currentTimeMillis();
            String logMessage = String.format("[%d] %s %d: %s - Order %d", timeStamp, threadType, threadId, action, orderId);
            try (FileWriter writer = new FileWriter("log.txt", true)) {
                writer.write(logMessage + "\n");
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    // Order class
    static class Order {
        private static int lastId = -1;
        private int id;

        public Order() {
            synchronized (Order.class) { // Synchronize on the class object
                this.id = ++lastId;
            }
        }

        public int getId() {
            return id;

        }
    }

    static class Waiter implements Runnable {
        private int id;
    
        public Waiter(int id) {
            this.id = id;
        }
    
        @Override
        public void run() {
            try {
                while (ordersPlaced.get() < NUM_ORDERS) { 
                    Thread.sleep(TIME_PLACEMENT); // Simulate time to place an order
                    Order order = new Order();
                    ordersPlaced.incrementAndGet(); // Increment the number of orders placed
                    orderQueue.put(order); // This will block if queue is full
                    log("Waiter", id, "Order Placed", order.getId());
                }

                while (true) {
                    Order servedOrder = preparedQueue.take(); // This will block if queue is empty
                    Thread.sleep(TIME_SERVING); // Simulate time to serve an order
                    log("Waiter", id, "Order Served", servedOrder.getId());

                    // Break the loop if all orders are served
                    if (Order.lastId == NUM_ORDERS && preparedQueue.isEmpty()) {
                        break;
                    }
                }
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            } finally {
                latch.countDown();
            }
        }
    }
    

    static class Chef implements Runnable {
        private int id;

        public Chef(int id) {
            this.id = id;
        }

        @Override
        public void run() {
            try {
                while (true) { 
                    Order order = orderQueue.take(); // Poll with a timeout
                    
                        // break the loop if all orders are placed and the queue is empty
                        if (Order.lastId >= NUM_ORDERS) {
                            break;
                        }
                       
                    
                    Thread.sleep(TIME_PREPARATION); // simulate time taken to prepare an order
                    preparedQueue.put(order); // this will block if queue is full
                    log("Chef", id, "Order Prepared", order.getId());
                }
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            } finally {
                latch.countDown();
            }
        }
    }
}
