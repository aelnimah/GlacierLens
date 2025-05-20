document.addEventListener("DOMContentLoaded", function () {
    const map = L.map('map').setView([55.0, -58.0], 5);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 18,
        attribution: '© OpenStreetMap'
    }).addTo(map);

    let markerCluster = L.markerClusterGroup();
    map.addLayer(markerCluster);

    function clearMarkers() {
        markerCluster.clearLayers();
    }

    function addMarkers(data) {
        data.forEach(iceberg => {
            const { Latitude, Longitude, ID, Timestamp, SightingMethod, Size, Shape, Source } = iceberg;

            if (Latitude && Longitude) {
                const marker = L.marker([parseFloat(Latitude), parseFloat(Longitude)]);

                const popupContent = `
                    <b>ID:</b> ${ID}<br>
                    <b>Timestamp:</b> ${Timestamp}<br>
                    <b>Size:</b> ${Size}<br>
                    <b>Shape:</b> ${Shape}<br>
                    <b>Sighting Method:</b> ${SightingMethod}<br>
                    <b>Source:</b> ${Source}<br>
                `;

                marker.bindPopup(popupContent);
                markerCluster.addLayer(marker);
            }
        });
    }

    function formatDate(dateString) {
        if (!dateString) return "";
        const date = new Date(dateString);
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const day = String(date.getDate()).padStart(2, '0');
        const year = String(date.getFullYear()).slice(2);
        return `${month}/${day}/${year}`;
    }

    // Fetch initial data
    fetch('/api/data')
        .then(response => response.json())
        .then(addMarkers)
        .catch(error => console.error('Error fetching data:', error));

    document.getElementById('query-btn').addEventListener('click', () => {
        const id = document.getElementById('query-id').value.trim();
        const size = document.getElementById('query-size').value.trim();
        const startTimestamp = formatDate(document.getElementById('start-timestamp').value);
        const endTimestamp = formatDate(document.getElementById('end-timestamp').value);

        fetch(`/api/query?id=${id}&size=${size}&startTimestamp=${startTimestamp}&endTimestamp=${endTimestamp}`)
            .then(response => response.json())
            .then(data => {
                clearMarkers();
                addMarkers(data);
            })
            .catch(error => console.error('Error querying data:', error));
    });
});
