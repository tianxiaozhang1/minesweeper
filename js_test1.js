var numbers = [[0, 0, 1, 1, 1, 9, 1, 0, 0, 1, 1, 1, 1, 9, 2, 9, 1, 1, 2, 3, 3, 9, 2, 9, 1, 1, 9, 2, 1, 1],
                [0, 0, 9, 3, 2, 1, 2, 1, 1, 1, 9, 2, 2, 2, 2, 1, 1, 1, 9, 9, 9, 2, 2, 1, 1, 1, 1, 3, 9, 2],
                [0, 0, 2, 9, 1, 2, 9, 4, 9, 2, 2, 9, 4, 9, 3, 1, 2, 9, 1, 0, 0, 0, 1, 1, 2, 3, 0, 0, 1, 1],
                [0, 1, 1, 2, 2, 2, 2, 4, 9, 2, 1, 1, 3, 9, 2, 0, 1, 2, 2, 1, 0, 1, 1, 1, 1, 9, 0, 3, 9, 2],
                [9, 2, 1, 1, 9, 2, 2, 9, 3, 3, 1, 1, 2, 2, 2, 0, 0, 1, 9, 2, 1, 1, 9, 2, 2, 2, 1, 3, 9, 3],
                [3, 9, 1, 2, 3, 9, 2, 2, 9, 2, 9, 1, 1, 9, 1, 0, 1, 2, 3, 9, 2, 2, 2, 4, 9, 2, 0, 2, 9, 3],
                [9, 3, 3, 3, 9, 3, 2, 2, 1, 2, 1, 1, 1, 1, 1, 0, 1, 9, 2, 2, 9, 1, 1, 9, 9, 2, 0, 1, 3, 9],
                [1, 2, 9, 9, 2, 2, 9, 2, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 3, 3, 2, 2, 2, 1, 0, 0, 3, 9],
                [1, 2, 2, 2, 1, 2, 3, 9, 1, 0, 1, 1, 1, 1, 9, 1, 0, 0, 0, 1, 9, 9, 1, 0, 0, 0, 0, 1, 3, 9],
                [9, 2, 0, 1, 1, 2, 9, 2, 2, 2, 3, 9, 2, 3, 2, 2, 0, 0, 1, 2, 4, 3, 2, 0, 0, 1, 1, 2, 9, 3],
                [9, 3, 1, 1, 9, 2, 1, 1, 1, 9, 9, 3, 9, 2, 9, 3, 2, 1, 1, 9, 2, 9, 2, 2, 1, 2, 9, 3, 3, 9],
                [2, 9, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 2, 3, 4, 9, 9, 2, 2, 2, 2, 2, 9, 3, 9, 4, 3, 9, 2, 1],
                [1, 2, 3, 9, 1, 1, 2, 9, 2, 1, 1, 1, 2, 9, 3, 9, 4, 3, 9, 1, 1, 2, 3, 4, 9, 4, 9, 3, 1, 0],
                [0, 1, 9, 2, 1, 1, 9, 2, 2, 9, 3, 3, 9, 2, 3, 3, 9, 2, 1, 2, 2, 9, 2, 9, 2, 3, 9, 2, 1, 1],
                [1, 2, 1, 2, 1, 2, 1, 1, 1, 3, 9, 9, 2, 2, 3, 9, 4, 2, 0, 1, 9, 2, 2, 1, 1, 1, 1, 2, 3, 9],
                [9, 1, 0, 1, 9, 1, 0, 0, 0, 2, 9, 3, 1, 1, 9, 9, 9, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 9, 9]];

window.onload = function() {
    showSquares(0, 0);
}

function showSquares(sqx, sqy) {
    var displayArea = [];
    var displayPoints = [];
    displayPoints.push(sqx*30+sqy)
    var fourWays = [[0,-1],[0,1],[-1,0],[1,0]];
    console.log("Before", displayPoints)

    roundsLeft = 16
    while (roundsLeft > 0) {

        for (var i1 in displayPoints) {
            for (var x1 in fourWays) {
                var sqax = Math.floor(displayPoints[i1]/30)
                var sqay = displayPoints[i1]%30
                
                if (sqax+fourWays[x1][0] >= 0 && sqax+fourWays[x1][0] <= 15 && sqay+fourWays[x1][1] >= 0 && sqay+fourWays[x1][1] <= 29) {
                    
                    if (numbers[sqax+fourWays[x1][0]][sqay+fourWays[x1][1]] === 0) {
                        console.log(sqax+fourWays[x1][0], sqay+fourWays[x1][1])
                        if (((sqax+fourWays[x1][0])*30+sqay+fourWays[x1][1]) in displayPoints) {
                        }
                        else {
                            displayPoints.push((sqax+fourWays[x1][0])*30+sqay+fourWays[x1][1])
                        }
                    }
                }
            }
        }

        var displayPoints = displayPoints.filter((v, i, a) => a.indexOf(v) === i);
        roundsLeft -= 1
        console.log("*", roundsLeft, displayPoints)
    }

    for (i1 in displayPoints) {
        displayArea.push([Math.floor(displayPoints[i1]/30), displayPoints[i1]%30])
    }

    console.log("LENGTH", displayArea.length)
    console.log("displayArea", displayArea[0])

}