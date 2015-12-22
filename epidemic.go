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
  whos_next := 1

  for whos_next == 1 {
		whos_next = rand.Intn(len(hermits)) + 1
  }
  fmt.Println(whos_next)
	if spread(whos_next) == 0 {
		// what should be done here?
	}

}

// returns 0 if next hermit is not sick yet
func spread(hermit_id int) int {
	// need to remember if he was sick
	he_was_sick = hermits[hermit_id]
	// now he is sick anyway
	hermits[hermit_id] = 1
	return he_was_sick
}
