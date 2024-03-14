
function form_to_json(selector){
    let formData = $(selector).serializeArray(); // Serialize form data as an array
    let formDataJson = {};
    $.each(formData, function(i, field) {
        formDataJson[field.name] = field.value;
    });

    return formDataJson;
}