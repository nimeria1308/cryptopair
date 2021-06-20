var currencies;
var pairs;

function fill_pairs() {
    const pairs_select = document.getElementById("currency_pairs");

    for (pair_id in pairs) {
        const pair = pairs[pair_id];
        const base_id = pair[0];
        const base = currencies[base_id];
        const quote_id = pair[1];
        const quote = currencies[quote_id];

        const pair_text = `${base[1]} (${base[0]}) in ${quote[1]} (${quote[0]})`;

        const opt = document.createElement("option");
        opt.value = pair_id;
        opt.innerText = pair_text;
        pairs_select.appendChild(opt);
    }
}

function draw_chart() {
    const pairs_select = document.getElementById("currency_pairs");
    const pair_id = pairs_select.value;

    const period_select = document.getElementById("period");
    const period = period_select.value;

    alert(`New pair id ${pair_id} for period ${period}`);
    // TODO
}

function page_loaded() {
    get_json("/api/currencies", function (c) {
        currencies = c;
        get_json("/api/pairs", function (p) {
            pairs = p;

            fill_pairs();
            draw_chart();
        });
    })
}
