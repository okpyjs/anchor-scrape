const allUrl = window.location.href
const parsedUrl = new URL(allUrl);
const params = parsedUrl.searchParams;
const url = params.get("url")


function getRandomColor() {
    const r = Math.floor(Math.random() * 256); // generate a random value for the red component (0-255)
    const g = Math.floor(Math.random() * 256); // generate a random value for the green component (0-255)
    const b = Math.floor(Math.random() * 256); // generate a random value for the blue component (0-255)
    return `rgb(${r}, ${g}, ${b})`; // return the color as an RGB string
}


function chart(data){
    const sortedObj = Object.fromEntries(Object.entries(data.anchor_text_distribution).sort((a, b) => b[1] - a[1]));
    $('.fa-spinner').addClass('d-none');
    $('.lead').addClass('d-none');
    $('#results-section').removeClass('d-none');
    $('#total-links').text(data.total_links);

    chartBgColor = []
    chartBorderColor = []
    for(i = 0; i < 9; i ++) {
        chartBgColor.push(getRandomColor())
        chartBorderColor.push(getRandomColor())
    }

    // other color
    chartBgColor.push(`#aaa`)
    chartBorderColor.push(`#aaa`)

    var chartData = {
        labels: [],
        datasets: [{
            // label: 'Anchor Text Distribution',
            data: [],
            backgroundColor: chartBgColor,
            borderColor: chartBorderColor,
            borderColor: 'white',
            borderWidth: 2,
            hoverOffset: 8,
        }]
    };
    var labels = Object.keys(sortedObj);
    var dataValues = Object.values(sortedObj);
    var otherValue = 0;
    for (var i = 0; i < labels.length; i++) {
        if (i < 9) {
            chartData.labels.push(labels[i]);
            chartData.datasets[0].data.push(dataValues[i]);
        } else {
            otherValue += dataValues[i];
        }
    }
    if (otherValue > 0) {
        chartData.labels.push('Other');
        chartData.datasets[0].data.push(otherValue);
    }

    // var myChart = new Chart(
    //     document.getElementById('chart'),
    //     config
    // );
    // var chartCtx = document.getElementById('chart').getContext('2d');
    // var chart = new Chart(chartCtx, {
    //     type: 'pie',
    //     data: chartData
    // });
    const options = {
        responsive: true,
        aspectRatio: 0.7,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                position: 'top',
                labels: {
                    font: {
                        size: 18,
                        weight: 'bold'
                    }
                }
            },
            title: {
                display: true,
                text: 'Anchor Text Distribution',
                font: {
                    size: 24,
                    weight: 'bold'
                }
            },
            tooltip: {
                callbacks: {
                    label: function (context) {
                        return `${context.label}: ${context.formattedValue}`;
                    }
                }
            }
        },
        layout: {
            padding: {
                left: 0,
                right: 0,
                top: 0,
                bottom: 0,
            },
            position: {
                top: 30
            }
        },
        cutout: '0%',
        // rotation: 0.5 * Math.PI,
        // circumference: 1.5 * Math.PI,
        animation: {
            duration: 2000,
            easing: 'easeInOutQuart'
        },
        hover: {
            mode: 'nearest',
            intersect: true
        },
        onClick: function (event, elements) {
            console.log(event);
            console.log(elements);
        }
    };

    const config = {
        type: 'pie',
        data: chartData,
        options: options
    };

    var myChart = new Chart(
        document.getElementById('chart'),
        config
    );

    var linksTableBody = '';
    data.links.forEach(function (link) {
        linksTableBody += `
            <tr>
                <td>
                    <a href="${url + link.url}">${link.url}</a>
                </td>
                <td>${link.anchor_text}</td>
            </tr>`;
    });
    $('#links-table-body').html(linksTableBody);
}
