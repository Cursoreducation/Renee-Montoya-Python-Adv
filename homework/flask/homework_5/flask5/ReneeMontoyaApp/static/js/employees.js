$(document).ready(function () {
    $.ajax({
        url: '/api/v1/employees',
        method: 'GET',
        success: function (response) {
            for (let employee of response) {
                let el = " <li class='list-group-item'>" + employee.name + "</li>";
                $('#employees').append(el);
            }
        }
    })
});
