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
      "text": "Epochs"
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
      [1, 83.05], [2, 87.66], [3, 88.76], [4, 89.26], [5, 89.53], [6, 89.68], [7, 89.77], [8, 89.84], [9, 89.86], [10, 89.87], [11, 89.9], [12, 89.89], [13, 89.9], [14, 89.88], [15, 89.87], [16, 89.87], [17, 89.87], [18, 89.86], [19, 89.86], [20, 89.85]
    ],
    "pointStart": 1
  }, {
    "dashStyle": "solid",
    "name": "Hierarchical paragraph vectors 4",
    "data": [
      [1, 84.8], [2, 87.89], [3, 88.86], [4, 89.33], [5, 89.58], [6, 89.74], [7, 89.85], [8, 89.9], [9, 89.94], [10, 89.96], [11, 89.96], [12, 89.96], [13, 89.96], [14, 89.96], [15, 89.96], [16, 89.95], [17, 89.95], [18, 89.95], [19, 89.94], [20, 89.94]
    ],
    "pointStart": 1
  }, {
    "dashStyle": "DashDot",
    "name": "Hierarchical paragraph vectors 6",
    "data": [
      [1, 83.06], [2, 87.31], [3, 88.43], [4, 88.93], [5, 89.18], [6, 89.33], [7, 89.38], [8, 89.44], [9, 89.45], [10, 89.44], [11, 89.45], [12, 89.43], [13, 89.42], [14, 89.4], [15, 89.39], [16, 89.39], [17, 89.38], [18, 89.37], [19, 89.36], [20, 89.35]
    ],
    "pointStart": 1
  }]
}

