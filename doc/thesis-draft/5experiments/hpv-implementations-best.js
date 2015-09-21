{
  "legend": {
    "symbolWidth": 120
  },
  "chart": {
    "height": 700,
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
    "text": "Accuracy Development of Different HPV Implementations When Increasing the Epochs, Word Vector Dimensionality 48"
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
      "text": "Accuracy in %"
    },
    "min": 80,
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
      [1, 82.308], [2, 86.98], [3, 88.064], [4, 88.44], [5, 88.82], [6, 88.972], [7, 89.08], [8, 89.108], [9, 89.272], [10, 89.272], [11, 89.268], [12, 89.308], [13, 89.384], [14, 89.368], [15, 89.384], [16, 89.424], [17, 89.416], [18, 89.396], [19, 89.4], [20, 89.416]
    ],
    "pointStart": 1
  }, {
    "dashStyle": "solid",
    "name": "Hierarchical paragraph vectors 4",
    "data": [
      [1, 84.34], [2, 87.664], [3, 88.44], [4, 88.856], [5, 88.992], [6, 89.136], [7, 89.352], [8, 89.396], [9, 89.484], [10, 89.5], [11, 89.564], [12, 89.552], [13, 89.544], [14, 89.592], [15, 89.596], [16, 89.58], [17, 89.636], [18, 89.616], [19, 89.62], [20, 89.608]
    ],
    "pointStart": 1
  }, {
    "dashStyle": "DashDot",
    "name": "Hierarchical paragraph vectors 6",
    "data": [
      [1, 82.512], [2, 86.484], [3, 87.472], [4, 88.216], [5, 88.404], [6, 88.676], [7, 88.884], [8, 88.872], [9, 88.948], [10, 89.036], [11, 89.124], [12, 89.076], [13, 89.1], [14, 89.108], [15, 89.092], [16, 89.1], [17, 89.116], [18, 89.084], [19, 89.076], [20, 89.076]
    ],
    "pointStart": 1
  }, {
    "dashStyle": "dot",
    "name": "Hierarchical paragraph vectors 7",
    "color": "#8085e9",
    "data": [
      [1, 84.308], [2, 87.08], [3, 87.88], [4, 88.524], [5, 88.876], [6, 89.056], [7, 89.124], [8, 89.176], [9, 89.196], [10, 89.228], [11, 89.272], [12, 89.208], [13, 89.224], [14, 89.252], [15, 89.264], [16, 89.284], [17, 89.268], [18, 89.284], [19, 89.284], [20, 89.28]
    ],
    "pointStart": 1
  }]
}
