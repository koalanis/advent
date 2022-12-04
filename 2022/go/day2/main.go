package main

import (
	"_/Users/kalebalanis/Github/advent/2022/go/utils"
	"bufio"
	"fmt"
	"log"
)

var year = 2022
var day = 2

func main() {
	file, err := utils.GetAdventDataFile(2022, 2)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		text := scanner.Text()
		fmt.Println(text)
	}
}
