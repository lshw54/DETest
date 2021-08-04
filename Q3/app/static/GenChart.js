var c1 = document.getElementById("c1").innerHTML;
var c2 = document.getElementById("c2").innerHTML;
var c3 = document.getElementById("c3").innerHTML;
var c1t = document.getElementById("c1t").innerHTML;
var c2t = document.getElementById("c2t").innerHTML;
var c3t = document.getElementById("c3t").innerHTML;
var ctx = document.getElementById('canvas_bar');
var ctx2 = document.getElementById('canvas_bar2');
var canvas_bar = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['薯片', '林林', '正氣'],
        datasets: [{
            label: 'Vote Result',
            data: [c1.split(" ")[0],c2.split(" ")[0],c3.split(" ")[0]],
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
            yAxes: [{ticks: {beginAtZero: true,responsive: true}}]}
        
    }
});
var canvas_bar = new Chart(ctx2, {
    type: 'bar',
    data: {
        labels: ['薯片', '林林', '正氣'],
        datasets: [{
            label: 'Last 10mins Vote Result',
            data: [c1t.split(" ")[0],c2t.split(" ")[0],c3t.split(" ")[0]],
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
            yAxes: [{ticks: {beginAtZero: true,responsive: true}}]}
        
    }
});