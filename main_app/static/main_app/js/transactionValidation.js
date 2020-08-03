$('#receive_btn').on('click', function (e) {
    $('#receive_l1_hidden').val($('#receive_l1_input').val());
    $('#receive_l2_hidden').val($('#receive_l2_input').val());
    if ($('#receive_accts').children("option:selected").val() == '') {
        e.preventDefault();
        $('#receive_accts').addClass('is-invalid');
    } else {
        $('#receive_accts').removeClass('is-invalid');
    }
    if ($('#receive_l1_input').val() == '') {
        e.preventDefault();
        $('#receive_l1_input').addClass('is-invalid');
    } else {
        $('#receive_l1_input').removeClass('is-invalid');
    }
    if ($('#receive_l2_input').val() == '') {
        e.preventDefault();
        $('#receive_l2_input').addClass('is-invalid');
    } else {
        $('#receive_l2_input').removeClass('is-invalid');
    }
    if ($('#receive_amount_atm').val() == '') {
        e.preventDefault();
        $('#receive_amount_atm').addClass('is-invalid');
    } else {
        $('#receive_amount_atm').removeClass('is-invalid');
    }
})
$('#transfer_btn').on('click', function (e) {
    if ($('#transfer_from_accts').children("option:selected").val() == '') {
        e.preventDefault();
        $('#transfer_from_accts').addClass('is-invalid');
    } else {
        $('#transfer_from_accts').removeClass('is-invalid');
    }
    if ($('#transfer_to_accts').children("option:selected").val() == '') {
        e.preventDefault();
        $('#transfer_to_accts').addClass('is-invalid');
    } else {
        $('#transfer_to_accts').removeClass('is-invalid');
    }
    if ($('#transfer_amount_atm').val() == '') {
        e.preventDefault();
        $('#transfer_amount_atm').addClass('is-invalid');
    } else {
        $('#transfer_amount_atm').removeClass('is-invalid');
    }
})
$('#pay_btn').on('click', function (e) {
    $('#pay_l1_hidden').val($('#pay_l1_input').val());
    $('#pay_l2_hidden').val($('#pay_l2_input').val());
    if ($('#pay_accts').children("option:selected").val() == '') {
        e.preventDefault();
        $('#pay_accts').addClass('is-invalid');
    } else {
        $('#pay_accts').removeClass('is-invalid');
    }
    if ($('#pay_l1_input').val() == '') {
        e.preventDefault();
        $('#pay_l1_input').addClass('is-invalid');
    } else {
        $('#pay_l1_input').removeClass('is-invalid');
    }
    if ($('#pay_l2_input').val() == '') {
        e.preventDefault();
        $('#pay_l2_input').addClass('is-invalid');
    } else {
        $('#pay_l2_input').removeClass('is-invalid');
    }
    if ($('#pay_amount_atm').val() == '') {
        e.preventDefault();
        $('#pay_amount_atm').addClass('is-invalid');
    } else {
        $('#pay_amount_atm').removeClass('is-invalid');
    }
})