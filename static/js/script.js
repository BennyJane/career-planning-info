$(function () {
    function render_time() {
        return moment($(this).data('timestamp')).format('lll')
    }

    $('[data-toggle="tooltip-comment"]').tooltip(
        {title: render_time}
    );
});


$(function () {
    function getUrl() {
        return 'ddddddddddd'
    }

    $('.jumbotron [data-toggle="popover"]').popover({header: getUrl})
})


