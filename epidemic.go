// array or any structure which holds 6 hermits
// random choice of 5 the rest hermits - who sick one is asking for help
// is this hermit ill or not
// if not ill - mark him as ill an continue with him as "main person"
// if already ill - stop

package main

import (
	"fmt"
	"math/rand"
	"time"
)

var hermits = map[int]int{
	1: 0,
	2: 0,
	3: 0,
	4: 0,
	5: 0,
	6: 0,
}

func main() {
	// make hermit number 1 feel sick
	hermits[1] = 1

	rand.Seed(time.Now().UTC().UnixNano())
	for i := 1; i <= 100; i++ {
		hermits = map[int]int{1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
		currentSick := 1
		whosNext := currentSick
		whosNext = randomNext(whosNext, currentSick)

		count := 0
		for spread(whosNext) == 0 {
			count++
			currentSick = whosNext
			whosNext = randomNext(whosNext, currentSick)
		}
		fmt.Println(count)
	}
}

func randomNext(hermitID int, currentSick int) int {
	for hermitID == currentSick {
		hermitID = rand.Intn(len(hermits)) + 1
	}
	return hermitID
}

// returns 0 if next hermit is not sick yet
func spread(hermitID int) int {
	// need to remember if he was sick
	heWasSick := hermits[hermitID]
	// now he is sick anyway
	hermits[hermitID] = 1
	return heWasSick
}
