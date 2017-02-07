$(document).ready(function() {
  $('#main_table tfoot th').each(function(){
        var title = $(this).text();
        $(this).html( '<input type="text" style="width:100%"/>' );
    });

  var table = $('#main_table').DataTable({
    "processing": true,
    'ajax': {
      method: "GET",
      url: "http://abitu.net/tickets_admin/get_data",
      dataType: "jsonp",
      contentType: "jsonp",
      error: handleGetDataError
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

  $('#main_table').on('click', '.editButton', function(){
    $($(this).parent().parent().find('td')[3]).text();
    modal_init($(this).parent().parent().find('td'));
    $('#popupEdit').modal("show");
  });

  $('#main_table').on('click', '.conversationButton', function(){
    var conversationButtonId = $(this).attr('id');
    var conversationId = conversationButtonId.slice(18);
    if(conversationId == '0'){
      ticketHtml = $($(this).parent().parent().find('td')[4]).html();
      ticketId = $($(this).parent().parent().find('td')[0]).text();
      $(conversationDialog).html(ticketHtml +
                              '<textarea class="form-control" rows="7" id="textareaAnswer' + ticketId + '"></textarea>' +
                              '<button class="btn btn-primary answerButton" id="sendAnswerButton' + conversationId + '">' +
                              'Ответить</button>');
    }else{
      conversation_modal_init(conversationId);
    }
    $('#popupConversation').modal("show");
  })

  $(document).on('click', '.answerButton', function(){
    var conversationId = $(this).attr('id').slice(16);
    var answerText = $($(this).parent().find('textarea')[0]).val();
    var ticketId = $($(this).parent().find('textarea')[0]).attr('id').slice(14);
    conversation_send_answer(conversationId, answerText, ticketId);
  });

});

$('#modal_button').click(function() {
    var xmlRequest = $.ajax({
      method: "GET",
      url: "http://abitu.net/tickets_admin/send_data",
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

function handleGetDataError(xhr, textStatus, error){
  alert("Please, log in as admin on abitu.net");
}

function conversation_send_answer(conversationId, answerText, ticketId){
  var answerRequest = $.ajax({
    method: "GET",
    url: "http://abitu.net/tickets_admin/send_answer",
    dataType: "jsonp",
    contentType: "jsonp",
    data: {
      "conversation_id": conversationId,
      "answer_text": answerText,
      "ticket_id": ticketId
    }
  });
  answerRequest.done(function(response){

  });
}

function conversation_modal_init(conversationId){
  var conversationRequest = $.ajax({
    method: "GET",
    url: "http://abitu.net/tickets_admin/get_conversation",
    dataType: "jsonp",
    contentType: "jsonp",
    data: {
      "conversation_id": conversationId
    }
  });
  conversationRequest.done(function(response){
    $(conversationDialog).html(response.conversation +
                                '<textarea class="form-control" rows="7" id="textareaAnswer0"></textarea>' +
                                '<button class="btn btn-primary answerButton" id="sendAnswerButton' + conversationId + '">' +
                                'Ответить</button>');
  });
}

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
