package scripts.benchmark;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

public class MultiMark {
    public static void parallelSort(int[] arr, int threadCount) throws InterruptedException {
        int len = arr.length;
        int chunkSize = (len + threadCount - 1) / threadCount;
        Thread[] threads = new Thread[threadCount];

        // Sort each chunk in a separate thread
        for (int i = 0; i < threadCount; i++) {
            final int start = i * chunkSize;
            final int end = Math.min(start + chunkSize, len);
            threads[i] = new Thread(() -> Arrays.sort(arr, start, end));
            threads[i].start();
        }
        for (Thread t : threads) {
            t.join();
        }

        // Merge sorted chunks
        int[] result = arr;
        int currentChunks = threadCount;
        while (currentChunks > 1) {
            int mergedChunks = (currentChunks + 1) / 2;
            Thread[] mergeThreads = new Thread[mergedChunks];
            int[] mergedArr = new int[len];

            for (int i = 0; i < mergedChunks; i++) {
                final int leftStart = i * 2 * chunkSize;
                final int leftEnd = Math.min(leftStart + chunkSize, len);
                final int rightStart = leftEnd;
                final int rightEnd = Math.min(rightStart + chunkSize, len);
                final int[] currentResult = result; // Make result effectively final for lambda

                mergeThreads[i] = new Thread(() -> {
                    int l = leftStart, r = rightStart, idx = leftStart;
                    while (l < leftEnd && r < rightEnd) {
                        if (currentResult[l] <= currentResult[r]) {
                            mergedArr[idx++] = currentResult[l++];
                        } else {
                            mergedArr[idx++] = currentResult[r++];
                        }
                    }
                    while (l < leftEnd) mergedArr[idx++] = currentResult[l++];
                    while (r < rightEnd) mergedArr[idx++] = currentResult[r++];
                });
                mergeThreads[i].start();
            }
            for (Thread t : mergeThreads) t.join();
            result = mergedArr;
            chunkSize *= 2;
            currentChunks = mergedChunks;
        }
        System.arraycopy(result, 0, arr, 0, len);
    }

    public static double benchmark(int threadCount, int listSize) throws InterruptedException {
        Random rand = new Random();
        int[] arr = new int[listSize];
        for (int i = 0; i < listSize; i++) {
            arr[i] = rand.nextInt(1_000_001);
        }
        long start = System.nanoTime();
        parallelSort(arr, threadCount);
        long end = System.nanoTime();
        return (end - start) / 1e9;
    }

    public static void main(String[] args) throws Exception {
        int cpuCores = Runtime.getRuntime().availableProcessors();
        System.out.println("CPU cores: " + cpuCores);
        int[] threadCounts = {1, 2, 4, 8, 16, 32, 64, 128};
        List<Double> times = new ArrayList<>();
        int listSize = 50_000_000;

        for (int n : threadCounts) {
            double t = benchmark(n, listSize);
            System.out.printf("Threads: %d, Time taken: %.4f seconds%n", n, t);
            times.add(t);
        }

        // Print results as CSV for external plotting
        System.out.println("\nThreadCount,TimeTakenSeconds");
        for (int i = 0; i < threadCounts.length; i++) {
            System.out.printf("%d,%.6f%n", threadCounts[i], times.get(i));
        }
    }
}
