{
  "chart": {
    "height": 550, "style":{"fontFamily":"Computer Modern Sans"}
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
      "text": "TF-IDF Dimensionality"
    },
    "type": "numeric",
    "tickInterval": 100
  },
  "yAxis": {
    "title": {
      "text": "Accuracy in %"
    },
    "min": 63,
    "max": 88,
    "type": "numeric",
    "minorTickInterval": 1,
    "tickInterval": 2
  },
  "tooltip": {
    "headerFormat": "<b>{series.name}</b><br />",
    "pointFormat": "Tfid features = {point.x}, Accuracy = {point.y}"
  },
  "series": [{
    "name": "Epochs 1",
    "data": [
      [32, 63.436], [64, 67.04], [96, 73.572], [200, 76.668], [300, 79.584], [400, 82.7], [500, 84.244], [600, 84.92], [700, 85.24], [800, 85.756], [900, 86.048], [1000, 86.384], [1100, 86.672], [1200, 86.696], [1300, 86.928], [1400, 87.088], [1500, 86.976], [1600, 87.268], [1700, 87.22], [1800, 87.316], [1900, 87.432], [2000, 87.384], [2100, 87.544], [2200, 87.444], [2300, 87.516], [2400, 87.684], [2500, 87.592]],
    "pointStart": 1
  }]
}

