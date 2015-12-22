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

func main() {
  var hermits = map[int]int{
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
  }

  // make hermit number 1 feel sick
  hermits[1] = 1

  rand.Seed(time.Now().UTC().UnixNano())
  //whos_next := rand.Intn(len(hermits))

  for i:=0; i<=100; i++ {
	whos_next := rand.Intn(len(hermits)) + 1
	fmt.Println(whos_next)
  }
  //fmt.Println(whos_next)
}
