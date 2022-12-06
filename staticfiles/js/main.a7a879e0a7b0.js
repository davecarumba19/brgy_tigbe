function showTime(){
    var date = new Date();
    var h = date.getHours(); 
    var m = date.getMinutes(); 
    var s = date.getSeconds(); 
    var session = "AM";
    
    if(h == 0){
        h = 12;
    }
    
    if(h > 12){
        h = h - 12;
        session = "PM";
    }
    
    h = (h < 10) ? "0" + h : h;
    m = (m < 10) ? "0" + m : m;
    s = (s < 10) ? "0" + s : s;
    
    var time = h + ":" + m + ":" + s + " " + session;
    document.getElementById("DigitalCLOCK").innerText = time;
    document.getElementById("DigitalCLOCK").textContent = time;
    
    setTimeout(showTime, 1000);
    
}
 
showTime();

function drawChart1() {
    var data = google.visualization.arrayToDataTable([
      ['Population', 'Number People'],
      ['Male',     11859],
      ['Female',      11829],
    ]);

    var options = {
      title: 'GENDER',
      pieHole: 0.4,
    };

    var chart = new google.visualization.PieChart(document.getElementById('donutchart1'));
    chart.draw(data, options);
  }

  function drawChart2() {
    var data = google.visualization.arrayToDataTable([
      ['Population', 'Number People'],
      ['Non-Voters', 3799],
      ['Voters',    19889]
    ]);

    var options = {
      title: 'VOTERS',
      pieHole: 0.4,
    };

    var chart = new google.visualization.PieChart(document.getElementById('donutchart2'));
    chart.draw(data, options);
  }

  function drawChart3() {
    var data = google.visualization.arrayToDataTable([
      ['Population', 'Number People'],
      ['Children (17 Below)',  5920],
      ['Senior Citizens (60 Up)', 5919],
      ['Adult (18 - 59)',    11849]
    ]);

    var options = {
      title: 'AGE',
      pieHole: 0.4,
    };

    var chart = new google.visualization.PieChart(document.getElementById('donutchart3'));
    chart.draw(data, options);
  }