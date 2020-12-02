// Read in timeSeries data

d3.csv("https://raw.githubusercontent.com/spearjen/TransitData/spearjay/resources/timeSeries.csv").then(function(data) {
    console.log(data);

    var titlesArray=data.map(data=>data.Title);
    console.log(titlesArray);

    var urlsArray=data.map(data=>data.url);
    console.log(urlsArray);

    var blurbsArray=data.map(data=>data.Blurb);
    console.log(blurbsArray);

    // Drowpdown selection
    var value = document.getElementById("changeViz");
    for(index in titlesArray) {
        value.options[value.options.length] = new Option(titlesArray[index], index);
        }
    })

    $("#changeViz").on("change",indexIdNo)
    var fakeEvent={
        target:{
            value:0
        }
    };

// change everything on user selection
    function indexIdNo(event) {
        d3.csv("https://raw.githubusercontent.com/spearjen/TransitData/spearjay/resources/timeSeries.csv").then(function(data) {
        
        // var dropdownMenu = d3.select("#changeViz");
        var vizContainer=$("#vizContainer")
        vizContainer.html('<div id="graph"></div>')

        // Assign the value of the dropdown menu option to a variable
        var indexNo = event.target.value;
        console.log(indexNo);

        // variables
        var graphId = data[indexNo];
        console.log(graphId);

        var titlePicked = graphId.Title;
        console.log(titlePicked);

        var blurbPicked = graphId.Blurb;
        console.log(blurbPicked);

        var urlPicked= graphId.url;
        console.log(urlPicked);

        function initViz() {
            // if (viz) {
            //     // viz.dispose();
                var containerDiv = document.getElementById("graph"),
                url = urlPicked;
                var viz = new tableau.Viz(containerDiv, url);
            // }
            // else {
            //     var containerDiv = document.getElementById("vizContainer"),
            //     url = urlPicked;
            //     var viz = new tableau.Viz(containerDiv, url);
            // }
        };

    //     // function loadViz (containerDiv,urlPicked) {
    //     //     if (viz) {
    //     //         viz.dispose();
    //     //     }
    //     //     viz = new tableau.Viz(containerDiv,urlPicked)
    //     // }
        initViz();
    });

    //     })
}
    indexIdNo(fakeEvent);
    
