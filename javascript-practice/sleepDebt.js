function getSleepHours(day){
    if (day==='Monday' || day==='Tuesday'){
        return 9
    } else if (day==='Wednesday' || day==='Thursday'){
        return 7
    } else if (day==='Friday' || day==='Saturday'){
        return 5
    } else {
        return 8
    }
}

function getActualSleepHours(){
    let hours = getSleepHours('Monday') + getSleepHours('Tuesday') +
    getSleepHours('Wednesday') + getSleepHours('Thursday') +
    getSleepHours('Friday') + getSleepHours('Saturday') + getSleepHours('Sunday')
    return hours
}

function getIdealSleepHours(){
    let hours = 4
    return hours * 7
}

function calculateSleepDebt(){
    let idealHours = getIdealSleepHours()
    let actualHours = getActualSleepHours()
    if (actualHours === idealHours){
        return 'you got the perfect amount of sleep'
    } else if (actualHours > idealHours) {
        return `you got more than needed by ${actualHours-idealHours} `
    } else {
        return `you should get more rest, you're short by ${idealHours-actualHours}`
    }
}

console.log(getActualSleepHours())
console.log(getIdealSleepHours())
console.log(calculateSleepDebt())