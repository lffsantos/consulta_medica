$( document ).ready(function() {
    $.ajax({
      url: "doctors",
      success: function(data) {
          let result = [''];
          result.push.apply(result, data);
          $('#medicos').select2({
            data: result
          });
          console.log(result);
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
    $( "#limpar" ).click(function( event ) {


    });
    $( "#buscar" ).click(function( event ) {
        $('table>tbody').html('');
        let payload = {};
        let nome_medico = $('#medicos').val();
        if (nome_medico !== ""){
            payload['nome_medico'] = nome_medico;
        }
        let intervalo_consulta = $('input[name="intervalo_consulta"]').val();
        if(intervalo_consulta !== ""){
            payload['intervalo_consulta'] = intervalo_consulta;
        }
        let valor_consulta = $('input[name="valor_consulta"]').val();
        if(valor_consulta !== ""){
            payload['valor_consulta'] = valor_consulta;
        }
        let qtd_exames = $('input[name="qtd_exames"]').val();
        if(qtd_exames !== ""){
            payload['qtd_exames_ate'] = qtd_exames;
        }
        $.ajax({
           url: "report",
           dataType: "json",
           type: "GET",
           contentType: 'application/json; charset=utf-8',
           data: payload,
           async: false,
           success: function(data) {
              console.log(data);
               $.each(data, function (key, value) {
                  let detail = '<tr>' +
                      '<td>' + value['nome_medico'] + '</td>' +
                      '<td>' + value['numero_guia'] + '</td>' +
                      '<td>' + value['dt_consulta'] + '</td>' +
                      '<td>' + value['valor_consulta'].toFixed(2) + '</td>' +
                      '<td>' + value['gasto_consulta'].toFixed(2) + '</td>' +
                      '<td>' + value['qt_exames'] + '</td>' +
                      '</tr>';
                  $('table>tbody').append(detail);
              });
          }
        });
    });
});
