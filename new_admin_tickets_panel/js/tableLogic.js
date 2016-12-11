$(document).ready(function() {
  $('#main_table tfoot th').each(function(){
        var title = $(this).text();
        $(this).html( '<input type="text" style="width:100%"/>' );
    });

  var table = $('#main_table').DataTable({
    "processing": true,
    'ajax': {
      method: "GET",
      url: "http://localhost:5022/get_data",
      dataType: "jsonp",
      contentType: "jsonp",
    },
    "columns": [
      {"data": "id_ticket"},
      {"data": "time"},
      {"data": "user_info"},
      {"data": "browser"},
      {"data": "ticket_data"},
      {"data": "url"},
      {"data": "id_type"},
      {"data": "priority"},
      {"data": "status"},
      {"data": "conversation_id"},
      {"data": "admin_id"},
      {"data": "editButton"}
    ]
  });

  table.columns().every( function () {
    var that = this;

    $('input', this.footer()).on('keyup change', function(){
        if(that.search() !== this.value) {
            that
                .search(this.value)
                .draw();
        }
    });
  });

  $('#main_table').on('click', 'tr td button', function(){
    $($(this).parent().parent().find('td')[3]).text();
    modal_init($(this).parent().parent().find('td'));
    $('#popupEdit').modal("show");
  });

});

$('#modal_button').click(function() {
    var xmlRequest = $.ajax({
          method: "GET",
          url: "http://localhost:5022/send_data",
          dataType: "jsonp",
          contentType: "jsonp",
          data: {
            "ticket_id": $('#modal_ticket_id').text(),
            "ticket_type": $('#modal_ticket_type').val(),
            "ticket_priority": $('#modal_ticket_priority').val(),
            "ticket_status": $('#modal_ticket_status').val(),
            "conversation_id": $('#modal_conversation_id').val(),
            "admin_id": $('#modal_admin_id').val()
          }
    });
    xmlRequest.done(function(){
      location.reload();
    });
});


function modal_init(td_list){
  $('#modal_ticket_id').text($(td_list[0]).text());
  $('#modal_time').text($(td_list[1]).text());
  $('#modal_user_info').html($(td_list[2]).html());
  $('#modal_browser').text($(td_list[3]).text());
  $('#modal_ticket_info').html($(td_list[4]).html());
  $('#modal_url').text($(td_list[5]).text());
  $('#modal_ticket_type').attr("value", $(td_list[6]).text());
  $('#modal_ticket_priority').attr("value", $(td_list[7]).text());
  $('#modal_ticket_status').attr("value", $(td_list[8]).text());
  $('#modal_conversation_id').attr("value", $(td_list[9]).text());
  $('#modal_admin_id').attr("value", $(td_list[10]).text());
}
/*
function add_content() {
    var xmlRequest = $.ajax({
        method: "GET",
        url: "http://localhost:5022/get_data",
        dataType: "jsonp",
        contentType: "jsonp",
        data: {}
    });
    xmlRequest.done(function(data){
        for (var i = 0; i < data.length; i++)
        {
          console.log(data[i].id_ticket);
            $('#main_table_body').append(
              '<tr>' +
                '<td>'+ data[i].id_ticket + '</td>' +
                '<td>'+ data[i].time + '</td>' +
                '<td>id- ' +
                  data[i].id_user +
                  '<br>' + data[i].name +
                  '<br>' + data[i].email +
                  '<br>' + data[i].phone +
                '</td>' +
                '<td>' + data[i].browser + '</td>' +
                '<td>' +
                  '<strong align="center">' + data[i].title +
                  '</strong>' +
                  '<br>' + data[i].text +
                '</td>' +
                '<td>' + data[i].url + '</td>' +
                '<td>' + data[i].id_type + '</td>' +
                '<td>'+ data[i].priority + '</td>' +
                '<td>' + data[i].status + '</td>' +
                '<td>'+ data[i].conversation_id + '</td>' +
                '<td>' + data[i].admin_id + '</td>' +
                '<td>' +
                  'Редактировать' +
                '</td>' +
              '</tr>'
            );
        }
    });
}

*/
