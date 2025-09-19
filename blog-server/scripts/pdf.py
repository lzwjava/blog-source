import requests

from constants import url

# Path to a local markdown file to upload for testing
markdown_file_path = 'scripts/test.md'  # Change this to your test file path

# Prepare the files and data for the POST request
with open(markdown_file_path, 'rb') as f:
    files = {'file': (markdown_file_path, f, 'text/markdown')}
    data = {'dryRun': 'false'}  # Set to 'true' to test dry run
    response = requests.post(url, files=files, data=data)

# Print the response status and content
print('Status code:', response.status_code)

if response.headers.get('Content-Type') == 'application/pdf':
    with open('target/output.pdf', 'wb') as out_pdf:
        out_pdf.write(response.content)
    print('PDF saved as output.pdf')
else:
    print('Response:', response.text)

