
$(function () {
    $('#container').highcharts({
        chart: {
            type: 'scatter',
            zoomType: 'xy'
        },
        title: {
            text: 'XY GRAPH'
        },
        xAxis: {
            title: {
                text: "{{ graph_x }}"
            }
        },
        yAxis: {
            title: {
                text: "{{ graph_y }}"
            }
        },
        plotOptions: {
            scatter: {
                marker: {
                    radius: 1.0
                },
                color: '#fa0000',
                lineWidth: 0.5
            }
        },
        series: [{
            name: 'Data pull',
            data:
                [{% for line in lines|dictsort:graph_x %}
                    [
                    {% for key, value in line.items %}
                        {% if key == graph_x %}
                            {{ value }}
                        {% endif %}
                    {% endfor %},

                    {% for key, value in line.items %}
                        {% if key == graph_y %}
                            {{ value }}
                        {% endif %}
                    {% endfor %}
                    ],
            {% endfor %}]
        }]
    });
});

