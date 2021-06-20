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

    console.log(`New pair id ${pair_id} for period ${period}`);
    var ctx = document.getElementById('chart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
            datasets: [{
                label: '# of Votes',
                data: [12, 19, 3, 5, 2, 3],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
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
