document.addEventListener('DOMContentLoaded', function () {
    fetch('https://www.lzwjava.xyz/bandwidth')
        .then(response => response.json())
        .then(data => {
            var bandwidthData = JSON.parse(data);
            var fiveMinuteData = bandwidthData.interfaces[0].traffic.fiveminute.reverse();
            var firstInterval = fiveMinuteData[0];
            var averageTraffic = (firstInterval.rx + firstInterval.tx) / 2;
            var trafficKBs = (averageTraffic / (5 * 60 * 1024)).toFixed(2);

            var statusButton = document.getElementById('statusHeader');
            if (trafficKBs > 10) {
                statusButton.innerHTML = `
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect>
                        <line x1="8" y1="21" x2="16" y2="21"></line>
                        <line x1="12" y1="17" x2="12" y2="21"></line>
                    </svg>
                `;
            } else {
                statusButton.innerHTML = `
                   <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                     <!-- Bell shape -->
                         <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
                        <!-- Bell bottom -->
                        <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
                        <!-- Slash through bell -->
                        <line x1="4" y1="4" x2="20" y2="20"></line>
                    </svg>
                `;
            }
        })
        .catch(error => {
            console.error('Error fetching bandwidth data:', error);
        });
});
