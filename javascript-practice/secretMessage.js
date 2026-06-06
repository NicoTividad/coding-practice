let secretMessage = [
  'Learning',
  'is',
  'not',
  'about',
  'what',
  'you',
  'get',
  'right',
  'in',
  'the',
  'beginning,',
  'but',
  'about',
  'the',
  'work',
  'you',
  'put',
  'in',
  'to',
  'develop',
  'real',
  'understanding.'
];

secretMessage.pop()
console.log(secretMessage)

secretMessage[0] = 'Programming'
console.log(secretMessage)

secretMessage.push('!!')
console.log(secretMessage)

secretMessage.shift()
console.log(secretMessage)

secretMessage.unshift('Studying')
console.log(secretMessage)

secretMessage.splice(6,5)
console.log(secretMessage)

let openMessage = secretMessage.slice(0,7)
console.log(openMessage)


console.log(openMessage.join(' '))