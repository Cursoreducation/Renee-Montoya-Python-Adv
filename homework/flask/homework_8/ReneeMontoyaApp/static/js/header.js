$(document).ready(function () {
    $.ajax({
        url: '/api/v1/menu-items',
        method: 'GET',
        success: function (response) {
            for (let item of response) {
                let li = "<li class='nav-item'>" +
                    "<a class='nav-link' href='" + item.link + "'>"
                    +  item.name +
                    "</a></li>";
                $('#menuList').append(li);
            }
        }
    })
});
