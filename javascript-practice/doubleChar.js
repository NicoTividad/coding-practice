function doubleChar(str) {
    let newStr = []
	for (let i = 0; i < str.length; i++){
        newStr.push(str[i])
        newStr.push(str[i])
    }
    return newStr.join('')
}

console.log(doubleChar('String'))