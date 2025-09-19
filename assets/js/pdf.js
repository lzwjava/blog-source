document.addEventListener("DOMContentLoaded", function () {

    var downloadPdfButton = document.getElementById('downloadPdfButton');
    if (downloadPdfButton) {
        downloadPdfButton.addEventListener('click', function (event) {
            event.preventDefault(); // Prevent default anchor behavior

            // Extract the base filename without the extension
            var filePath = downloadPdfButton.getAttribute('data-file-path'); // e.g., "pages/donate-en.md"
            var fileName = filePath.split('/').pop().replace('.md', ''); // e.g., "donate-en"
            var lang = fileName.split('-').pop(); // e.g., "en"
            var baseName = fileName.replace('-' + lang, ''); // e.g., "donate"


            // Set the PDF source to the corresponding PDF file
            var pdfFile = '/assets/pdfs/' + lang + '/' + baseName + '-' + lang + '.pdf'; // e.g., "/assets/pdfs/en/donate-en.pdf"


            // Initiate the download or open the PDF in a new tab
            window.open(pdfFile, '_blank');
        });
    }
});
