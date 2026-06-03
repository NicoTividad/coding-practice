function getComputerChoice(){
    const value = Math.floor(Math.random()*3)
    if (value===0){
        return 'Rock'
    } else if (value===1) {
        return 'Paper'
    } else {
        return 'Scissors'
    }
}

function getUserChoice(userInput){
    if (userInput==='Rock'){
        return userInput
    } else if (userInput==='Paper'){
        return userInput
    } else if (userInput==='Scissors'){
        return userInput
    } else {
        return null
    }
}

function determineWinner(user, comp){
    let result;
    if (user===comp){
        result = 'Tie!'
    } else if (user==='Rock' && comp==='Scissors'){
        result = 'You Win!'
    } else if (user==='Scissors' && comp==='Paper'){
        result = 'You Win!'
    } else if (user==='Paper' && comp==='Rock'){
        result = 'You Win!'
    } else {
        result =  'You Lose!'
    }
    return `${result} You chose ${user} and the comp chose ${comp}`
       
}

function playGame(userInput){
    let comp = getComputerChoice()
    let user = getUserChoice(userInput)
    if (user===null){
        return 'You did\'t write a correct gesture.'
    } else {
        return determineWinner(user,comp)
    }
}

// console.log(getUserChoice('Rock'))
// console.log(getComputerChoice())

console.log(playGame('Rock'))