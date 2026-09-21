import java.io.*;
import java.net.*;
import java.util.*;

class SensorData {
    float temperature;
    float humidity;
    float rainfall;

    public SensorData(float temperature, float humidity, float rainfall) {
        this.temperature = temperature;
        this.humidity = humidity;
        this.rainfall = rainfall;
    }
}

class SharedBuffer {
    private final SensorData[] buffer;
    private int in = 0, out = 0, count = 0;
    private final int size;

    public SharedBuffer(int size) {
        this.size = size;
        buffer = new SensorData[size];
    }

    public synchronized void put(SensorData data) throws InterruptedException {
        while (count == size)
            wait();

        buffer[in] = data;
        in = (in + 1) % size;
        count++;
        System.out.printf("[Producer] Produced: %.1f¡ÆC, %.1f%%, %.1fmm\n", data.temperature, data.humidity, data.rainfall);

        notifyAll();
    }

    public synchronized SensorData take() throws InterruptedException {
        while (count == 0)
            wait();

        SensorData data = buffer[out];
        out = (out + 1) % size;
        count--;

        notifyAll();
        return data;
    }
}

class Producer extends Thread {
    private final SharedBuffer buffer;
    private final String urlStr = "https://apihub.kma.go.kr/api/typ01/url/gts_syn1.php?tm=202211301200&dtm=10&stn=47&help=1&authKey=njld-D40Rb25Xfg-NAW9hA";
    private final String fileName = "rainfall.txt";

    public Producer(SharedBuffer buffer) {
        this.buffer = buffer;
    }

    private void downloadFile() throws IOException {
        URL url = new URL(urlStr);
        BufferedInputStream in = new BufferedInputStream(url.openStream());
        FileOutputStream out = new FileOutputStream(fileName);

        byte[] buffer = new byte[1024];
        int count;
        while ((count = in.read(buffer, 0, 1024)) != -1) {
            out.write(buffer, 0, count);
        }

        in.close();
        out.close();
    }

    public void run() {
        try {
            downloadFile();

            BufferedReader reader = new BufferedReader(new FileReader(fileName));
            String line;
            while ((line = reader.readLine()) != null) {
                if (line.startsWith("#") || line.trim().length() < 20) continue;

                String[] tokens = line.trim().split(" +");
                if (tokens.length < 18) continue;

                float temp = Float.parseFloat(tokens[10]);
                float hum = Float.parseFloat(tokens[12]);
                float rain = Float.parseFloat(tokens[17]);

                buffer.put(new SensorData(temp, hum, rain));
                Thread.sleep(1000);
            }

            reader.close();
        } catch (Exception e) {
            System.err.println("Producer error: " + e.getMessage());
        }
    }
}

class Consumer extends Thread {
    private final SharedBuffer buffer;

    public Consumer(SharedBuffer buffer) {
        this.buffer = buffer;
    }

    public void run() {
        try {
            while (true) {
                SensorData data = buffer.take();

                System.out.printf("[Consumer] Consumed: %.1f¡ÆC, %.1f%%, %.1fmm\n", data.temperature, data.humidity, data.rainfall);

                if (data.temperature > 30.0)
                    System.out.println("[Warning] High Temperature Alert!");
                if (data.humidity > 80.0)
                    System.out.println("[Warning] High Humidity Alert!");
                if (data.rainfall > 30.0)
                    System.out.println("[Warning] Heavy Rainfall Alert!");

                Thread.sleep(2000);
            }
        } catch (Exception e) {
            System.err.println("Consumer error: " + e.getMessage());
        }
    }
}

public class WeatherMonitor {
    public static void main(String[] args) {
        SharedBuffer buffer = new SharedBuffer(5);
        Thread producer = new Producer(buffer);
        Thread consumer = new Consumer(buffer);

        producer.start();
        consumer.start();
    }
}
