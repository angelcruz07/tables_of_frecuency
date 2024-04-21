function sumNumbers(data) {
	let numbers = data.length
	let sum = 0
	for (let i = 0; i <= numbers; i++) {
		sum += data[0]
	}

	return sum
}

data = [
	1.7, 1.6, 1.9, 1.8, 1.9, 1.7, 1.8, 1.6, 1.9, 1.7, 1.9, 1.8, 1.9, 1.8, 1.6,
	1.8, 1.9, 1.7, 1.9, 1.8
]

// data = [
// 	119, 109, 124, 119, 106, 112, 112, 112, 112, 109, 112, 124, 109, 109, 109,
// 	106, 124, 112, 112, 106
// ]

// data = [3.2, 3.1, 2.4, 4.0, 3.5, 3.0, 3.5, 3.8, 4.2, 4.9]

console.log(sumNumbers(data))
