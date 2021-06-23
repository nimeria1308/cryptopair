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

const month_names = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
];

function select_changed() {
    const period = document.getElementById("period").value;
    const year_select = document.getElementById("year");
    const month_select = document.getElementById("month");

    var show_year = false;
    var show_month = false;

    switch (period) {
        case "month":
            show_year = true;
            break;
        case "day":
            show_year = true;
            show_month = true;
            break;
    }

    year_select.style.display = show_year ? "inline-block" : "none";
    month_select.style.display = show_month ? "inline-block" : "none";

    draw_chart();
}

var chart;

function draw_chart() {
    const pairs_select = document.getElementById("currency_pairs");
    const pair_id = pairs_select.value;

    const period_select = document.getElementById("period");
    const period = period_select.value;

    const year_select = document.getElementById("year");
    const year = year_select.value;

    const month_select = document.getElementById("month");
    const month = month_select.value;

    const ctx = document.getElementById('chart').getContext('2d');

    var url;
    switch (period) {
        case "year":
            url = `/api/pair/${pair_id}/year`;
            break;
        case "month":
            url = `/api/pair/${pair_id}/month/${year}`;
            break;
        case "day":
            url = `/api/pair/${pair_id}/day/${year}/${month}`;
            break;
        case "realtime":
            url = `/api/pair/${pair_id}`;
            break;
    }

    get_json(url, function(bid_data) {
        // prepare data
        const labels = []
        const bids = []

        const pair = pairs[pair_id];
        const base = currencies[pair[0]];
        const quote = currencies[pair[1]];

        for (i in bid_data) {
            bids.push(bid_data[i][0]);
            labels.push(bid_data[i][1]);
        }

        const data_text = `${base[1]} (${base[0]}) in ${quote[1]} (${quote[0]})`

        const data = {
            labels: labels,
            datasets: [{
                label: data_text,
                data: bids,
                borderColor: 'rgb(255, 99, 132)',
                tension: 0.4
            }]
        }

        // Period text as title
        const title = period_select.options[period_select.selectedIndex].text;

        // prepare config
        const config = {
            type: 'line',
            data: data,
            options: {
                responsive: true,
                plugins: {
                    title: {
                        display: true,
                        text: title,
                    },
                },
                interaction: {
                    intersect: false,
                },
                scales: {
                    x: {
                        display: true,
                        title: {
                            display: true,
                            text: `${base[1]} (${base[0]})`
                        }
                    },
                    y: {
                        display: true,
                        title: {
                            display: true,
                            text: `${quote[1]} (${quote[0]})`
                        },
                    }
                }
            },
        };

        if (chart) {
            chart.destroy();
        }

        chart = new Chart(ctx, config);
    });
}

function page_loaded() {
    get_json("/api/currencies", function(c) {
        currencies = c;
        get_json("/api/pairs", function(p) {
            pairs = p;

            fill_pairs();
            draw_chart();
        });
    })
}