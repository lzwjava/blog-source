document.addEventListener('DOMContentLoaded', function () {
    fetch('https://lzwjava.shop/bandwidth?i=eth0')
        .then(response => response.json())
        .then(data => {
            // console.log(data);
            //var bandwidthData = JSON.parse(data);
            var bandwidthData = data;

            // Create a container for the times
            var timesContainer = document.createElement('div');

            var currentUtcTime = new Date();
            var currentLocalTime = new Date(currentUtcTime.getTime());

            var pUtcTime = document.createElement('p');
            pUtcTime.textContent = `UTC Time: ${currentUtcTime.toUTCString()}`;
            timesContainer.appendChild(pUtcTime);

            var pLocalTime = document.createElement('p');
            pLocalTime.textContent = `My Local Time: ${currentLocalTime.toString()}`;
            timesContainer.appendChild(pLocalTime);

            // Append the times container to the status div
            document.getElementById('status').appendChild(timesContainer);

            // Create a table
            var table = document.createElement('table');
            table.border = '1';
            table.style.borderCollapse = 'collapse';
            table.style.width = '100%';

            // Create table header
            var thead = document.createElement('thead');
            var tr = document.createElement('tr');
            var headers = ['Time', 'Traffic (KB/s)', 'Status'];
            headers.forEach(headerText => {
                var th = document.createElement('th');
                th.textContent = headerText;
                tr.appendChild(th);
            });
            thead.appendChild(tr);
            table.appendChild(thead);

            // Create table body
            var tbody = document.createElement('tbody');

            // Process traffic data
            var fiveMinuteData = bandwidthData.interfaces[0].traffic.fiveminute.reverse();
            var maxRows = 100;
            var rowsAdded = 0;

            fiveMinuteData.forEach(interval => {
                if (rowsAdded >= maxRows) {
                    return; // Stop adding more rows if the limit is reached
                }

                var tr = document.createElement('tr');

                var dataTime = new Date(Date.UTC(interval.date.year, interval.date.month - 1, interval.date.day, interval.time.hour, interval.time.minute));
                var timeDifference = Math.round((currentUtcTime - dataTime) / (1000 * 60)); // Time difference in minutes

                var tdTimeDifference = document.createElement('td');
                tdTimeDifference.textContent = timeDifference + 'm ago';
                tr.appendChild(tdTimeDifference);

                var averageTraffic = (interval.rx + interval.tx) / 2; // Calculate average of RX and TX
                var tdTrafficKBs = document.createElement('td');
                var trafficKBs = (averageTraffic / (5 * 60 * 1024)).toFixed(2); // Convert to KB/s
                tdTrafficKBs.textContent = trafficKBs;
                tr.appendChild(tdTrafficKBs);

                var tdStatus = document.createElement('td');
                tdStatus.textContent = trafficKBs > 7 ? 'Online' : 'Offline';
                tdStatus.className = trafficKBs > 7 ? 'status-online' : 'status-offline';
                tr.appendChild(tdStatus);

                tbody.appendChild(tr);
                rowsAdded++;
            });
            table.appendChild(tbody);

            // Append the table to the status div
            document.getElementById('status').appendChild(table);
        })
        .catch(error => {
            console.error('Error fetching bandwidth data:', error);
        });
});
