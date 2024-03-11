// Documentation

// Used BlockingQueue for the order and prepared queues to handle the synchronization between the chefs and waiters.
// BlockingQueue will block the waiter thread from placing an order if the order queue is full, from serving an order if the prepared queue is empty, 
// and the chef thread from preparing an order if the order queue is empty.
// Blocking queues are thread-safe and provide the necessary synchronization for the waiters and chefs to place and prepare orders.

// Used AtomicInteger variables ordersPlaced and ordersPrepared to keep track of the number of orders placed and prepared. 
// This is necessary to keep track of the number of orders placed and prepared by the waiters and chefs in a thread-safe manner.

// In the main method, existing log.txt file is deleted (for new set of logs), the queues are initialised, config file is read, and the waiter and chef threads are started. 
// A CountDownLatch variable is used to wait for all the threads to finish before exiting the program.

// The log function is synchronized on a class-level variable logLock to ensure that the log messages are written to the 
// file in a thread-safe manner.

// The Order class is used to create order objects with unique ids. The id is incremented in a synchronized block to ensure
// that the ids are unique.

// The Waiter and Chef classes implement the Runnable interface and override the run method. The run method contains the
// logic for placing and preparing orders. The waiter and chef threads are terminated when all orders are served.

// In the waiter thread, there is an infinite while loop. In each iteration, the waiter checks if the prepared queue is full
// or there are no more orders to be placed.If so, and if the prepared queue is empty and all orders are prepared, the loop is broken. 
// Otherwise the waiter serves an order from the prepared queue.
// Else the waiter creates a new order object and places it in the order queue. The number of orders placed is incremented.

// In the chef thread, there is an infinite while loop. In each iteration, the chef takes an order from the order queue and prepares it.
// The prepared order is then placed in the prepared queue. The number of orders prepared is incremented. If all orders are prepared, the loop is broken.

// The logic is written this way as the time taken to place an order is significantly less than the time taken to prepare an order,
// hence the waiter can place multiple orders while the chef prepares an order and orders can be served if the prepared queue
// is at capacity or there are no more orders to be placed. Especially when the prepared queue size is small, this is optimal.


import java.util.concurrent.*;
import java.util.concurrent.atomic.AtomicInteger;
import java.io.*;
import java.util.*;

public class restaurant {
    // variables for configuration values
    private static int NUM_CHEFS;
    private static int NUM_WAITERS;
    private static int NUM_ORDERS;
    private static long TIME_PLACEMENT;
    private static long TIME_PREPARATION;
    private static long TIME_SERVING;
    private static int ORDER_QUEUE_SIZE;
    private static int PREPARED_QUEUE_SIZE;

    // queues for placing and preparing orders
    private static BlockingQueue<Order> orderQueue;
    private static BlockingQueue<Order> preparedQueue;

    // atomic variable to track the number of orders placed
    private static AtomicInteger ordersPlaced = new AtomicInteger(0);
    private static AtomicInteger ordersPrepared = new AtomicInteger(0);

    // synchronization control for chefs and waiters
    private static CountDownLatch latch;

    private static final Object logLock = new Object(); // class-level variable for log synchronization

