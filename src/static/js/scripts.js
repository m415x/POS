$(document).ready(function(){
    $("#btn__edit").click(function(){
        $(".edit__input")
        .removeAttr('readonly')
        .removeAttr('disabled')
        // .removeClass('form-control-plaintext')
        .addClass('border-bottom');
        $("#btn__edit").hide();
        $(".btn__confirm").removeClass('visually-hidden');
        $(".btn__delete").addClass('visually-hidden');
        $(".btn__file").removeClass('visually-hidden');
    })
})

$(document).ready(function(){
    $("#btn__cancel").click(function(){
        $(".edit__input")
        .attr('readonly', true)
        .attr('disabled', true)
        // .addClass('form-control-plaintext')
        .removeClass('border-bottom');
        $("#btn__edit").show();
        $(".btn__confirm").addClass('visually-hidden');
        $(".btn__delete").removeClass('visually-hidden');
        $(".btn__file").addClass('visually-hidden');
    })
})