document.addEventListener('DOMContentLoaded', function () {
    var statusButton = document.getElementById('statusHeader');
    const onlineSVG = `
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect>
            <line x1="8" y1="21" x2="16" y2="21"></line>
            <line x1="12" y1="17" x2="12" y2="21"></line>
        </svg>
    `;
    const offlineSVG = `
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
            <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
            <line x1="4" y1="4" x2="20" y2="20"></line>
        </svg>
    `;

    const now = new Date();
    const currentHour = now.getHours();

    // Set default based on time
    if (currentHour >= 9 && currentHour < 24) {
        statusButton.innerHTML = onlineSVG;
    } else {
        statusButton.innerHTML = offlineSVG;
    }


    fetch('https://lzwjava.shop/bandwidth?i=eth0')
        .then(response => response.json())
        .then(data => {
            var bandwidthData = data;
            var fiveMinuteData = bandwidthData.interfaces[0].traffic.fiveminute.reverse();
            var firstInterval = fiveMinuteData[0];
            var averageTraffic = (firstInterval.rx + firstInterval.tx) / 2;
            var trafficKBs = (averageTraffic / (5 * 60 * 1024)).toFixed(2);


            if (trafficKBs > 7) {
                statusButton.innerHTML = onlineSVG;
            } else {
                statusButton.innerHTML = offlineSVG;
            }
        })
        .catch(error => {
            console.error('Error fetching bandwidth data:', error);
        });
});
