$( document ).ready(function() {
    let selector_intervalo_consulta = $('input[name="intervalo_consulta"]');
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
    selector_intervalo_consulta.daterangepicker({
        autoUpdateInput: false,
        locale: {
          cancelLabel: 'Clear',
          format: 'DD/M/Y'
        }
      });
    selector_intervalo_consulta.on('apply.daterangepicker', function(ev, picker) {
      $(this).val(picker.startDate.format('DD/MM/YYYY') + ' - ' + picker.endDate.format('DD/MM/YYYY'));
    });

    selector_intervalo_consulta.on('cancel.daterangepicker', function(ev, picker) {
      $(this).val('');
    });
    $( "#limpar" ).click(function( event ) {


    });
    let datatable = $('#relatorio').DataTable({
        "order": [],
        data: [],
        columns: [
                    { data: 'nome_medico' },
                    { data: 'numero_guia' },
                    { data: 'dt_consulta' },
                    { data: 'valor_consulta', render: $.fn.dataTable.render.number( ',', '.', 2, 'R$ ' )},
                    { data: 'gasto_consulta' ,render: $.fn.dataTable.render.number( ',', '.', 2, 'R$ ' )},
                    { data: 'qt_exames' }
                ],
        "language": {
            "lengthMenu": "Mostrar _MENU_ resultados por página",
            "zeroRecords": "Nada Encontrado",
            "info": "Mostrando página _PAGE_ of _PAGES_",
            "infoEmpty": "Sem resultados",
            "infoFiltered": "(filtro para _MAX_ registros no total)",
            "search":  "Filtrar:",
            "paginate": {
                "first":      "Primeiro",
                "last":       "Último",
                "next":       "Próximo",
                "previous":   "Anterior"
            },
        }
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
               datatable.clear().draw();
               datatable.rows.add(data); // Add new data
               datatable.columns.adjust().draw()
          }
        });
    });
});
