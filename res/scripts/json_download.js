function get_json(url, handler) {
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function () {
        const text = xhttp.responseText;
        const json_result = JSON.parse(text)
        handler(json_result);
    }

    xhttp.open("GET", url);
    xhttp.send();
}
