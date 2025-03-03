package org.lzwjava;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

@RestController
public class HelloController {

    @CrossOrigin(origins = "*")
    @GetMapping("/bandwidth")
    public ResponseEntity<String> getBandwidth() {
        try {
            String osName = System.getProperty("os.name").toLowerCase();
            Process process;
            if (osName.contains("mac")) {
                // macOS: Use a different method, e.g., ifconfig or iperf
                // Example using ifconfig (may require parsing to extract relevant data)
                process = new ProcessBuilder("ifconfig", "en0").start(); // en0 is usually the primary network interface on macOS
            } else {
                // Linux: Use vnstat
                process = new ProcessBuilder("vnstat", "-i", "eth0", "-5", "--json").start();
            }

            StringBuilder output = new StringBuilder();
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()))) {
                String line;
                while ((line = reader.readLine()) != null) {
                    output.append(line).append("\n"); // Append newline to preserve formatting
                }
            }

            int exitCode = process.waitFor();
            if (exitCode != 0) {
                return ResponseEntity.status(500).body("Command failed with exit code: " + exitCode);
            }

            // Return the captured data as a JSON response
            return ResponseEntity.ok(output.toString());

        } catch (IOException | InterruptedException e) {
            return ResponseEntity.status(500).body("Error executing command: " + e.getMessage());
        }
    }
}