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
        url: "http://localhost:5022",
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
                    '<td>' + data[i].status + '</td>' +
                '</tr>'
            );
        }
    });
}