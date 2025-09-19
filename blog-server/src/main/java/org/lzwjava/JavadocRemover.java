package org.lzwjava;

import java.io.IOException;
import java.nio.file.FileVisitResult;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.SimpleFileVisitor;
import java.nio.file.attribute.BasicFileAttributes;
import java.util.regex.Pattern;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class JavadocRemover {

    private static final Logger logger = LoggerFactory.getLogger(JavadocRemover.class);

    private JavadocRemover() {
        throw new IllegalStateException("Utility class");
    }

    public static void main(String[] args) {
        if (args.length > 0) {
            String directoryPath = args[0];
            removeJavadocFromDirectory(directoryPath);
        } else {
            logger.error("Please provide a directory path as a command-line argument.");
        }
    }

    public static void removeJavadocFromDirectory(String directoryPath) {
        Path startPath = Paths.get(directoryPath);
        try {
            Files.walkFileTree(startPath, new SimpleFileVisitor<Path>() {
                @Override
                public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) {
                    if (file.toString().endsWith(".java")) {
                        removeJavadocFromFile(file);
                    }
                    return FileVisitResult.CONTINUE;
                }
            });
        } catch (IOException e) {
            logger.error("Error walking the file tree", e);
        }
    }

    private static void removeJavadocFromFile(Path filePath) {
        try {
            String content = new String(Files.readAllBytes(filePath));
            Pattern pattern = Pattern.compile("/\\*\\*.*?\\*/", Pattern.DOTALL);
            content = pattern.matcher(content).replaceAll("");
            Files.write(filePath, content.getBytes());
        } catch (IOException e) {
            logger.error("Error removing Javadoc from file: {}", filePath, e);
        }
    }
}
