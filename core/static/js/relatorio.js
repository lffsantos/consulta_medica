$( document ).ready(function() {
    $.ajax({
      url: "doctors",
      success: function(data) {
          $('#medicos').select2({
            data: data
          });
          console.log(data);
      }
     });
    $('input[name="intervalo_consulta"]').daterangepicker({
        autoUpdateInput: false,
        locale: {
          cancelLabel: 'Clear',
          format: 'DD/M/Y'
        }
      });
    $('input[name="intervalo_consulta"]').on('apply.daterangepicker', function(ev, picker) {
      $(this).val(picker.startDate.format('DD/MM/YYYY') + ' - ' + picker.endDate.format('DD/MM/YYYY'));
    });

    $('input[name="intervalo_consulta"]').on('cancel.daterangepicker', function(ev, picker) {
      $(this).val('');
    });
});