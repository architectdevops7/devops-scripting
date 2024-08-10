package main

import (
	"fmt"
	"time"
)

func PrintTimeStampThailandBangkok() {
	loc, _ := time.LoadLocation("Asia/Bangkok")
	t := time.Now().In(loc)

	fmt.Println(t)
	fmt.Println(t.Unix())
}

func PrintTimeStampAmericaLA() {
	loc, _ := time.LoadLocation("America/Los_Angeles")
	t := time.Now().In(loc)

	fmt.Println(t)
	fmt.Println(t.Unix())
}

func main() {
	PrintTimeStampAmericaLA()
	PrintTimeStampThailandBangkok()
}
