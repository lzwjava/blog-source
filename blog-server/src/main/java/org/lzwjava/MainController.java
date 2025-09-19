package org.lzwjava;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class MainController {

    private static Logger logger = LoggerFactory.getLogger(MainController.class);

    @CrossOrigin(origins = "*")
    @GetMapping("/bandwidth")
    public ResponseEntity<String> getBandwidth(@RequestParam(value = "i", required = false) String networkInterface) {
        try {
            String osName = System.getProperty("os.name").toLowerCase();

            Process process;
            if (osName.contains("mac")) {
                process = new ProcessBuilder("ifconfig", "en0").start();
            } else {
                process = new ProcessBuilder("vnstat", "-i", networkInterface, "-5", "--json").start();
            }

            logger.info("getBandwidth: Executing command for OS: {}", osName);

            StringBuilder output = new StringBuilder();
            StringBuilder errorOutput = new StringBuilder();

            // Capture standard output
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()))) {
                String line;
                while ((line = reader.readLine()) != null) {
                    output.append(line).append(System.lineSeparator());
                }
            }

            // Capture error output
            try (BufferedReader errorReader = new BufferedReader(new InputStreamReader(process.getErrorStream()))) {
                String errorLine;
                while ((errorLine = errorReader.readLine()) != null) {
                    errorOutput.append(errorLine).append(System.lineSeparator());
                }
            }

            int exitCode = process.waitFor();
            if (exitCode != 0) {
                // Prioritize stdout for JSON errors, fallback to stderr
                String errorResponse = output.length() > 0 ? output.toString() : errorOutput.toString();
                return ResponseEntity.status(500).body(errorResponse);
            }

            return ResponseEntity.ok(output.toString());

        } catch (IOException e) {
            return ResponseEntity.status(500).body("Error executing command: " + e.getMessage());
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            return ResponseEntity.status(500).body("Command execution interrupted: " + e.getMessage());
        }
    }
}
