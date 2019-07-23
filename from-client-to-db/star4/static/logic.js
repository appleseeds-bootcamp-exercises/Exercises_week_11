getActors = () => {
    $.get('/get_actors', function populateActors(data, status) {
        data = JSON.parse(data)
        newContent = $('<ul></ul>')
        for (let index = 0; index < data.length; index++) {
            newContent.append(`<li>${data[index].full_name}</li>`)
        }
        $('#content').html(newContent)
    })
}
$(document).ready(getActors)
