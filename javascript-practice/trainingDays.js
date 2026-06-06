const setUp = 'Training Days';

function getRandEvent(){
    num = Math.floor(Math.random()*3)
    if (num === 0){
        return 'Marathon'
    } else if (num === 1){
        return 'Triathlon'
    } else {
        return 'Pentathlon'
    }
}

const getTrainingDays = (event) => {
    if (event==='Marathon'){
        return 50
    } else if (event==='Triathlon'){
        return 100
    } else {
        return 200
    }
}

const getRandPrize = () => {
    let num = Math.floor(Math.random()*3)
    if (num === 0){
        return 'Money'
    } else if (num === 1){
        return 'Fame'
    } else {
        return 'Charcoal'
    }
}

const logEvent = (name,event) => {
    let eventDescription = `${name} will do ${event} with ${getTrainingDays(event)} days.`
    console.log(eventDescription)
}

const logPrize = (name) => {
    let prize = `${name} gets ${getRandPrize()}`
    console.log(prize)
}

logEvent('Nico','Marathon')
logPrize('Nico')