// $(document).ready(function () {
//     $("#searchInput").on('keyup', function (event) {
//         let text = $(this).val();
//         console.log(text);
//     })
//
// });
$(document).ready(function () {
    $('#searchInput').on('keyup', function (event) {
        $("#searchResults").empty();
        let filter_text = $(this).val();
        console.log(filter_text)
        $.ajax(
            {
                type: "GET",
                url: "/api/v1/search",
                data: {"q": filter_text},
                success: function (response) {
                    for (let item of response) {
                        console.log(item)
                        if (item.name) {
                            let li_name = "<li>" + item.name + "</li>";
                            $('#searchResults').append(li_name);
                        }
                        if (item.email) {
                            let li_email = "<li>" + item.email + "</li>";
                            $('#searchResults').append(li_email);
                        }
                        if (item.location) {
                            let li_location = "<li>" + item.location + "</li>";
                            $('#searchResults').append(li_location);
                        }
                        if (item.city) {
                            let li_city = "<li>" + item.city + "</li>";
                            $('#searchResults').append(li_city);
                        }
                        if (item.address) {
                            let li_address = "<li>" + item.address + "</li>";
                            $('#searchResults').append(li_address);
                        }
                    }
                }
            }
        )
    })
});

$(document).on("click", "#searchInput", function (e) {
    $("#searchResults").empty();
});
