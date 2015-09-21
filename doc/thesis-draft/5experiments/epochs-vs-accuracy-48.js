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
    "min": 82,
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
      [1, 82.59], [2, 87.04], [3, 88.08], [4, 88.6], [5, 88.9], [6, 89.07], [7, 89.2], [8, 89.28], [9, 89.34], [10, 89.37], [11, 89.4], [12, 89.43], [13, 89.44], [14, 89.45], [15, 89.47], [16, 89.48], [17, 89.49], [18, 89.49], [19, 89.5], [20, 89.5]
    ],
    "pointStart": 1
  }, {
    "dashStyle": "solid",
    "name": "Hierarchical paragraph vectors 4",
    "data": [
      [1, 84.38], [2, 87.38], [3, 88.3], [4, 88.76], [5, 89], [6, 89.13], [7, 89.21], [8, 89.3], [9, 89.34], [10, 89.37], [11, 89.39], [12, 89.42], [13, 89.43], [14, 89.44], [15, 89.45], [16, 89.46], [17, 89.46], [18, 89.47], [19, 89.47], [20, 89.47]
    ],
    "pointStart": 1
  }, {
    "dashStyle": "DashDot",
    "name": "Hierarchical paragraph vectors 6",
    "data": [
      [1, 82.65], [2, 86.62], [3, 87.68], [4, 88.22], [5, 88.54], [6, 88.76], [7, 88.91], [8, 88.99], [9, 89.04], [10, 89.11], [11, 89.15], [12, 89.15], [13, 89.18], [14, 89.2], [15, 89.21], [16, 89.22], [17, 89.23], [18, 89.24], [19, 89.25], [20, 89.25]
    ],
    "pointStart": 1
  }]
}

