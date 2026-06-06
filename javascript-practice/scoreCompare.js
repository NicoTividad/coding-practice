function scoreCompare(arr){
    let points = 0;
    for (let i=0; i<arr.length; i++){
        // console.log(`\nComparing ${i[0]} with ${i[2]}`)
        // console.log(arr[i])
        if (arr[i][0]>arr[i][2]){
            points += 3
        } else if (arr[i][0]===arr[i][2]){
            points++
        }
    }
    return points
}

arr = ["2:1", "3:3", "0:1", "4:1", "1:1", "1:2"]
console.log(scoreCompare(arr))