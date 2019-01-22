$(document).ready(function() {

    var table = $('#data_frame').DataTable( {
         "aLengthMenu": [
                  [20, 50, 100, 200, -1],
                  [20, 50, 100, 200, "All"]],
        "pageLength": 20,
        'scrollCollapse': true,
        'deferRender': true,
        'scroller': true,
        'paging': true,
        'type': "POST",
        'bPaginate': true,
        'stripeClasses':['stripe_even','stripe_odd'],
        'language': { search: "", info: "<b>_START_</b> to <b>_END_</b> out of <b>_TOTAL_</b>" },
        'responsive': true,
        'dom': 
        "<'row'<'col-sm-3'l><'col-sm-6 text-center'><'col-sm-3'f>>" +
        "<'row'<'col-sm-12'tr>>" +
        "<'row'<'col-sm-12'p>>"
    });

    $("div.toolbar").html("<img id='toggle_button' class='density' onclick='tightRows()' src='tight.png' width=30px>");

    $('.dataTables_filter input')
       .off()
       .on('keyup', function() {
          console.log(this.value);
          
          $('#data_frame').DataTable().search(this.value.trim(), false, false).draw();
       });    

} );