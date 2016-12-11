$(document).ready(function(){
    clear_table();
    get_tickets();
    $('#main_table').DataTable();
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
              '<td>id тикета</td>' +
              '<td>' + data.id_ticket + '</td>' +
            '</tr>' +
            '<tr>' +
              '<td>Время</td>' +
              '<td>' + data.time + '</td>' +
            '</tr>' +
            '<tr>' +
              '<td>id пользователя</td>' +
              '<td>' + data.id_user + '</td>' +
            '</tr>' +
            '<tr>' +
              '<td>Имя</td>' +
              '<td>' + data.name + '</td>' +
            '</tr>' +
            '<tr>' +
              '<td>email</td>' +
              '<td><input type="text" class="form-control" id="edit_email" value="' + data.email + '"></td>' +
            '</tr>' +
            '<tr>' +
              '<td>Телефон</td>' +
              '<td><input type="text" class="form-control" id="edit_phone" value="' + data.phone + '"></td>' +
            '</tr>' +
            '<tr>' +
              '<td>Браузер</td>' +
              '<td>' + data.browser + '</td>' +
            '</tr>' +
            '<tr>' +
              '<td>Заголовок</td>' +
              '<td>' + data.title + '</td>' +
            '</tr>' +
            '<tr>' +
              '<td>Текст</td>' +
              '<td>' + data.text + '</td>' +
            '</tr>' +
            '<tr>' +
              '<td>Url</td>' +
              '<td>' + data.url + '</td>' +
            '</tr>' +
            '<tr>' +
              '<td>Тип тикета</td>' +
              '<td>' +
                '<div class="input-group">' +
                  '<input type="radio" name="id_type" checked>Методист ЗФТШ<br>' +
                  '<input type="radio" name="id_type">Евент<br>' +
                  '<input type="radio" name="id_type">Техподдержка<br>' +
                '</div>' +
              '</td>' +
            '</tr>' +
            '<tr>' +
              '<td>Приоритет</td>' +
              '<td><input type="text" class="form-control" id="edit_id_ticket" value="' + data.priority + '"></td>' +
            '</tr>' +
            '<tr>' +
              '<td>Статус</td>' +
              '<td>' +
                data.status + '<br>' +
                '<button type="button" class="btn btn-primary">Закрыть тикет</button>' +
              '</td>' +
            '</tr>' +
            '<tr>' +
              '<td>Диалог абиту</td>' +
              '<td>' + data.conversation_id + '</td>' +
            '</tr>' +
            '<tr>' +
              '<td>Админ</td>' +
              '<td><input type="text" class="form-control" id="edit_admin_id" value="' + data.admin_id + '"></td>' +
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
    var id_type = [];
    var status = [];

    $('#find-div').find('[name="id_type"]').each(function() {
        if($(this).is(':checked')){
            id_type.push($(this).attr('value'));
        }
    });
    console.log(id_type);
    var xmlRequest = $.ajax({
        method: "GET",
        url: "http://abitu.net/tickets_admin",
        dataType: "jsonp",
        contentType: "jsonp",
        data: {
            'time': '0',
            'id_type': JSON.stringify(id_type),
            'status': JSON.stringify(['solved']),
            'order': JSON.stringify(['time'])
        }
    });
    xmlRequest.done(function(data){
        for (var i = 0; i < data.length; i++)
        {
            $('#data_table').append(
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
                  '<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#myModal' + i + '">' +
                    'Редактировать' +
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
