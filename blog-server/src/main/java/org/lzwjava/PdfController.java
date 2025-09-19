package org.lzwjava;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.file.Files;
import java.util.UUID;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

@RestController
@RequestMapping("/api")
public class PdfController {

    @PostMapping(
            value = "/pdf",
            consumes = MediaType.MULTIPART_FORM_DATA_VALUE,
            produces = MediaType.APPLICATION_PDF_VALUE)
    public ResponseEntity<byte[]> pdf(
            @RequestParam("file") MultipartFile markdownFile,
            @RequestParam(value = "dryRun", defaultValue = "false") boolean dryRun)
            throws IOException, InterruptedException {

        if (markdownFile.isEmpty()) {
            return ResponseEntity.badRequest().body("No file uploaded".getBytes());
        }

        // Create temporary files using absolute paths
        String tempDir = System.getProperty("java.io.tmpdir");
        String originalFileName = markdownFile.getOriginalFilename();
        String tempMarkdownPath = tempDir + File.separator + "temp_" + UUID.randomUUID() + ".md";
        String tempPdfPath = tempDir + File.separator + "temp_" + UUID.randomUUID() + ".pdf";

        // Save uploaded Markdown file temporarily
        File tempMarkdownFile = new File(tempMarkdownPath);
        markdownFile.transferTo(tempMarkdownFile);

        if (dryRun) {
            String message = "Dry run: Would generate PDF from: " + originalFileName;
            deleteTempFile(tempMarkdownFile);
            return ResponseEntity.ok().body(message.getBytes());
        }

        // Determine font based on language and platform
        String cjkFont = determineFont(originalFileName);
        String geometry = "left=1.4cm, top=.8cm, right=1.4cm, bottom=1.8cm, footskip=.5cm";

        // Build Pandoc command
        String[] command = {
            "pandoc",
            tempMarkdownPath,
            "-o",
            tempPdfPath,
            "-f",
            "markdown",
            "--pdf-engine",
            "xelatex",
            "-V",
            "romanfont=" + cjkFont,
            "-V",
            "mainfont=" + cjkFont,
            "-V",
            "CJKmainfont=" + cjkFont,
            "-V",
            "CJKsansfont=" + cjkFont,
            "-V",
            "CJKmonofont=" + cjkFont,
            "-V",
            "geometry:" + geometry,
            "-V",
            "classoption=16pt",
            "-V",
            "CJKoptions=Scale=1.1",
            "-V",
            "linestretch=1.5"
        };

        // Execute Pandoc command
        ProcessBuilder processBuilder = new ProcessBuilder(command);
        processBuilder.redirectErrorStream(true);
        Process process = processBuilder.start();
        int exitCode = process.waitFor();

        // Capture output and error output
        StringBuilder output = new StringBuilder();
        StringBuilder errorOutput = new StringBuilder();
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()))) {
            String line;
            while ((line = reader.readLine()) != null) {
                output.append(line).append(System.lineSeparator());
            }
        }
        try (BufferedReader errorReader = new BufferedReader(new InputStreamReader(process.getErrorStream()))) {
            String errorLine;
            while ((errorLine = errorReader.readLine()) != null) {
                errorOutput.append(errorLine).append(System.lineSeparator());
            }
        }

        // Clean up Markdown temp file
        deleteTempFile(tempMarkdownFile);

        if (exitCode != 0) {
            String errorMessage = "Pandoc failed for " + originalFileName + "\nOutput:\n" + output + "\nError Output:\n"
                    + errorOutput;
            deleteTempFile(new File(tempPdfPath));
            return ResponseEntity.status(500).body(errorMessage.getBytes());
        }

        // Read PDF file and prepare response
        File pdfFile = new File(tempPdfPath);
        byte[] pdfBytes = Files.readAllBytes(pdfFile.toPath());
        deleteTempFile(pdfFile);

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_PDF);
        headers.setContentDispositionFormData("attachment", "output.pdf");

        return ResponseEntity.ok().headers(headers).body(pdfBytes);
    }

    private String determineFont(String fileName) {
        String lang = fileName != null
                ? fileName.substring(fileName.lastIndexOf('-') + 1).replace(".md", "")
                : "en";
        String os = System.getProperty("os.name").toLowerCase();
        boolean isMac = os.contains("mac");

        if (isMac) {
            switch (lang) {
                case "hi":
                    return "Kohinoor Devanagari";
                case "ar":
                    return "Geeza Pro";
                case "en":
                case "fr":
                case "de":
                case "es":
                    return "Helvetica";
                case "zh":
                    return "PingFang SC";
                case "hant":
                    return "PingFang TC";
                case "ja":
                    return "Hiragino Sans";
                default:
                    return "Arial Unicode MS";
            }
        } else {
            switch (lang) {
                case "hi":
                    return "Noto Sans Devanagari";
                case "ar":
                    return "Noto Naskh Arabic";
                case "en":
                case "fr":
                case "de":
                case "es":
                    return "DejaVu Sans";
                case "zh":
                    return "Noto Sans CJK SC";
                case "hant":
                    return "Noto Sans CJK TC";
                case "ja":
                    return "Noto Sans CJK JP";
                default:
                    return "Noto Sans";
            }
        }
    }

    private void deleteTempFile(File file) {
        if (file.exists()) {
            file.delete();
        }
    }
}
