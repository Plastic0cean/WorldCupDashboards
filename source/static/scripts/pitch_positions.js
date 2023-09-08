var positions = document.querySelectorAll(".marker");

function addPositionAbbreviation (positions) {
    for (let index = 0; index < positions.length; index++)
    {
        var positionName = positions[index].classList[1];
        positions[index].innerHTML = positionsAbbreviations[positionName];
    }
}

const positionsAbbreviations = {
    "forward": "FW",
    "left-winger": "LW",
    "right-winger": "RW",
    "attacking-midfielder": "AMF",
    "center-midfielder": "CM",
    "defensive-midfielder": "DM",
    "center-back": "CB",
    "left-back": "LB",
    "right-back": "RB",
    "goal-keeper": "GK"
}


addPositionAbbreviation(positions);