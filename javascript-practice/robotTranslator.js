let string = 'apple pie'
let robot = ['b','e','o','p']
let result = []
for (let i = 0; i < string.length; i++){
    // console.log(string[i])
    for (let j = 0; j < robot.length; j++){
        // console.log(robot[j])
        if (string[i]===robot[j]){
            // console.log(robot[j])
            result.push(robot[j])
            if (robot[j]==='e' || robot[j]==='o'){
                result.push(robot[j])
            } 
        }
    }
}

console.log(result.join('').toUpperCase())