const nytimesDiv = document.querySelector('.nytimes');

if (nytimesDiv) {
    const updateButton = document.createElement('button');
    updateButton.textContent = 'Update NYTimes Articles';
    nytimesDiv.appendChild(updateButton);

    updateButton.addEventListener('click', () => {
        fetch('https://api.github.com/repos/lzwjava/lzwjava.github.io/actions/workflows/nytimes.yml/dispatches', {
            method: 'POST',
            headers: {
                'Accept': 'application/vnd.github+json',
                'Authorization': 'Bearer token',
                'X-GitHub-Api-Version': '2022-11-28',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ ref: 'main' })
        })
        .then(response => {
            if (response.status === 204) {
                alert('Update triggered successfully! Please wait a few minutes to see the result.');
            } else {
                alert(`Update failed. Status code: ${response.status}`);
                console.error('Update failed:', response);
            }
        })
        .catch(error => {
            alert('Update failed. Check the console for errors.');
            console.error('Error triggering update:', error);
        });
    });
} else {
    console.error("nytimes div not found!");
}
