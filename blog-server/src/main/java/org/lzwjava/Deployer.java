package org.lzwjava;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class Deployer {

    private static final Logger logger = LoggerFactory.getLogger(Deployer.class);

    public static void main(String[] args) {
        if (args.length < 4) {
            logger.error("Usage: DeployHelper <JAR_PATH> <REMOTE_PATH> <SERVER_IP> <SSH_USERNAME>");
            System.exit(1);
        }

        String jarPath = args[0];
        String remotePath = args[1];
        String serverIp = args[2];
        String sshUsername = args[3];

        try {
            deployJarToHetzner(jarPath, remotePath, serverIp, sshUsername);
        } catch (IOException | InterruptedException e) {
            logger.error("Error during deployment", e);
        }
    }

    public static void deployJarToHetzner(String jarPath, String remotePath, String serverIp, String sshUsername)
            throws IOException, InterruptedException {
        // Command to transfer the JAR file using SCP
        String[] scpCommand = {"scp", jarPath, sshUsername + "@" + serverIp + ":" + remotePath};
        executeCommand(scpCommand, "JAR file uploaded successfully.");

        // Command to check and kill existing Java process
        String[] pgrepCommand = {"ssh", sshUsername + "@" + serverIp, "pgrep -f 'java -jar'"};
        Process pgrepProcess = new ProcessBuilder(pgrepCommand).start();
        int pgrepExitCode = pgrepProcess.waitFor();

        if (pgrepExitCode == 0) {
            String[] pkillCommand = {"ssh", sshUsername + "@" + serverIp, "pkill -f 'java -jar'"};
            executeCommand(pkillCommand, "Existing Java process killed.");
        } else {
            logger.info("No existing Java process found.");
        }

        // Command to start the JAR file on the server
        String[] startCommand = {
            "ssh", sshUsername + "@" + serverIp, "nohup java -jar " + remotePath + " > app.log 2>&1 &"
        };
        executeCommand(startCommand, "JAR file started on the server.");
    }

    private static void executeCommand(String[] command, String successMessage)
            throws IOException, InterruptedException {
        Process process = new ProcessBuilder(command).redirectErrorStream(true).start();

        BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
        String line;
        while ((line = reader.readLine()) != null) {
            logger.info(line);
        }

        int exitCode = process.waitFor();
        if (exitCode == 0) {
            logger.info(successMessage);
        } else {
            logger.error("Command failed with exit code: " + exitCode);
        }
    }
}
