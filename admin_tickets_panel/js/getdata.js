$(document).ready(function(){
    clear_table();
    get_tickets();
});

$('input').change(function() {
    clear_table();
    get_tickets();
});

function clear_table() {
    $('#data_table').empty();
}

function view_more_info(data, id){
    return '<div class="modal fade" id="' + id + '" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">' +
    '<div class="modal-dialog" role="document">' +
      '<div class="modal-content">' +
        '<div class="modal-header">' +
          '<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>' +
          '<h4 class="modal-title" id="myModalLabel">Расширенная информация/редактировать</h4>' +
        '</div>' +
        '<div class="modal-body">' +
          '<table class="table">' +
            '<tbody>' +
              '<tr>' +
                '<td>Заголовок</td>' +
                '<td>' + data.title + '</td>' +
              '</tr>' +
              '<tr>' +
                '<td>Время отправки</td>' +
                '<td>' + data.time + '</td>' +
              '</tr>' +
              '<tr>' +
                '<td>Полный текст</td>' +
                '<td>' + data.description + '</td>' +
              '</tr>' +
              '<tr>' +
                '<td>Тип тикета</td>' +
                '<td>' +
                  '<div class="input-group">' +
                    '<input type="radio" name="ticket_type" checked>Методист ЗФТШ<br>' +
                    '<input type="radio" name="ticket_type">Евент<br>' +
                    '<input type="radio" name="ticket_type">Техподдержка<br>' +
                  '</div>' +
                '</td>' +
              '</tr>' +
              '<tr>' +
                '<td>Подразделение ФЦ</td>' +
                '<td>' +
                  '<input type="radio" name="domain">Abitu.net<br>' +
                  '<input type="radio" name="domain" checked>ЗФТШ<br>' +
                  '<input type="radio" name="domain">Летняя школа<br>' +
                '</td>' +
              '</tr>' +
              '<tr>' +
                '<td>Пользователь</td>' +
                '<td>' +
                  data.userid + '<br>' +
                  '<button type="button" class="btn btn-default">Перейти к диалогу</button>' +
                '</td>' +
              '</tr>' +
              '<tr>' +
                '<td>Статус</td>' +
                '<td>' +
                  data.status + '<br>' +
                  '<button type="button" class="btn btn-primary">Закрыть тикет</button>' +
                '</td>' +
              '</tr>' +
            '</tbody>' +
          '</table>' +
        '</div>' +
        '<div class="modal-footer">' +
          '<button type="button" class="btn btn-default" data-dismiss="modal">Закрыть</button>' +
          '<button type="button" class="btn btn-primary">Сохранить</button>' +
        '</div>' +
      '</div>' +
    '</div>' +
  '</div>'
}

function get_tickets() {
    var time = [];
    var ticket_type = [];
    var domain = [];
    var status = [];
    $('#find-div').find('[name="domain"]').each(function() {
        if($(this).is(':checked')){
            domain.push($(this).attr('value'));
        }
    });
    $('#find-div').find('[name="ticket_type"]').each(function() {
        if($(this).is(':checked')){
            ticket_type.push($(this).attr('value'));
        }
    });
    console.log(domain);
    console.log(ticket_type);
    var xmlRequest = $.ajax({
        method: "GET",
        url: "http://abitu.net/tickets_admin",
        dataType: "jsonp",
        contentType: "jsonp",
        data: {
            'time': '0',
            'ticket_type': JSON.stringify(ticket_type),
            'domain': JSON.stringify(domain),
            'status': JSON.stringify(['solved']),
            'order': JSON.stringify(['time'])
        }
    });
    xmlRequest.done(function(data){
        for (var i = 0; i < data.length; i++)
        {
            $('#data_table').append(
                '<tr>' +
                    '<td>' + data[i].time + '</td>' +
                    '<td>' + data[i].title + '</td>' +
                    '<td>' + data[i].description + '</td>' +
                    '<td>' + data[i].ticket_type + '</td>' +
                    '<td>' + data[i].domain + '</td>' +
                    '<td>' + data[i].userid + '</td>' +
                    '<td>' +
                    '<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#myModal' +
                    i + '">' +
                    'Смотреть ещё' +
                    '</button>' +
                    '</td>' +
                '</tr>'
            );
            var moreInfo = view_more_info(data[i], 'myModal' + i.toString());
            $('body').append(
                moreInfo
            );
        }
    });
}