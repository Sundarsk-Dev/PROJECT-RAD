import java.util.*;

public class ReservoirSampling {

    // Reservoir sampling for k = 1
    public static <T> T reservoirSample(List<T> stream) {
        if (stream == null || stream.size() == 0) return null;

        Random rand = new Random();

        // Step 1: select the first element by default
        T result = stream.get(0);

        // i starts from 2nd element (index 1)
        for (int i = 1; i < stream.size(); i++) {
            int streamSize = i + 1;

            // Random index from 0 to streamSize-1
            int j = rand.nextInt(streamSize);

            // If j == 0, replace the current result
            if (j == 0) {
                result = stream.get(i);
            }
        }

        return result;
    }

    // Simulation test like Python code
    public static void main(String[] args) {
        List<String> stream = Arrays.asList(
            "Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape"
        );

        int N = stream.size();
        int NUM_RUNS = 100000;

        Map<String, Integer> counts = new HashMap<>();
        for (String item : stream) {
            counts.put(item, 0);
        }

        // Run reservoir sampling many times
        for (int i = 0; i < NUM_RUNS; i++) {
            String selected = reservoirSample(stream);
            counts.put(selected, counts.get(selected) + 1);
        }

        double expected = (double) NUM_RUNS / N;

        System.out.println("--- Reservoir Sampling (k=1) Simulation ---");
        System.out.println("Total Items: " + N + ", Runs: " + NUM_RUNS);
        System.out.printf("Expected Count per Item: %.2f%n%n", expected);

        for (String item : stream) {
            int count = counts.get(item);
            double diff = Math.abs(count - expected);
            System.out.printf(
                "Item: %-12s | Actual Count: %-6d | Deviation: %.2f%n",
                item, count, diff
            );
        }
    }
}
