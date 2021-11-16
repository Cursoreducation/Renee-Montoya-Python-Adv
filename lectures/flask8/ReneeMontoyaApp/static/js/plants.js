$(document).ready(function () {
    $.ajax({
        url: '/api/v1/plants',
        method: 'GET',
        success: function (response) {
            for (let plant of response) {
                let el = " <li class='list-group-item'>" + plant.name + "</li>";
                $('#plants').append(el);
            }
        }
    })
});