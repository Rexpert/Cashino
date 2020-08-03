var receives = JSON.parse(document.getElementById('receives').textContent);
$('#receive_l1').on('change', function () {
    $('#receive_l2').find('option:not(:first)').remove();
    var l1_val = $(this).val();
    var l2_val = $('#receive_l2_input').val();
    if (l1_val == '') {
        if (l2_val != '') {
            $('#receive_l2_input').siblings('.input-group-append').children('.dropdown-toggle').click();
        }
        $('#receive_l2_input').siblings('.input-group-append').prop('disabled', true);
    } else {
        $('#receive_l2_input').siblings('.input-group-append').prop('disabled', false);
        for (i = 0; i < receives.length; i++) {
            if (receives[i]['l1'] == l1_val) {
                for (j = 0; j < receives[i]['l2'].length; j++) {
                    $('#receive_l2').append($('<option>', {
                        value: receives[i]['l2'][j],
                        text: receives[i]['l2'][j],
                    }));
                }
            }
        }
    }
    $('#receive_l2').data('combobox').refresh();
});
var pays = JSON.parse(document.getElementById('pays').textContent);
$('#pay_l1').on('change', function () {
    $('#pay_l2').find('option:not(:first)').remove();
    var l1_val = $(this).val();
    var l2_val = $('#pay_l2_input').val();
    if (l1_val == '') {
        if (l2_val != '') {
            $('#pay_l2_input').siblings('.input-group-append').children('.dropdown-toggle').click();
        }
        $('#pay_l2_input').siblings('.input-group-append').prop('disabled', true);
    } else {
        $('#pay_l2_input').siblings('.input-group-append').prop('disabled', false);
        for (i = 0; i < pays.length; i++) {
            if (pays[i]['l1'] == l1_val) {
                for (j = 0; j < pays[i]['l2'].length; j++) {
                    $('#pay_l2').append($('<option>', {
                        value: pays[i]['l2'][j],
                        text: pays[i]['l2'][j],
                    }));
                }
            }
        }
    }
    $('#pay_l2').data('combobox').refresh();
});