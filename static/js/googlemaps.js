function initMap() {
        var uluru = {lat: latitude, lng: longitude};
        var map = new google.maps.Map(
        document.getElementById('map'), {zoom: 13, center: uluru});
        var marker = new google.maps.Marker({position: uluru, map: map});
}