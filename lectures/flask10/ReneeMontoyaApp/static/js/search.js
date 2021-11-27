$(document).ready(function () {
    $("#searchInput").on('keyup', function (event) {
        let text = $(this).val();
        console.log(text);
    })
});