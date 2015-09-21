{
  "legend": {
    "symbolWidth": 120
  },
  "chart": {
    "height": 550,
    "style": {
      "fontFamily": "Computer Modern Sans"
    }
  },
  "line": {
    "dataLabels": {
      "enabled": true
    }
  },
  "title": {
    "text": "x"
  },
  "xAxis": {
    "title": {
      "text": "Runtime in Epochs per PV"
    },
    "type": "numeric",
    "tickInterval": 5
  },
  "yAxis": {
    "title": {
      "text": "Mean Accuracy in %"
    },
    "min": 83,
    "max": 90,
    "type": "numeric",
    "minorTickInterval": 1,
    "tickInterval": 1
  },
  "tooltip": {
    "headerFormat": "<b>{series.name}</b><br />",
    "pointFormat": "Epochs = {point.x}, Accuracy = {point.y}"
  },
  "series": [{
    "dashStyle": "LongDash",
    "name": "Hierarchical paragraph vectors 0",
    "data": [
      [1, 83.05], [2, 87.66], [3, 88.76], [4, 89.26], [5, 89.53], [6, 89.68], [7, 89.77], [8, 89.84], [9, 89.86], [10, 89.87], [11, 89.9], [12, 89.89], [13, 89.9], [14, 89.88], [15, 89.87], [16, 89.87], [17, 89.87], [18, 89.86], [19, 89.86], [20, 89.85], [21, 89.85]
    ],
    "pointStart": 1
  }, {
    "dashStyle": "solid",
    "name": "Hierarchical paragraph vectors 4",
    "data": [
      [2.02, 84.8], [4.04, 87.89], [6.06, 88.86], [8.08, 89.33], [10.10, 89.58], [12.12, 89.74], [14.14, 89.85], [16.16, 89.9], [18.18, 89.94], [20.20, 89.96], [21, 89.96]
    ],
    "pointStart": 1
  }, {
    "dashStyle": "DashDot",
    "name": "Hierarchical paragraph vectors 6",
    "data": [
      [1.75, 83.06], [3.50, 87.31], [5.25, 88.43], [7.00, 88.93], [8.75, 89.18], [10.50, 89.33], [12.25, 89.38], [14.00, 89.44], [15.75, 89.45], [17.50, 89.44], [19.25, 89.45], [21, 89.43]
    ],
    "pointStart": 1
  }]
}

