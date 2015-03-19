// Playground - noun: a place where people can play

import Cocoa

var population: Int = 2000
var message: String
var hasPostOffice: Bool = true

if population < 10000 {
    message = "\(population) is a small town!"
} else if population >= 10000 && population < 50000 {
    message = "\(population) is a medium town!"
} else if population >= 50000 && population < 1000000 {
    message = "\(population) is pretty big!"
} else {
    message = "\(population) is a metropolis!"
}

println (message)

if !hasPostOffice {
    println("Where do we buy stamps?")
}


// ternary operator 
// a ? b : c
// message = population < 10000 ? "\(population) is a small town!" : "\(population) is pretty big!"

// println (message)