    public static void main(String[] args) {

        // if log.txt exists, delete it
        File logFile = new File("log.txt");
        if (logFile.exists()) {
            logFile.delete();
        }
        // read configuration from file
        readConfig();

        // initialize queues
        orderQueue = new LinkedBlockingQueue<>(ORDER_QUEUE_SIZE);
        preparedQueue = new LinkedBlockingQueue<>(PREPARED_QUEUE_SIZE);

        // initialize CountDownLatch
        latch = new CountDownLatch(NUM_CHEFS + NUM_WAITERS);

        try {
            // start waiter and chef threads
            for (int i = 0; i < NUM_WAITERS; i++) {
                new Thread(new Waiter(i), "Waiter-" + i).start();
            }
            for (int i = 0; i < NUM_CHEFS; i++) {
                new Thread(new Chef(i), "Chef-" + i).start();
            }

            // wait for all threads to finish
            latch.await();

            // termination message
            System.out.println("All orders are served. Restaurant is closed now.");

            // exit the program
            System.exit(0);

        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

   // method to read config.txt
    private static void readConfig() {
        File configFile = new File("config.txt");

        try (Scanner scanner = new Scanner(configFile)) {
            while (scanner.hasNextLine()) {
                // remove leading and trailing whitespaces
                String line = scanner.nextLine().trim();
                
                // if there are empty lines or lines without numbers, throw exception
                if (line.isEmpty() || !Character.isDigit(line.charAt(0))) {
                    throw new IOException("An error occured while reading config.txt file.");
                }
                
                // remove comments (if any)
                if (line.contains("#")) {
                    line = line.substring(0, line.indexOf('#')).trim();
                }
                
                // use another Scanner to read the number
                try (Scanner lineScanner = new Scanner(line)) {
                    if (NUM_CHEFS == 0) { 
                        NUM_CHEFS = lineScanner.nextInt();
                    } else if (NUM_WAITERS == 0) {
                        NUM_WAITERS = lineScanner.nextInt();
                    } else if (NUM_ORDERS == 0) {
                        NUM_ORDERS = lineScanner.nextInt();
                    } else if (TIME_PLACEMENT == 0) {
                        TIME_PLACEMENT = lineScanner.nextLong();
                    } else if (TIME_PREPARATION == 0) {
                        TIME_PREPARATION = lineScanner.nextLong();
                    } else if (TIME_SERVING == 0) {
                        TIME_SERVING = lineScanner.nextLong();
                    } else if (ORDER_QUEUE_SIZE == 0) {
                        ORDER_QUEUE_SIZE = lineScanner.nextInt();
                    } else if (PREPARED_QUEUE_SIZE == 0) {
                        PREPARED_QUEUE_SIZE = lineScanner.nextInt();
                    } else {
                        throw new IOException("An error occured while reading config.txt file.");
                    }
                }
            }
            
            if (scanner.ioException() != null) {
                throw scanner.ioException();
            }
        } catch (IOException e) {
            System.err.println("An error occurred while reading config.txt file. Exiting the program.");
            System.exit(1); // terminate the program
        }
    }

    // method to log actions of the waiters and chefs in log.txt
    private static void log(String threadType, int threadId, String action, int orderId) {
        synchronized (logLock) {
            long timeStamp = System.currentTimeMillis();
            String logMessage = String.format("[%d] %s %d: %s - Order %d", timeStamp, threadType, threadId, action,
                    orderId);
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

    // Waiter class
    static class Waiter implements Runnable {
        private int id;

        public Waiter(int id) {
            this.id = id;
        }

        @Override
        public void run() {
            try {
                while(true) {
                    // if prepared queue is full or there are no more orders to be placed
                    if (preparedQueue.size() == PREPARED_QUEUE_SIZE || ordersPlaced.get() >= NUM_ORDERS) {
                        if (preparedQueue.isEmpty() && ordersPrepared.get() >= NUM_ORDERS){
                            break;
                        }
                        Order order = preparedQueue.take();
                        Thread.sleep(TIME_SERVING); // simulate time taken to serve an order
                        log("Waiter", id, "Order Served", order.getId());
                    }
                    // else place orders if there are stil orders to be placed
                    else {
                        Order order = new Order();
                        orderQueue.put(order);
                        log("Waiter", id, "Order Placed", order.getId());
                        ordersPlaced.incrementAndGet(); // increment the number of orders placed
                        Thread.sleep(TIME_PLACEMENT); // simulate time taken to place an order
                    }
                }

            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            } finally {
                latch.countDown();
            }
        }
    
    }
    // Chef class
    static class Chef implements Runnable {
        private int id;

        public Chef(int id) {
            this.id = id;
        }

        @Override
        public void run() {
            try {
                while (true) {
                    Order order = orderQueue.take();
                    Thread.sleep(TIME_PREPARATION); // simulate time taken to prepare an order
                    preparedQueue.put(order); // this will block if queue is full
                    ordersPrepared.incrementAndGet(); // increment the number of orders served
                    log("Chef", id, "Order Prepared", order.getId());
                    // if all orders are prepared, break the loop
                    if (ordersPrepared.get() >= NUM_ORDERS){
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

}