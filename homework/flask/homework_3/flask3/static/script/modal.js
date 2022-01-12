$(document).ready(function () {
    $('#task-modal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget); // Button that triggered the modal
        const taskID = button.data('source'); // Extract info from data-* attributes
        const content = button.data('content'); // Extract info from data-* attributes

        const modal = $(this);

        $('#task-form-display').attr('taskID', taskID);

        if (content) {
            modal.find('.form-control').val(content);
        } else {
            modal.find('.form-control').val('');
        }
    })
    $('#submit-task').click(function () {
        const tID = $('#task-form-display').attr('taskID');
        console.log($('#task-modal').find('.form-control').val());
        $.ajax({
            type: 'PATCH',
            url: "/api/v1/todos",
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'title': tID,
                'text': $('#task-modal').find('.form-control').val()
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });
});