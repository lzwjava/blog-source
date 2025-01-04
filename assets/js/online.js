document.addEventListener('DOMContentLoaded', function () {
    fetch('https://www.lzwjava.xyz/bandwidth')
        .then(response => response.json())
        .then(data => {
            var bandwidthData = JSON.parse(data);

            // Create a table
            var table = document.createElement('table');
            table.border = '1';
            table.style.borderCollapse = 'collapse';
            table.style.width = '100%';

            // Create table header
            var thead = document.createElement('thead');
            var tr = document.createElement('tr');
            var headers = ['UTC Time', 'Local Time', 'Traffic (KB/s)', 'Status'];
            headers.forEach(headerText => {
                var th = document.createElement('th');
                th.textContent = headerText;
                tr.appendChild(th);
            });
            thead.appendChild(tr);
            table.appendChild(thead);

            // Create table body
            var tbody = document.createElement('tbody');
            var fiveMinuteData = bandwidthData.interfaces[0].traffic.fiveminute.reverse();
            fiveMinuteData.forEach(interval => {
                var tr = document.createElement('tr');

                var utcTime = new Date(Date.UTC(interval.date.year, interval.date.month - 1, interval.date.day, interval.time.hour, interval.time.minute));
                var localTime = new Date(utcTime.getTime());

                var tdUtcTime = document.createElement('td');
                tdUtcTime.textContent = `${utcTime.getUTCFullYear().toString().slice(-2)}-${String(utcTime.getUTCMonth() + 1).padStart(2, '0')}-${String(utcTime.getUTCDate()).padStart(2, '0')} ${String(utcTime.getUTCHours()).padStart(2, '0')}:${String(utcTime.getUTCMinutes()).padStart(2, '0')}`;
                tr.appendChild(tdUtcTime);

                var tdLocalTime = document.createElement('td');
                tdLocalTime.textContent = `${localTime.getFullYear().toString().slice(-2)}-${String(localTime.getMonth() + 1).padStart(2, '0')}-${String(localTime.getDate()).padStart(2, '0')} ${String(localTime.getHours()).padStart(2, '0')}:${String(localTime.getMinutes()).padStart(2, '0')}`;
                tr.appendChild(tdLocalTime);

                var averageTraffic = (interval.rx + interval.tx) / 2; // Calculate average of RX and TX
                var tdTrafficKBs = document.createElement('td');
                var trafficKBs = (averageTraffic / (5 * 60 * 1024)).toFixed(2); // Convert to KB/s
                tdTrafficKBs.textContent = trafficKBs;
                tr.appendChild(tdTrafficKBs);

                var tdStatus = document.createElement('td');
                tdStatus.textContent = trafficKBs > 5 ? 'Online' : 'Offline';
                tr.appendChild(tdStatus);

                tbody.appendChild(tr);
            });
            table.appendChild(tbody);

            // Append the table to the status div
            document.getElementById('status').appendChild(table);
        })
        .catch(error => {
            console.error('Error fetching bandwidth data:', error);
        });
});
