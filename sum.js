function sumNumbers(data) {
	let numbers = data.length
	let sum = 0
	for (let i = 0; i <= numbers; i++) {
		sum += data[i]
	}
	return sum
}

data = [3, 3, 3, 1]

console.log(sumNumbers(data))
