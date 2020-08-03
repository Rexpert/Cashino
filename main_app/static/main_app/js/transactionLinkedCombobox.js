$('#transfer_from_accts').on('change', function () {
    $('#transfer_to_accts').find('option:not(:first)').prop('disabled', false);
    var from = $(this).val();
    $('#transfer_to_accts option').filter(function () {
        return this.value == from;
    }).prop("disabled", true);
})
$('#transfer_to_accts').on('change', function () {
    $('#transfer_from_accts').find('option:not(:first)').prop('disabled', false);
    var to = $(this).val();
    $('#transfer_from_accts option').filter(function () {
        return this.value == to;
    }).prop("disabled", true);
})